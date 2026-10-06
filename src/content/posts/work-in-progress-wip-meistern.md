---
title: "Work-in-Progress (WIP) meistern"
slug: "work-in-progress-wip-meistern"
date: 2025-09-23T10:51:22
description: "Work-in-Progress (WIP) richtig begrenzen: Mit WIP-Limits, Little’s Law, klaren Regeln und Kanban reduzierst du Durchlaufzeiten."
image: "/wp-content/uploads/2025/09/c76673c0-f156-4432-9f42-d1b0f16a53a31.png"
category: "arbeitsweisen"
vgwort: "https://vg06.met.vgwort.de/na/e2cd1c5b710043f7b80af5430bd11d3c"
wpId: 6904
---

Work-in-Progress (WIP) richtig begrenzen: Mit WIP-Limits, Little’s Law, klaren Regeln und [Kanban](/kanban-optimiert-deinen-arbeitsfluss/) reduzierst du Durchlaufzeiten und steigerst den Durchsatz.

## Einleitung: Warum Work-in-Progress (WIP) dein Tempo bestimmt

Work-in-Progress (WIP) zeigt, wie viele Aufgaben gleichzeitig in Arbeit sind. Zu viel WIP bremst Teams aus. Du wartest länger, wechselst öfter den Kontext und verlierst Fokus. Wenn du WIP gezielt steuerst, sinkt die Durchlaufzeit, der Fluss wird ruhiger und Ergebnisse kommen verlässlich.

## Ursprung: Von Toyota bis zur Wissensarbeit

WIP stammt aus dem Lean-Ansatz des Toyota Production System. Pionier war Taiichi Ohno. Ziel war weniger Verschwendung und mehr Fluss. In der Wissensarbeit machte David J. Anderson WIP-Limits durch Kanban populär. Den mathematischen Rücken liefert John D. C. Little mit Little’s Law (1961). Die Idee ist zeitlos: Begrenze parallele Arbeit, damit Arbeit schneller fertig wird.

## Definition: Was genau ist WIP?

WIP ist die Menge an Aufgaben, die gerade aktiv bearbeitet werden. Sie liegt zwischen „angestoßen“ und „fertig“. Alles, was du begonnen hast, zählt. Backlog zählt nicht. „Done“ zählt nicht. Nur „in Arbeit“ zählt. Genau hier setzt Steuerung an.

## Little’s Law: Die Formel hinter WIP

Little’s Law verknüpft Bestand, Durchsatz und Zeit. Es gilt stabil über viele Prozesse hinweg.

- **Formel:** L = λ × W  
  L = durchschnittlicher Bestand (hier: **WIP**)  
  λ = **Durchsatz** (Items pro Zeit)  
  W = **Durchlaufzeit** bzw. **Cycle Time**

Daraus folgen praktische Umformungen:

- **WIP = Durchsatz × Cycle Time**
- **Cycle Time = WIP ÷ Durchsatz**
- **Durchsatz = WIP ÷ Cycle Time**

Beispiel: Dein Team liefert 20 Tasks pro Woche. Die gewünschte Cycle Time liegt bei 2 Tagen (≈ 0,4 Wochen). Empfohlenes WIP: 20 × 0,4 = **8** parallele Tasks. Mehr WIP macht dich langsamer, nicht schneller.

## Kennzahlen: Lead Time, Cycle Time, Durchsatz

- **Durchsatz (Throughput):** Fertiggestellte Items pro Zeitraum.
- **Cycle Time:** Start bis „Done“ für ein Item.
- **Lead Time:** Kundenwartezeit von Anfrage bis Lieferung.
- **WIP:** Anzahl aktiver Items im System.

Ziel ist ein stabiler Fluss: moderates WIP, verlässlicher Durchsatz, kurze Cycle Time.

## WIP-Limits setzen: Schritt-für-Schritt-Vorgehen

1. **Prozess sichtbar machen**  
   Zeichne dein Kanban-Board: To Do → In Progress → Review → Done. Spalte „In Progress“ bei Bedarf feiner (z. B. „Entwurf“, „Implementierung“, „Test“).
2. **Basisdaten sammeln**  
   Miss für zwei Wochen Durchsatz und Cycle Time. So vermeidest du Blindflug.
