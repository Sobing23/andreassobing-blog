#!/usr/bin/env python3
"""
Räumt die Schlagwörter in den Markdown-Dateien auf.

Aufruf:
    python3 -I tags.py <ordner mit .md-Dateien>

Vorgehen:
  1. Schreibweisen vereinheitlichen (E-Mail/email/EMail, Groß/klein, Bindestriche)
  2. Gleichbedeutende Schlagwörter zusammenführen (MERGE)
  3. Nichtssagende Schlagwörter entfernen (DROP)
  4. Nur Schlagwörter behalten, die danach in mindestens MIN_COUNT Artikeln vorkommen
Die Datei wird in place umgeschrieben; alle anderen Felder bleiben unverändert.
"""
import collections
import json
import re
import sys
from pathlib import Path

MIN_COUNT = 3

# normalisierter Schlüssel -> Ziel-Schlüssel
MERGE = {
    "kampagne": "kampagnen",
    "e-mail kampagne": "kampagnen",
    "text": "texte",
    "schreiben": "texte",
    "copywrite": "texte",
    "conversions": "conversion",
    "strategie unternehmen": "unternehmensstrategie",
    "strategie": "unternehmensstrategie",
    "social": "social media",
    "social network": "social media",
    "kreativität": "kreativitätstechniken",
    "ideen": "kreativitätstechniken",
    "brainstorming": "kreativitätstechniken",
    "web zitate": "zitate",
    "commercial masterpieces": "commercials",
    "aufbau newsletter": "verteileraufbau",
    "verteilerliste": "verteileraufbau",
    "e-mail": "e-mail marketing",
    "chatgpt plugins": "chatgpt",
    "startups": "startup",
    "suchmaschine (seo&sem)": "seo",
}

# Schlagwörter ohne Aussagekraft
DROP = {"download", "facts", "tipps", "interview", "studie", "internet", "video", "trends", "mobile", "design"}

# Anzeigeformen
DISPLAY = {
    "e-mail marketing": "E-Mail-Marketing",
    "e-mail marketing guide": "E-Mail Marketing Guide",
    "okr": "OKR",
    "seo": "SEO",
    "crm": "CRM",
    "dsgvo": "DSGVO",
    "chatgpt": "ChatGPT",
    "e commerce": "E-Commerce",
    "verteileraufbau": "Verteileraufbau",
    "texte": "Texte & Copywriting",
    "unternehmensstrategie": "Unternehmensstrategie",
    "kreativitätstechniken": "Kreativitätstechniken",
    "startup": "Startups",
    "kampagnen und automatisierungen": "Kampagnen & Automatisierung",
}


def key(tag):
    k = tag.lower().strip()
    k = re.sub(r"\be[\s-]?mails?\b", "e-mail", k)
    k = re.sub(r"[\s_]+", " ", k).replace(" - ", " ").replace("-", " ").replace("e mail", "e-mail")
    k = MERGE.get(k, k)
    return k


def main(folder):
    files = sorted(Path(folder).glob("*.md"))
    variants = collections.defaultdict(collections.Counter)
    per_file = {}
    for f in files:
        fm = f.read_text(encoding="utf-8").split("---", 2)[1]
        keys = set()
        for t in re.findall(r'^  - "(.*)"$', fm, re.M):
            k = key(t)
            if k in DROP:
                continue
            variants[k][t] += 1
            keys.add(k)
        per_file[f] = keys

    counts = collections.Counter(k for ks in per_file.values() for k in ks)
    keep = {k for k, n in counts.items() if n >= MIN_COUNT}

    def display(k):
        if k in DISPLAY:
            return DISPLAY[k]
        best = variants[k].most_common(1)[0][0]
        return best[0].upper() + best[1:]

    mapping = {k: display(k) for k in sorted(keep)}
    tagged = 0
    for f, keys in per_file.items():
        text = f.read_text(encoding="utf-8")
        _, fm, body = text.split("---", 2)
        fm = re.sub(r'^tags:\n(?:  - ".*"\n)+', "", fm, flags=re.M)
        new = sorted({mapping[k] for k in keys if k in keep})
        if new:
            tagged += 1
            block = "tags:\n" + "".join(f'  - "{t}"\n' for t in new)
            # nach "category:" bzw. "image:" einfügen, sonst vor "wpId"
            fm = re.sub(r"^(wpId: )", block + r"\1", fm, count=1, flags=re.M)
        f.write_text("---" + fm + "---" + body, encoding="utf-8")

    print(json.dumps({"schlagwoerter": len(mapping), "artikel_mit_schlagwort": tagged,
                      "liste": {v: counts[k] for k, v in mapping.items()}}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
