#!/usr/bin/env python3
"""
Wandelt den WordPress-Export (WXR) von andreassobing.de in Markdown-Dateien für Astro um.

Aufruf:
    python3 -I convert.py <datenordner> <zielordner>

Erwartet im Datenordner:
    blogitmarketing_WordPress_2026-09-25.xml      (Beiträge + Anhänge)
    blogitmarketing_WordPress_2026-09-25_1_.xml   (Seiten)
    blogitmarketing_WordPress_2026-09-25_2_.xml   (Medien)
    zaehlmarken.csv                               (Prosodia VGW OS Export)

Erzeugt im Zielordner:
    posts/<slug>.md, pages/<slug>.md
    report.json  (Auffälligkeiten je Artikel)
    images.txt   (alle referenzierten Bildpfade unter /wp-content/uploads/)
"""
import csv
import html as htmllib
import json
import re
import sys
from pathlib import Path

from lxml import etree
from markdownify import MarkdownConverter

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
}
DOMAINS = r"(?:https?:)?//(?:www\.)?(?:andreassobing\.de|hun-gry\.com|hun-gry\.de)"
UPLOAD_RE = re.compile(DOMAINS + r"(/wp-content/uploads/[^\s\"')\]>]+)", re.I)
INTERNAL_LINK_RE = re.compile(r"\]\(" + DOMAINS + r"(/[^)\s]*)?\)", re.I)
SIZE_SUFFIX_RE = re.compile(r"-\d{2,4}x\d{2,4}(?=\.[a-zA-Z]{3,4}$)")


# ---------------------------------------------------------------- Hilfsfunktionen
def t(el, path):
    return el.findtext(path, namespaces=NS) or ""


def clean(text):
    """HTML-Entities (&amp;, &#8211; …) in Klartext umwandeln."""
    return htmllib.unescape(htmllib.unescape(text or "")).strip()


def meta_of(item):
    return {
        m.findtext("wp:meta_key", namespaces=NS): m.findtext("wp:meta_value", namespaces=NS) or ""
        for m in item.findall("wp:postmeta", namespaces=NS)
    }


def yaml_str(value):
    """Sicherer YAML-String in doppelten Anführungszeichen."""
    value = (value or "").replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()
    return f'"{value}"'


def youtube_id(text):
    m = re.search(r"(?:v=|youtu\.be/|embed/|/v/)([A-Za-z0-9_-]{11})", text)
    return m.group(1) if m else None


def vimeo_id(text):
    m = re.search(r"vimeo\.com/(?:video/)?(\d+)", text)
    return m.group(1) if m else None


def original_upload_path(path):
    """/wp-content/uploads/2021/09/bild-1024x683.jpg -> /wp-content/uploads/2021/09/bild.jpg"""
    return SIZE_SUFFIX_RE.sub("", path)


