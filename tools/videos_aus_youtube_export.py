"""Erzeugt src/data/videos.json aus dem YouTube-Studio-Export.

Export: YouTube Studio > Analytics > Erweiterter Modus > Zeitraum "Gesamte Dauer" > Reiter "Inhalte" > Export als CSV.
Aufruf: python3 tools/videos_aus_youtube_export.py <Pfad zu Tabellendaten.csv>
Übernommen werden nur öffentliche Angaben (ID, Titel, Datum, Dauer, Aufrufe). Die Export-Datei selbst nicht ins Repo legen.
"""
import csv, json, sys
from datetime import datetime
from pathlib import Path

ziel = Path(__file__).resolve().parent.parent / "src" / "data" / "videos.json"
videos = []
with open(sys.argv[1], encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["Videos"] == "Gesamt" or not r["Videos"]:
            continue
        videos.append({
            "id": r["Videos"],
            "titel": r["Videotitel"].strip(),
            "datum": datetime.strptime(r["Veröffentlichungszeitpunkt des Videos"], "%b %d, %Y").date().isoformat(),
            "dauer": int(r["Dauer"] or 0),
            "aufrufe": int(r["Aufrufe"] or 0),
        })
videos.sort(key=lambda v: v["datum"], reverse=True)
ziel.write_text(json.dumps(videos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"{len(videos)} Videos nach {ziel}")