3. **Start-Limits berechnen**  
   Nutze Little’s Law rückwärts: **WIP-Limit je Spalte ≈ Durchsatz × Ziel-Cycle-Time-Anteil**. Beginne konservativ. Beispiel: Gesamt-WIP 8 → „Entwurf“ 3, „Implementierung“ 3, „Review“ 2.
4. **Swarming einführen**  
   Wenn eine Spalte voll ist, startet niemand Neues. Alle helfen, Engpässe zu leeren. Das senkt Wartezeiten.
5. **Wöchentlich justieren**  
   Evaluiere Blocker, Wartezeiten und Engpässe. Erhöhe Limits nie reflexhaft. Senke WIP schrittweise, bis der Fluss stabil wirkt.

## Praxisfragen: Wie streng müssen WIP-Limits sein?

WIP-Limits sind Leitplanken. Sie wirken nur, wenn du sie ernst nimmst. Notfälle gibt es, aber sie bleiben selten. Klare Regeln helfen:

- Kein neues Item, wenn deine Spalte am Limit ist.
- Blockierte Tickets werden markiert und priorisiert gelöst.
- Pairing oder Mobbing (Swarming) statt Solo-Hopping.
- Meetings kurz halten, Entscheidungen zügig treffen.
- Review-Termine regelmäßig, damit nichts stecken bleibt.

## Anti-Pattern: WIP frisst Produktivität

Diese Muster verlängern Lead Times, obwohl sie „busy“ aussehen:

- **Multitasking:** Häufige Kontextwechsel erhöhen Fehler und Verzögerung.
- **Unscharfe Definition of Done:** Aufgaben „fertig, aber…“ hängen fest.
- **Zu breite Spalten:** Alles landet in „In Progress“ und versumpft.
- **Verdeckte Blocker:** Externe Abhängigkeiten ohne Fristen.
- **Fehlende Priorität:** Zu viele „Top-Prioritäten“ gleichzeitig.

## Beispiel Marketing-Team: WIP senken, Output erhöhen

Ausgangslage: 15 parallele Tasks, Durchsatz 12/Woche, Cycle Time 6 Tage.  
Maßnahme: Gesamt-WIP-Limit 8, Review-Slot täglich, Swarming auf Blocker.  
Ergebnis nach 3 Wochen: Durchsatz stabil 14/Woche, Cycle Time 3–4 Tage, weniger Nacharbeit. Mini-Formel wirkt: **Cycle Time = WIP ÷ Durchsatz**.

## Resourcing: Wie groß darf WIP pro Person sein?

Als Faustregel gilt: **1–2 aktive Items pro Person**. Mehr erhöht Kontextwechsel. Ergänze Rollenfokus:

- Creator: maximal 2 kreative Arbeiten parallel.
- Analyst: 1 tiefes Analyse-Item plus 1 schnelles Reporting.
- Manager: 1 Projekt + 1 eskalierbarer Ad-hoc-Block.

## WIP in BWL/Accounting vs. Kanban: Begriffe sauber trennen

In der Kostenrechnung bedeutet Work-in-Process das **Bestandskonto unfertiger Erzeugnisse**. In Kanban ist WIP die **Anzahl aktiver Arbeiten**.

- **Accounting-WIP (Vereinfachung):**  
  WIP-Bestand = Material + Direktlohn + Gemeinkosten an unfertigen Aufträgen − Kosten fertiggestellter Einheiten.
- **Kanban-WIP:**  
  Zählgröße der parallel bearbeiteten Tickets. Ziel ist Begrenzung, nicht Bilanzierung.

Beide teilen das Prinzip „Bestand bindet Zeit und Kapital“. In der Bilanz bindet WIP Geld, im Flow bindet WIP Zeit.

## Kapazität planen: So rechnest du WIP vorausschauend

- **Kapazität (Tickets/Woche) ≈ verfügbare Teamtage ÷ durchschnittliche Ticket-Tage**
- **Empfohlenes Gesamt-WIP ≈ 1–1,5 × Teamgröße** (Startwert)
- **Puffer** für Ungeplantes: 10–15 % des WIP als „Fast Lane“