# ---------------------------------------------------------------- Vorverarbeitung (HTML/Shortcodes)
def preprocess(html, issues):
    """Bereinigt WordPress-HTML vor der Markdown-Umwandlung und vermerkt Auffälligkeiten."""
    # wpautop: WordPress speichert klassische Beiträge ohne <p>; Leerzeilen sind Absätze.
    if "<p" not in html:
        blocks = re.split(r"\n\s*\n", html.strip())
        html = "\n".join(
            b if re.match(r"\s*<(h\d|ul|ol|blockquote|table|div|figure|pre|\[)", b) else f"<p>{b.strip()}</p>"
            for b in blocks if b.strip()
        )

    # YouTube: [embedyt]URL[/embedyt], [youtube]URL[/youtube], [youtube id=...]
    def yt_repl(m):
        vid = youtube_id(m.group(0))
        if not vid:
            issues.append("youtube-ohne-id")
            return ""
        return f'\n<div class="video" data-provider="youtube" data-id="{vid}"></div>\n'

    html = re.sub(r"\[embedyt[^\]]*\].*?\[/embedyt\]", yt_repl, html, flags=re.S | re.I)
    html = re.sub(r"\[youtube[^\]]*\](?:.*?\[/youtube\])?", yt_repl, html, flags=re.S | re.I)

    # Vimeo
    def vimeo_repl(m):
        vid = vimeo_id(m.group(0))
        if not vid:
            issues.append("vimeo-ohne-id")
            return ""
        return f'\n<div class="video" data-provider="vimeo" data-id="{vid}"></div>\n'

    html = re.sub(r"\[vimeo[^\]]*\](?:.*?\[/vimeo\])?", vimeo_repl, html, flags=re.S | re.I)

    # YouTube-iframes direkt im HTML
    def iframe_repl(m):
        src = m.group(0)
        vid = youtube_id(src) if "youtu" in src else None
        if vid:
            return f'\n<div class="video" data-provider="youtube" data-id="{vid}"></div>\n'
        vid = vimeo_id(src) if "vimeo" in src else None
        if vid:
            return f'\n<div class="video" data-provider="vimeo" data-id="{vid}"></div>\n'
        issues.append("iframe-entfernt")
        url = re.search(r'src=["\']([^"\']+)', src)
        return f'<p>[Eingebetteter Inhalt: <a href="{url.group(1)}">Link</a>]</p>' if url else ""

    html = re.sub(r"<iframe.*?(?:</iframe>|/>)", iframe_repl, html, flags=re.S | re.I)

    # Flash (object/embed) – technisch tot
    if re.search(r"<(object|embed)", html, re.I):
        issues.append("flash-entfernt")
        html = re.sub(r"<object.*?</object>", "", html, flags=re.S | re.I)
        html = re.sub(r"<embed[^>]*>(?:</embed>)?", "", html, flags=re.S | re.I)

    # Twitter-Skripte entfernen, Blockquote mit Tweet-Text bleibt
    if re.search(r"<script", html, re.I):
        html = re.sub(r"<script.*?</script>", "", html, flags=re.S | re.I)
        issues.append("script-entfernt")

    # SlideDeck-Plugin existiert nicht mehr
    if re.search(r"\[SlideDeck", html, re.I):
        issues.append("slidedeck-entfernt")
        html = re.sub(r"\[SlideDeck[^\]]*\]", "", html, flags=re.I)

    # Sonstige bekannte Video-Shortcodes
    if re.search(r"\[(wpvideo|googlevideo)", html, re.I):
        issues.append("altes-video-entfernt")
        html = re.sub(r"\[(wpvideo|googlevideo)[^\]]*\](?:.*?\[/\1\])?", "", html, flags=re.S | re.I)

    # [caption]...[/caption] -> <figure>
    def caption_repl(m):
        attrs, inner = m.group(1), m.group(2)
        cap = re.search(r'caption="([^"]*)"', attrs)
        img = re.search(r"<img[^>]*>", inner)
        text = cap.group(1) if cap else re.sub(r"<[^>]+>", "", re.sub(r"<img[^>]*>", "", inner)).strip()
        if not img:
            return f"<p>{text}</p>" if text else ""
        return f"<figure>{img.group(0)}<figcaption>{text}</figcaption></figure>"

    html = re.sub(r"\[caption([^\]]*)\](.*?)\[/caption\]", caption_repl, html, flags=re.S | re.I)

    # Leere Formatierungsreste wie <strong><em></em></strong>
    for _ in range(3):
        html = re.sub(r"<(strong|em|b|i|span)[^>]*>\s*</\1>", "", html, flags=re.I)

    return html


