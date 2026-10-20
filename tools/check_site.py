#!/usr/bin/env python3
"""
Prüft die gebaute Seite gegen den WordPress-Export.

Aufruf:
    python3 -I check_site.py <dist-ordner> <report.json> <zaehlmarken.csv>

Prüfungen:
  1. Jede alte Adresse (Beiträge + Seiten) existiert in der neuen Seite (oder ist bewusst umgeleitet)
  2. VG-Wort: jede öffentliche Zählmarke ist im Artikel eingebaut, keine private Zählmarke im Code
  3. Interne Links zeigen auf existierende Seiten
  4. Bildverweise unter /wp-content/uploads/ (Liste der benötigten Dateien; Existenz, sobald Bilder da sind)
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

REDIRECTED = {"cookie-richtlinie-eu": "/datenschutz/", "e-mail-marketing-guide": "/thema/e-mail-marketing/", "youtube": "/videos/", "die-4ps-fuer-deinen-marketing-mix": "/die-4ps-des-marketings-ein-umfassender-leitfaden-fuer-einsteiger/", "4ps-marketing-beispiele": "/die-4ps-des-marketings-ein-umfassender-leitfaden-fuer-einsteiger/", "das-aidas-modell-die-weiterentwicklung-eines-bekannten-modells": "/die-aida-formel-dein-schluessel-zum-erfolgreichen-marketing/", "mit-dem-jobs-to-be-done-modell-kundenbeduerfnisse-besser-verstehen": "/jobs-to-be-done-jtbd-fuer-die-kundenbeduerfnisse/", "phasen-der-customer-journey": "/die-customer-journey/", "kaufentscheidungsprozess-so-ticken-kunden": "/der-kaufentscheidungsprozess/", "mit-dem-aaker-modell-baust-du-eine-starke-marke-auf": "/aakers-5-dimensionen-modell/", "das-kapferer-identitaetsprisma": "/das-identitaetsprisma-von-kapferer/", "marktpositionierung-konkurrenz-schlagen": "/marktpositionierung-erfolg-planen/", "warum-du-eine-mission-und-vision-fuer-dein-unternehmen-benoetigst": "/mission-vs-vision-der-wegweiser-fuer-dein-unternehmen/", "die-kunst-einer-wirkungsvollen-vision-und-mission": "/mission-vs-vision-der-wegweiser-fuer-dein-unternehmen/", "wie-du-ein-effektives-unternehmensleitbild-erstellst": "/wieso-du-ein-unternehmensleitbild-benoetigst/", "das-7-s-modell-ein-umfassender-blick-auf-unternehmenserfolg": "/das-mckinsey-7-s-modell/", "balanced-scorecard-fuer-nachhaltigen-erfolg": "/balanced-scorecard-einfach-erklaert/", "warum-das-moderne-betriebsmodell-nutzen": "/warum-du-ein-modernes-betriebsmodell-fuer-dein-unternehmen-brauchst/", "okr-connected-strategic-implementation-stack": "/der-connected-strategic-stack/", "okrs-im-change-management": "/okr-im-change-management/", "preiselastizitaet-der-nachfrage": "/preiselastizitaet-der-nachfrage-ein-muss-fuer-jedes-marketing/", "diminishing-returns-das-gesetz-der-abnehmenden-ertraege-erklaert": "/ertragsgesetz-grundlagen-und-praktische-bedeutung/", "customer-lifecycle-clc": "/der-customer-life-cycle-im-ueberblick/", "wie-du-den-customer-lifetime-value-erhoehst": "/customer-lifetime-value-der-wert-deiner-kunden/", "ctr-vs-ctor": "/ctr-vs-cto-im-e-mail-marketing/", "click-to-open-rate-ctor-fuer-erfolgreiches-e-mail-marketing": "/ctr-vs-cto-im-e-mail-marketing/", "die-bedeutung-der-e-mail-personalisierung": "/e-mail-personalisierung-wie-du-deine-kunden-wirklich-erreichst/", "was-du-ueber-personalisierte-e-mails-wissen-musst": "/e-mail-personalisierung-wie-du-deine-kunden-wirklich-erreichst/", "warum-du-eine-pillar-page-auf-deiner-webseite-brauchst": "/effektive-inhalte-mit-pillar-seiten/", "kotters-8-schritte-modell-zur-steuerung-der-marketingveraenderungen": "/kotters-8-stufen-modell/", "kurt-lewins-phasenmodell": "/lewins-3-stufen-modell/", "zeitfresser-meeting-und-9-gegenmassnahmen": "/tipps-fuer-effektive-meetings/"}


def page_exists(dist, path):
    path = unquote(path.split("#")[0].split("?")[0])
    if not path or path == "/":
        return (dist / "index.html").exists()
    p = dist / path.lstrip("/")
    return (p / "index.html").exists() or (p.is_file())


def main(dist, report_file, csv_file):
    dist = Path(dist)
    report = json.load(open(report_file, encoding="utf-8"))["items"]
    ergebnis = {}

    # 1. Alte Adressen
    fehlend = []
    for it in report:
        slug = it["slug"]
        if slug == "index":
            ok = (dist / "index.html").exists()
        elif slug in REDIRECTED:
            ok = (dist / slug / "index.html").exists()
        else:
            ok = (dist / slug / "index.html").exists()
        if not ok:
            fehlend.append(it["link"])
    ergebnis["adressen_geprueft"] = len(report)
    ergebnis["adressen_fehlend"] = fehlend

    # 2. VG-Wort
    csv.field_size_limit(sys.maxsize)
    rows = list(csv.DictReader(open(csv_file, encoding="utf-8"), delimiter=";"))
    private = {r["Private Zählmarke"].strip() for r in rows if r["Private Zählmarke"].strip()}
    erwartet = {}
    for r in rows:
        if r["Link"].strip() and r["Seite gelöscht"] == "0":
            slug = urlparse(r["Link"].strip()).path.strip("/") or "index"
            erwartet[slug] = r["Öffentliche Zählmarke"].strip()

    html_files = list(dist.rglob("*.html"))
    alle_texte = {}
    for f in html_files:
        alle_texte[f] = f.read_text(encoding="utf-8", errors="replace")
    gesamt = "\n".join(alle_texte.values())

    vg_fehlt = []
    for slug, pub in erwartet.items():
        f = dist / ("index.html" if slug == "index" else f"{slug}/index.html")
        if slug in REDIRECTED or slug == "index":
            continue  # Startseite und Cookie-Seite gibt es in der alten Form nicht mehr
        if not f.exists() or pub not in alle_texte.get(f, ""):
            vg_fehlt.append(slug)
    ergebnis["vgwort_erwartet"] = len([s for s in erwartet if s not in REDIRECTED and s != "index"])
    ergebnis["vgwort_fehlt"] = vg_fehlt
    ergebnis["vgwort_nicht_mehr_genutzt"] = [s for s in erwartet if s in REDIRECTED or s == "index"]
    ergebnis["private_zaehlmarken_im_code"] = sum(1 for p in private if p in gesamt)

    # 3. Interne Links
    kaputt = Counter()
    quelle = {}
    for f, text in alle_texte.items():
        for href in re.findall(r'href="(/[^"]*)"', text):
            if href.startswith(("//", "/pagefind/", "/_astro/")) or href in ("/rss.xml", "/sitemap-index.xml", "/favicon.png", "/wp-ids.json"):
                continue
            if href.startswith("/wp-content/"):
                continue
            if not page_exists(dist, href):
                kaputt[href] += 1
                quelle.setdefault(href, str(f.relative_to(dist).parent))
    ergebnis["interne_links_kaputt"] = [{"link": k, "anzahl": v, "z_b_in": quelle[k]} for k, v in kaputt.most_common()]

    # 4. Bilder
    bilder = set(re.findall(r'(/wp-content/uploads/[^"\s\')]+)', gesamt))
    vorhanden = [b for b in bilder if (dist / unquote(b).lstrip("/")).exists()]
    ergebnis["bilder_referenziert"] = len(bilder)
    ergebnis["bilder_vorhanden"] = len(vorhanden)
    ergebnis["bilder_fehlend_liste"] = sorted(bilder - set(vorhanden))

    print(json.dumps({k: (v if not isinstance(v, list) or len(v) < 40 else f"{len(v)} Einträge") for k, v in ergebnis.items()},
                     ensure_ascii=False, indent=1))
    Path("check_result.json").write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(*sys.argv[1:4])