Beispiel: 6 Personen, Ticket-Durchschnitt 2 Tage, 5 Arbeitstage/Woche → Kapazität ≈ (6×5) ÷ 2 = **15 Tickets/Woche**. Starte mit Gesamt-WIP **6–9**.

## WIP sichtbar machen: Board-Design und Policies

- Spalten klar benennen und begrenzen.
- WIP-Limit als Zahl an der Spalte führen.
- Swimlanes für Eilfälle streng begrenzen.
- Blocker-Tag mit Datum, damit Wartezeit messbar wird.
- Serviceklassen definieren (Standard, Eilig, Fixtermin).

## Messroutine: Welche Metriken du jede Woche checkst

- **Durchsatz (Woche):** Wie viele Tickets fertig?
- **Cycle Time (Median):** Wie lange pro Ticket?
- **WIP-Bestand (täglich):** Bleibt das Limit stabil?
- **Blocker-Zeit:** Anteil „wartend“ vs. „aktiv“.
- **Flow Efficiency:** Aktivzeit ÷ Gesamtdurchlaufzeit.

Ziel: WIP flach halten, Blockerzeit senken, Median-Cycle-Time stabilisieren.

## Change-Management: Wie du WIP-Limits ins Team bringst

- Erkläre **warum**: Kürzere Wartezeiten, weniger Stress, mehr Qualität.
- Starte als **Experiment**: Vier Wochen Test, dann Review.
- Teile Erfolge sichtbar: Diagramm für Cycle-Time-Verlauf.
- Belohne Fokus: Fertigstellen schlägt Starten.
- Halte Führung im Boot: Keine Eskalation über Limits ohne Trade-offs.

## FAQ: Kurze Antworten auf typische Einwände

**„Mehr WIP heißt doch mehr Output?“**  
Nein. Ab einem Punkt steigt Wartezeit stärker als der Nutzen der Parallelität.  
**„Wir haben viele Abhängigkeiten.“**  
Umso wichtiger sind kleine WIP-Batches und klare Blocker-Policies.  
**„Unsere Aufgaben sind groß.“**  
Schneide Tickets dünner. Kleine Lose fließen schneller.  
**„Kunden wollen sofort Start.“**  
Transparenz hilft: Sag realistische Starttermine statt alles gleichzeitig beginnen.

## Fazit: Mit Work-in-Progress (WIP) zu ruhigem Fluss

Wenn du Work-in-Progress (WIP) begrenzt, verkürzt du die Cycle Time, stabilisierst den Durchsatz und reduzierst Stress. Starte mit einem einfachen Limit, swarme bei Engpässen und messe wöchentlich. So entsteht verlässlicher Fluss, und dein Team liefert spürbar schneller.

Sieh dir auch diesne Beitrag von mir an: [Was ist First Principle Thinking und wie nutzt du es?](/was-ist-first-principle-thinking-und-wie-nutzt-du-es/)

## Zusammenfassung (Tabelle

| Bereich | Kernaussage | Formel/Heuristik | Nächster Schritt |
| --- | --- | --- | --- |
| Little’s Law | WIP steuert Zeit | WIP = Durchsatz × Cycle Time | Ziel-Cycle-Time festlegen |
| Limits | Fokus statt Hopping | 1–2 Items pro Person | Spaltenlimits einführen |
| Swarming | Engpässe räumen | Keine neuen Starts bei vollem WIP | Daily-Review der Blocker |
| Metriken | Fluss sichtbar machen | Durchsatz, CT, WIP, Blockerzeit | Wöchentliches Flow-Review |
| Planung | Realistische Kapazität | Kapazität ≈ Teamtage ÷ Ticket-Tage | Fast Lane strikt begrenzen |

## Quellen / weiterführende Links

- Ohno, T.: Toyota Production System – Beyond Large-Scale Production.
- Anderson, D. J.: Kanban – Successful Evolutionary Change for Your Technology Business.
- Little, J. D. C. (1961): A Proof for the Queueing Formula L = λW, Operations Research.
- Reinertsen, D.: The Principles of Product Development Flow.
- Kanban University – Kanban Guide und Policies.
- Lean Enterprise Institute – Grundlagen zu Flow und Verschwendung.
