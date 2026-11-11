"""Meldet geänderte Seiten per IndexNow an Bing, Yandex, Seznam, Naver und andere teilnehmende Suchmaschinen.

Aufruf im Veröffentlichungsablauf nach dem Deploy:
  python3 tools/indexnow.py <alter-commit> <neuer-commit>   meldet die Seiten der geänderten Artikel
  python3 tools/indexnow.py --alle                          meldet alle Adressen aus der veröffentlichten Sitemap

Der Schlüssel liegt öffentlich unter https://andreassobing.de/<schlüssel>.txt, so will es IndexNow.
"""
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

SITE = 'andreassobing.de'
SCHLUESSEL = '30f754ea75ff51074eeb68f79f5b8afd'
ENDPUNKT = 'https://api.indexnow.org/indexnow'
WURZEL = Path(__file__).resolve().parent.parent


def slug_aus(text):
    m = re.search(r'^slug:\s*"?([^"\n]+)"?', text, re.M)
    return m.group(1).strip() if m else None


def geaenderte_adressen(alt, neu):
    """Adressen der Artikel und Seiten, die zwischen zwei Commits geändert, neu angelegt oder gelöscht wurden."""
    if not alt or set(alt) == {'0'}:  # erster Push eines Zweigs: nichts zu vergleichen
        return []
    diff = subprocess.run(['git', 'diff', '--name-status', alt, neu, '--', 'src/content'],
                          capture_output=True, text=True, cwd=WURZEL, check=True).stdout
    adressen = set()
    for zeile in diff.splitlines():
        teile = zeile.split('\t')
        status, pfad = teile[0], teile[-1]
        if not pfad.endswith('.md'):
            continue
        if status.startswith('D'):  # gelöscht: Inhalt aus dem alten Stand lesen, die Adresse leitet jetzt weiter
            text = subprocess.run(['git', 'show', f'{alt}:{pfad}'], capture_output=True, text=True, cwd=WURZEL).stdout
        else:
            text = (WURZEL / pfad).read_text(encoding='utf-8')
        slug = slug_aus(text)
        if slug:
            adressen.add('/' if slug == 'index' else f'/{slug}/')
    if adressen:  # neue Artikel erscheinen auch auf Start- und Übersichtsseiten
        adressen.update(['/', '/archiv/', '/handbuch/'])
    return sorted(f'https://{SITE}{a}' for a in adressen)


def alle_adressen():
    with urllib.request.urlopen(f'https://{SITE}/sitemap-0.xml', timeout=30) as antwort:
        xml = antwort.read().decode('utf-8')
    return re.findall(r'<loc>([^<]+)</loc>', xml)


def melden(adressen):
    for start in range(0, len(adressen), 10000):  # IndexNow nimmt höchstens 10.000 Adressen je Anfrage
        teil = adressen[start:start + 10000]
        daten = json.dumps({'host': SITE, 'key': SCHLUESSEL, 'keyLocation': f'https://{SITE}/{SCHLUESSEL}.txt',
                            'urlList': teil}).encode()
        anfrage = urllib.request.Request(ENDPUNKT, data=daten, headers={'Content-Type': 'application/json; charset=utf-8'})
        try:
            with urllib.request.urlopen(anfrage, timeout=30) as antwort:
                print(f'IndexNow: {len(teil)} Adressen gemeldet, Antwort {antwort.status}')
        except urllib.error.HTTPError as fehler:
            # 4xx nur ausgeben: Die Seite ist zu diesem Zeitpunkt schon veröffentlicht
            print(f'IndexNow: Antwort {fehler.code} {fehler.reason}')
        except urllib.error.URLError as fehler:
            print(f'IndexNow: nicht erreichbar ({fehler.reason})')


if __name__ == '__main__':
    adressen = alle_adressen() if sys.argv[1:] == ['--alle'] else geaenderte_adressen(*sys.argv[1:3])
    if adressen:
        for a in adressen[:20]:
            print(' ', a)
        melden(adressen)
    else:
        print('IndexNow: keine geänderten Artikel')
