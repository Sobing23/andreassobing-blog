---
title: "UTM-Parameter: So erkennst du, welche Kampagne wirklich wirkt"
seoTitle: "UTM-Parameter: Erklärung, Beispiele und Vorlage"
slug: "utm-parameter-kampagnen-tracking"
date: 2026-11-18T18:00:00
description: "UTM-Parameter einfach erklärt: die fünf wichtigsten Parameter, ein Beispiel aus dem Newsletter, wie Google Analytics sie Kanälen zuordnet, die häufigsten Fehler und eine Vorlage für einheitliche Benennung zum Herunterladen."
image: "/wp-content/uploads/2026/11/utm-parameter-titelbild.jpg"
category: "marketing"
vgwort: "https://vg09.met.vgwort.de/na/aff5dfd32bad4e30abcf3e57cfa0a226"
tags:
  - "UTM-Parameter"
  - "Web Analytics"
  - "Kampagnen-Tracking"
  - "Google Analytics"
---

Der Newsletter verlinkt auf das neue Angebot, der LinkedIn-Post auch, dazu läuft eine Anzeige. Am Ende des Monats zeigt Google Analytics einen großen Block „Direct“, ein paar Zugriffe von LinkedIn und eine Kampagne, die in drei Schreibweisen auftaucht. Welcher Kanal hat das Angebot verkauft? Ohne saubere Kennzeichnung der Links lässt sich das kaum beantworten.

UTM-Parameter lösen dieses Problem. Sie sind kleine Zusätze am Ende einer Adresse, die dem Analysetool sagen, woher ein Besuch kommt. Das Prinzip ist simpel. Schwierig wird es erst, wenn mehrere Menschen im Team Links bauen und jeder seine eigene Schreibweise hat. Deshalb gibt es am Ende dieses Artikels eine Vorlage, mit der du die Benennung vereinheitlichst.

## Was UTM-Parameter sind

UTM steht für Urchin Tracking Module. Urchin war eine Software zur Webanalyse, die Google 2005 übernommen hat und aus der Google Analytics hervorging. Die Parameter haben den Namen behalten und sind heute ein Standard: Auch andere Werkzeuge wie Matomo erkennen sie automatisch.

Technisch ist ein UTM-Parameter ein ganz normaler Parameter in der Adresse. Er steht hinter einem Fragezeichen, mehrere Parameter werden mit dem Zeichen & verbunden:

![Aufbau einer Adresse mit UTM-Parametern: Ziel-Adresse, Fragezeichen, dann utm_source=newsletter, utm_medium=email, utm_campaign=2026-11_winter-sale und utm_content=button-oben, jeweils mit & verbunden und mit Erklärung, welche Frage jeder Parameter beantwortet.](/wp-content/uploads/2026/11/utm-parameter-aufbau.jpg)

Wer auf den Link klickt, landet ganz normal auf der Zielseite. Das Analysetool liest die Parameter aus und ordnet den Besuch der Quelle, dem Medium und der Kampagne zu.

## Die wichtigsten Parameter

Google Analytics kennt mehrere UTM-Parameter. Drei davon solltest du laut Google immer setzen, die übrigen nach Bedarf:

| Parameter | beantwortet die Frage | Beispiel |
|---|---|---|
| `utm_source` | Wer schickt den Besucher? | newsletter, linkedin, google |
| `utm_medium` | Über welchen Kanal? | email, social, cpc |
| `utm_campaign` | Zu welcher Kampagne gehört der Link? | 2026-11_winter-sale |
| `utm_content` | Welches Element wurde geklickt? | button-oben, textlink-unten |
| `utm_term` | Welches bezahlte Keyword? | laufschuhe-damen |

Fehlt einer der drei Pflichtwerte, erscheint in den Berichten „(not set)“. Daneben gibt es neuere Parameter wie `utm_id` für eine Kampagnen-ID und `utm_source_platform` für die Plattform, über die eine Kampagne gesteuert wird. Für die meisten Marketingteams reichen die fünf aus der Tabelle.

Wichtig: Die Werte unterscheiden zwischen Groß- und Kleinschreibung. `utm_source=Newsletter` und `utm_source=newsletter` sind für Google Analytics zwei verschiedene Quellen. Google empfiehlt deshalb ausdrücklich, durchgehend kleinzuschreiben.

## Ein Beispiel aus dem Newsletter

Ein Onlineshop verschickt im November einen Newsletter zum Winter-Sale. Darin gibt es zwei Links zur Angebotsseite: einen Button oben und einen Textlink am Ende. Die beiden Links sehen so aus:

```
https://www.beispiel-shop.de/winter-sale/?utm_source=newsletter&utm_medium=email&utm_campaign=2026-11_winter-sale&utm_content=button-oben
https://www.beispiel-shop.de/winter-sale/?utm_source=newsletter&utm_medium=email&utm_campaign=2026-11_winter-sale&utm_content=textlink-unten
```