# ---------------------------------------------------------------- Markdown
class BlogConverter(MarkdownConverter):
    """markdownify mit Erhalt von <figure> und Video-Platzhaltern."""

    def convert_div(self, el, text, *args, **kwargs):
        if "video" in (el.get("class") or []):
            return f'\n\n<div class="video" data-provider="{el.get("data-provider")}" data-id="{el.get("data-id")}"></div>\n\n'
        return text

    def convert_figure(self, el, text, *args, **kwargs):
        img = el.find("img")
        cap = el.find("figcaption")
        if img is None:
            return text
        alt = (img.get("alt") or "").replace('"', "&quot;")
        caption = cap.get_text(" ", strip=True) if cap is not None else ""
        return (
            f'\n\n<figure><img src="{img.get("src")}" alt="{alt}" loading="lazy">'
            f"<figcaption>{caption}</figcaption></figure>\n\n"
        )


def to_markdown(html):
    md = BlogConverter(heading_style="ATX", bullets="-", strip=["span", "font", "center", "u"]).convert(html)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md


def rewrite_urls(md, images):
    # Bildpfade auf eigene Domain, relativ, auf Originalgröße
    def up(m):
        p = original_upload_path(m.group(1))
        images.add(p)
        return p

    md = UPLOAD_RE.sub(up, md)
    # Interne Links relativ machen
    md = INTERNAL_LINK_RE.sub(lambda m: "](" + (m.group(1) or "/") + ")", md)
    md = re.sub(r'href="' + DOMAINS + r'(/[^"]*)?"', lambda m: f'href="{m.group(1) or "/"}"', md, flags=re.I)
    return md