Quelle, Medium und Kampagne sind gleich, nur `utm_content` unterscheidet sich. So siehst du später, ob der Button oder der Textlink mehr Besuche und Käufe gebracht hat. Postet das Team dieselbe Aktion auf LinkedIn, bleibt die Kampagne gleich, Quelle und Medium ändern sich: `utm_source=linkedin&utm_medium=social`. In der Auswertung lässt sich die Kampagne dann über alle Kanäle hinweg vergleichen.

Gerade bei E-Mails lohnt sich das besonders. Viele Mailprogramme übermitteln beim Klick nicht, woher der Besuch kommt. Ohne Parameter landen solche Besuche deshalb oft im Topf „Direct“. Wie du E-Mail-Kampagnen darüber hinaus auswertest, steht im Artikel zu [Kennzahlen im E-Mail-Marketing](/kennzahlen-im-e-mail-marketing/).

## Warum utm_medium über den Kanal entscheidet

Google Analytics sortiert jeden Besuch in eine Standard-Kanalgruppe, etwa E-Mail, Organic Social oder Display. Dafür prüft es feste Regeln, und die wichtigste Rolle spielt dabei das Medium. Wer hier eigene Begriffe erfindet, findet seine Besuche später unter „Unassigned“, also nicht zugeordnet.

| Kanal in Google Analytics | passende Werte für utm_medium |
|---|---|
| Email | email, e-mail, e_mail, e mail |
| Organic Social | social, social-media, social-network, sm |
| Paid Social und Paid Search | cpc, ppc, paid-social oder andere Werte mit „cp“ oder beginnend mit „paid“, zusammen mit einer bekannten Social- oder Suchmaschinen-Quelle |
| Display | display, banner, cpm, interstitial, expandable |
| Affiliates | affiliate |
| Referral | referral, link, app |

Ein Beispiel: `utm_medium=newsletter` sieht logisch aus, passt aber zu keiner Regel. Diese Besuche fehlen dann im Kanal E-Mail. Richtig ist `utm_medium=email` und `utm_source=newsletter`. Die Regeln selbst achten übrigens nicht auf Groß- und Kleinschreibung, die Berichte zu Quelle und Kampagne aber schon.

## Die häufigsten Fehler

**Uneinheitliche Schreibweise.** Black-Friday, black_friday und blackfriday sind drei Kampagnen. Das ist der häufigste und ärgerlichste Fehler, weil er sich nachträglich nur mühsam zusammenrechnen lässt.

**UTM-Parameter auf internen Links.** Ein Banner auf der eigenen Startseite bekommt keine UTM-Parameter. Die Parameter beschreiben, wie jemand auf deine Website kommt, nicht, wo er sich darauf bewegt. In Google Analytics 4 kann ein solcher Link die Zuordnung späterer Besuche verfälschen: Kommt der Besucher beim nächsten Mal direkt, wird ihm laut Analytics Mania der Wert vom internen Link zugeschrieben. Für interne Klicks gibt es Ereignisse.

**Personenbezogene Daten in den Parametern.** Eine E-Mail-Adresse oder Kundennummer hat in `utm_content` nichts zu suchen. Google untersagt ausdrücklich, personenbezogene Daten an Google Analytics zu senden, und nennt dabei ausdrücklich die Parameter in der Adresse.

**Erfundene Medien.** Wie oben beschrieben: Ein Medium, das keine Regel kennt, landet unter „Unassigned“.

**Parameter, die unterwegs verloren gehen.** Manche Weiterleitungen geben den Teil hinter dem Fragezeichen nicht weiter. Klick deshalb jeden neuen Link einmal selbst an und prüf, ob die Parameter auf der Zielseite noch in der Adresszeile stehen.

**Manuelle Parameter für Google Ads.** Für Anzeigen bei Google gibt es die automatische Tag-Kennzeichnung mit der sogenannten gclid. Google empfiehlt, sie eingeschaltet zu lassen, auch wenn du zusätzlich UTM-Parameter verwendest.

Zum Thema Datenschutz noch ein Hinweis: Apple entfernt in Safari seit Version 17 bestimmte Klick-Kennungen wie die gclid von Google oder die fbclid von Meta, zunächst im privaten Modus sowie bei Links aus Mail und Nachrichten. Normale UTM-Parameter sind davon bisher nicht betroffen. Sie identifizieren keine einzelne Person, sondern beschreiben nur die Kampagne.

## Die Vorlage für einheitliche Benennung

UTM-Parameter scheitern selten an der Technik, sondern fast immer an der Disziplin. Die Lösung ist eine kurze, verbindliche Konvention, die das ganze Team kennt. Diese Regeln haben sich bewährt:

![Vorlage für eine UTM-Konvention: Regeln für die Schreibweise und feste Listen für utm_source und utm_medium, dazu ein Muster für utm_campaign aus Jahr, Monat und Thema sowie für utm_content aus Element und Position.](/wp-content/uploads/2026/11/utm-parameter-vorlage.jpg)

1. **Alles klein, keine Leerzeichen, keine Umlaute.** Wörter verbindest du mit Bindestrich: `winter-sale`, nicht `Winter Sale` oder `wintersale`.
2. **Feste Listen für Quelle und Medium.** Neue Werte kommen nur nach Absprache dazu. Für das Medium nimmst du die Werte, die Google Analytics kennt.
3. **Ein Muster für Kampagnen.** Zum Beispiel Jahr und Monat, ein Unterstrich, dann das Thema: `2026-11_winter-sale`. So sortieren sich Kampagnen im Bericht von selbst nach Zeit.
4. **Ein Muster für Inhalte.** Element und Position: `button-oben`, `textlink-unten`, `bild-header`.
5. **Eine gemeinsame Tabelle.** Jeder Link wird in einer Tabelle erzeugt und dort eingetragen. So siehst du auch nach einem Jahr noch, welcher Link wo im Einsatz war.

Für den fünften Punkt kannst du dir meine [UTM-Vorlage als Excel-Datei](/wp-content/uploads/2026/11/utm-vorlage.xlsx) herunterladen. Sie enthält die Listen für Quelle und Medium als Auswahlfelder und baut den fertigen Link automatisch zusammen, inklusive Kleinschreibung und Bindestrichen statt Leerzeichen. Die Datei funktioniert in Excel und lässt sich in Google Sheets importieren. Wer lieber online arbeitet, findet bei Google den kostenlosen Campaign URL Builder, der allerdings keine Liste deiner bisherigen Links führt.

Die Konvention gehört schriftlich festgehalten und an einer Stelle abgelegt, die alle finden. Am besten wird sie Teil des Ablaufs, mit dem ihr Kampagnen plant, so wie ich es im Artikel zu [Digital Analytics](/digital-analytics-kpis-tools-praxis/) beschreibe.

## Was ich davon halte

UTM-Parameter sind das unspektakulärste Werkzeug im Marketing und eines der wichtigsten. Ohne sie ist jede Diskussion über den Erfolg von Kanälen Bauchgefühl. Mit ihnen lässt sich zumindest sauber zählen, welcher Link wie viele Besuche und Abschlüsse gebracht hat.

Man sollte sie aber nicht überschätzen. Erstens messen sie nur Klicks. Wer eine Anzeige sieht und zwei Tage später den Namen deiner Marke googelt, taucht bei der Anzeige nicht auf. Zweitens fehlen in Deutschland viele Besuche ganz in den Daten, weil Menschen der Messung im Cookie-Banner nicht zustimmen. Die Zahlen zeigen also Verhältnisse, keine vollständige Wirklichkeit. Wie man den Beitrag einzelner Kanäle trotzdem einschätzt, beschreibe ich im Artikel zur [Attribution](/attribution-so-kannst-du-den-erfolg-deiner-marketing-kampagnen-messen/).

Mein Rat: Fang klein an. Fünf Quellen, vier Medien, ein Muster für Kampagnen und eine gemeinsame Tabelle reichen für die meisten Teams. `utm_term` brauchst du nur, wenn du bezahlte Suche ohne automatische Kennzeichnung betreibst. Und erkläre die Konvention jedem, der Links baut, auch der Agentur und der Kollegin, die nur ab und zu einen Social-Media-Post absetzt. Ein einziger Link mit eigener Schreibweise reicht, um einen Bericht unbrauchbar zu machen.

Weitere Artikel zum Thema findest du im Handbuch-Kapitel [Growth Marketing](/thema/growth/).

*Bild: mrwashingt0n, Pixabay*

*Quellen: [Google Analytics Hilfe: Kampagnendaten mit benutzerdefinierten URLs erfassen](https://support.google.com/analytics/answer/10917952), [Google Analytics Hilfe: Standard-Channelgruppen](https://support.google.com/analytics/answer/9756891), [Google Analytics Hilfe: Keine personenbezogenen Daten senden](https://support.google.com/analytics/answer/6366371), [Google: Campaign URL Builder](https://ga-dev-tools.web.app/ga4/campaign-url-builder/), [Analytics Mania: UTM Parameters in Google Analytics 4](https://www.analyticsmania.com/post/utm-parameters-in-google-analytics-4/), [Matomo: Campaign Tracking](https://matomo.org/faq/faq_119/), [Wikipedia: UTM parameters](https://en.wikipedia.org/wiki/UTM_parameters), [TAGGRS: Safari Link Tracking Protection](https://taggrs.io/safari-27-tracking-protection/)*