# ---------------------------------------------------------------- Hauptlauf
def main(data_dir, out_dir):
    data_dir, out_dir = Path(data_dir), Path(out_dir)
    parser = etree.XMLParser(huge_tree=True, recover=True)
    posts_xml = etree.parse(str(data_dir / "blogitmarketing_WordPress_2026-09-25.xml"), parser)
    pages_xml = etree.parse(str(data_dir / "blogitmarketing_WordPress_2026-09-25_1_.xml"), parser)
    media_xml = etree.parse(str(data_dir / "blogitmarketing_WordPress_2026-09-25_2_.xml"), parser)

    # Anhänge: ID -> URL
    attachments = {}
    for tree in (posts_xml, pages_xml, media_xml):
        for it in tree.findall(".//item"):
            if t(it, "wp:post_type") == "attachment":
                attachments.setdefault(t(it, "wp:post_id"), t(it, "wp:attachment_url"))

    # VG-Wort: Link -> öffentliche Zählmarke (private bleiben bewusst draußen)
    csv.field_size_limit(sys.maxsize)
    vgwort = {}
    with open(data_dir / "zaehlmarken.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter=";"):
            if row["Link"].strip() and row["Seite gelöscht"] == "0":
                vgwort[row["Link"].strip()] = f'https://{row["Server"].strip()}/{row["Öffentliche Zählmarke"].strip()}'

    # Rubriken: slug -> Rubrik-Schlüssel (von Hand/redaktionell festgelegt)
    rubriken = {}
    rub_file = data_dir / "rubriken.tsv"
    if rub_file.exists():
        with open(rub_file, encoding="utf-8") as f:
            for row in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
                rubriken[row["slug"]] = row["rubrik"]

    report, images, slugs = [], set(), set()
    for kind, tree, wp_type in (("posts", posts_xml, "post"), ("pages", pages_xml, "page")):
        target = out_dir / kind
        target.mkdir(parents=True, exist_ok=True)
        for it in tree.findall(".//item"):
            if t(it, "wp:post_type") != wp_type or t(it, "wp:status") != "publish":
                continue
            link = it.findtext("link")
            path = re.sub(r"^https?://[^/]+", "", link)
            slug = path.strip("/") or "index"
            issues = []
            meta = meta_of(it)

            html = preprocess(t(it, "content:encoded"), issues)
            md = rewrite_urls(to_markdown(html), images)

            # Rest-Shortcodes melden (Platzhalter-Wörter wie [Zielgruppe] sind Text und bleiben)
            # Eckige Klammern, auf die kein "(" folgt, sind keine Markdown-Links -> möglicher Shortcode
            leftovers = {
                m.group(0) for m in re.finditer(r"\[/?[a-z][a-z0-9_-]*(?:\s[^\]\n]*)?\](?!\()", md)
                if re.match(r"\[/?[a-z0-9_-]+(?:\s+[a-z_]+=|\])", m.group(0))
            }
            if leftovers:
                issues.append("shortcode-rest:" + ",".join(sorted(leftovers))[:120])

            image = ""
            if meta.get("_thumbnail_id") in attachments:
                m = UPLOAD_RE.search(attachments[meta["_thumbnail_id"]])
                if m:
                    image = original_upload_path(m.group(1))
                    images.add(image)

            # Beitragsbild steht in alten Artikeln zusätzlich ganz oben im Text -> dort entfernen,
            # die Vorlage zeigt es ohnehin über dem Artikel an.
            if image:
                md = re.sub(r"^\[?!\[[^\]]*\]\(" + re.escape(image) + r"[^)]*\)(?:\]\([^)]*\))?\s*", "", md, count=1)

            tags = sorted({clean(c.text) for c in it.findall("category") if c.get("domain") == "post_tag" and c.text})
            description = clean(meta.get("_yoast_wpseo_metadesc", ""))
            seo_title = clean(meta.get("_yoast_wpseo_title", ""))
            words = len(re.findall(r"\w+", re.sub(r"<[^>]+>|\]\([^)]*\)", " ", md)))
            if words < 150:
                issues.append(f"sehr-kurz:{words}-woerter")
            if not description:
                issues.append("keine-meta-beschreibung")

            fm = ["---", f"title: {yaml_str(clean(t(it, 'title')))}"]
            if seo_title and "%%" not in seo_title:
                fm.append(f"seoTitle: {yaml_str(seo_title)}")
            fm += [
                f"slug: {yaml_str(slug)}",
                f"date: {t(it, 'wp:post_date').replace(' ', 'T')}",
            ]
            if t(it, "wp:post_modified") and t(it, "wp:post_modified") != t(it, "wp:post_date"):
                fm.append(f"updated: {t(it, 'wp:post_modified').replace(' ', 'T')}")
            if description:
                fm.append(f"description: {yaml_str(description)}")
            if image:
                fm.append(f"image: {yaml_str(image)}")
            if wp_type == "post":
                if slug in rubriken:
                    fm.append(f"category: {yaml_str(rubriken[slug])}")
                else:
                    issues.append("keine-rubrik")
            if tags:
                fm.append("tags:")
                fm += [f"  - {yaml_str(x)}" for x in tags]
            if link in vgwort:
                fm.append(f"vgwort: {yaml_str(vgwort[link])}")
            fm.append(f"wpId: {t(it, 'wp:post_id')}")
            fm.append("---")

            fname = slug.replace("/", "__") + ".md"
            (target / fname).write_text("\n".join(fm) + "\n\n" + md + "\n", encoding="utf-8")
            slugs.add(slug)
            report.append({
                "type": wp_type, "slug": slug, "link": link, "title": clean(t(it, "title")),
                "date": t(it, "wp:post_date")[:10], "words": words, "vgwort": link in vgwort,
                "image": bool(image), "tags": len(tags), "issues": issues,
            })

    # VG-Wort-Marken, die keinem exportierten Artikel zugeordnet werden konnten
    unmatched_vg = [l for l in vgwort if re.sub(r"^https?://[^/]+", "", l).strip("/") not in slugs]

    (out_dir / "report.json").write_text(
        json.dumps({"items": report, "vgwort_unmatched": unmatched_vg}, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    (out_dir / "images.txt").write_text("\n".join(sorted(images)) + "\n", encoding="utf-8")
    print(f"{len(report)} Dateien erzeugt, {len(images)} Bildpfade, {len(unmatched_vg)} VG-Wort-Marken ohne Artikel")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
