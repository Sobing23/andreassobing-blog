---
title: "Chat, Automatisierung, Agenten: Die drei Stufen der KI im Unternehmen"
seoTitle: "KI im Unternehmen: Drei Stufen von Chat bis KI-Agent und Reverse Prompting erklärt"
slug: "ki-im-unternehmen-chat-automatisierung-agenten"
date: 2026-10-13T14:00:00
description: "Dan Martell teilt den KI-Einsatz im Unternehmen in drei Stufen: Chat, Automatisierung und Agenten. Was hinter dem Modell steckt, wie Reverse Prompting funktioniert und wo die Versprechen zu groß sind."
image: "/wp-content/uploads/2026/10/ki-drei-stufen-titelbild.jpg"
category: "ki-tools"
vgwort: "https://vg09.met.vgwort.de/na/280e5b18e8ba4ec5a80f37f9eb20471f"
tags:
  - "KI"
  - "Prompts"
  - "KI-Agenten"
  - "Automatisierung"
---

Viele Unternehmen nutzen KI heute so: Jemand öffnet ein Chatfenster, kopiert einen Prompt aus einem Video hinein, prüft das Ergebnis und kopiert es weiter. Das spart ein paar Minuten, verändert aber wenig. Der kanadische Unternehmer und Coach Dan Martell sagt dazu in seinem „AI Business Cheat Sheet“: Das Problem ist nicht das Werkzeug, sondern die Strategie.

Sein Cheat Sheet teilt den Einsatz von KI in drei Stufen ein und stellt eine Prompt-Technik vor, die er Reverse Prompting nennt. Ich stelle beides hier vor und ordne es ein. Denn das Dokument ist auch Werbung für Martells Coaching und seine eigene Agenten-Software. Das merkt man an einigen Versprechen.

## Die drei Stufen der KI

Martell vergleicht die drei Stufen mit Fortbewegungsmitteln. Das Bild ist einfach, aber es trifft den Unterschied gut: Wie viel musst du selbst tun, und wie viel übernimmt die Technik?

![Die drei Stufen der KI im Unternehmen nach Dan Martell: Stufe 1 Chat wie ein Skateboard, Stufe 2 Automatisierung wie ein E-Scooter, Stufe 3 Agenten wie ein persönlicher Fahrer. Je höher die Stufe, desto mehr übernimmt die KI.](/wp-content/uploads/2026/10/ki-drei-stufen-modell.jpg)

| Stufe | Prinzip | Bild | Wofür | Beispiele für Werkzeuge |
| --- | --- | --- | --- | --- |
| 1. Chat | Unterstützung im Dialog | Skateboard: Du schiebst selbst an, die KI macht dich schneller | Ideen, Entwürfe, Recherche, Strategie | Claude, Gemini, Grok |
| 2. Automatisierung | Verbundene Abläufe | E-Scooter: Du legst die Strecke fest, ein Motor fährt | Wiederkehrende Aufgaben ohne menschliches Zutun | Zapier, Make, n8n |
| 3. Agenten | Selbstständige Ausführung | Persönlicher Fahrer: Du nennst das Ziel, die KI plant und fährt | Komplexe Aufgaben mit mehreren Schritten | Claude Cowork, Manus |

Martells These: Die meisten Unternehmer bleiben auf Stufe 1 stehen. Wer wachsen will, ohne im gleichen Maß Personal aufzubauen, muss alle drei Stufen beherrschen.

## Stufe 1: Chat und Reverse Prompting

Auf der ersten Stufe ist die KI ein Sparringspartner. Du fragst, sie antwortet, du arbeitest mit dem Ergebnis weiter. Die Qualität hängt fast vollständig davon ab, wie viel Kontext die KI hat.

### Push statt Pull

Martell unterscheidet zwei Arten zu prompten. Beim **Push Prompting** gibst du eine fertige Anweisung vor: „Schreib mir eine E-Mail zu unseren Zielen für das zweite Quartal. Motivierend, höchstens 200 Wörter.“ Die KI muss raten, was du meinst. Das Ergebnis ist allgemein und klingt nicht nach dir.

Beim **Reverse Prompting**, Martell spricht auch von Pull Prompting, drehst du die Richtung um. Du nennst nur das Ziel und lässt dich von der KI befragen:

> Ich brauche deine Hilfe bei [Aufgabe]. Bevor du mir hilfst, stell mir drei bis vier Fragen, damit du allen Kontext hast, den du für das beste Ergebnis brauchst. Stell immer nur eine Frage und warte auf meine Antwort, bevor du die nächste stellst.

![Push Prompting im Vergleich zu Reverse Prompting: Beim Push Prompting rät die KI, was du willst. Beim Reverse Prompting stellt sie erst Fragen und holt sich den Kontext.](/wp-content/uploads/2026/10/ki-reverse-prompting.jpg)

Der Gedanke dahinter ist richtig. Die meisten schwachen Ergebnisse entstehen nicht durch schlechte Formulierungen, sondern durch fehlenden Kontext. Wenn die KI fragt, merkst du oft selbst erst, was du eigentlich willst. Martell verspricht allerdings „Zero editing“, also gar keine Nacharbeit. Das halte ich für übertrieben. Weniger Nacharbeit ja, keine Nacharbeit nein.

Wie Prompts grundsätzlich aufgebaut sein sollten, beschreibe ich in den Artikeln [Strategie Prompt Engineering für Marketer](/strategie-prompt-engineering-fuer-marketer/) und [Die KADE-Formel](/die-kade-formel-ein-innovativer-ansatz-zur-maximierung-der-chatgpt-leistung/).

### Die MAPS-Formel

Für Aufgaben, bei denen du schon genau weißt, was du brauchst, nennt Martell eine einfache Struktur. Sie heißt MAPS:

- **Mission:** Was ist dein Ziel? Zum Beispiel zehn Prozent mehr Leads oder ein Produktstart.
- **Ask:** Was soll die KI tun? Etwa eine Überschrift, eine E-Mail-Sequenz oder einen Blogartikel schreiben.
- **Parameters:** Was soll sie beachten? Beispiele, frühere Ergebnisse, eine Website der Konkurrenz, ein bekanntes Modell.
- **Shape:** In welcher Form willst du das Ergebnis? Als Tabelle, Liste, Zusammenfassung oder Tabellendatei.

Als Satz: „Mein Ziel ist [Mission], dafür brauche ich [Ask]. Beachte dabei [Parameters] und gib das Ergebnis als [Shape] aus.“ Das ist nicht neu, aber leicht zu merken.

### Aus guten Ergebnissen eigene Vorlagen machen

Der für mich nützlichste Tipp im Cheat Sheet ist ein kleiner Trick. Wenn du mit der KI so lange an einem Text gearbeitet hast, bis er wirklich passt, gibst du ihr zum Schluss diesen Auftrag:

> Schreib den vollständigen System-Prompt, der von Anfang an genau dieses Ergebnis erzeugt hätte.

Diesen Prompt speicherst du. Du kannst ihn im Team teilen oder als Grundlage für einen eigenen Assistenten nutzen, wie im Artikel [Wie du deinen eigenen Chatbot mit GPT erstellst](/wie-du-deinen-eigenen-chatbot-mit-gpt-erstellst/). So wird aus einer einmaligen Unterhaltung eine Vorlage, die das Wissen deines Unternehmens festhält. Martell nennt das „Company IP“, also geistiges Eigentum des Unternehmens.

## Stufe 2: Automatisierung

Auf der zweiten Stufe verlässt du das Chatfenster. Werkzeuge wie Zapier, Make oder n8n verbinden deine Programme und lassen Daten automatisch fließen. Neu ist, dass mitten im Ablauf ein KI-Schritt sitzen kann, der nicht nur Daten weiterreicht, sondern Texte schreibt oder Informationen bewertet.

Martells Beispiel ist eine automatische Vorbereitung auf Kundentermine:

1. **Auslöser:** Ein Interessent bucht über Calendly einen Beratungstermin.
2. **Recherche:** Make ruft die Website des Unternehmens ab und sammelt Informationen über das Geschäft.
3. **KI-Schritt:** Die Informationen gehen mit einem festen System-Prompt an Claude. Die KI schreibt eine persönliche E-Mail vor dem Termin, die auf typische Herausforderungen der Branche eingeht.
4. **Versand:** Gmail verschickt die E-Mail.

![Beispiel für einen automatisierten Ablauf mit KI-Schritt: Terminbuchung in Calendly, Recherche der Website mit Make, persönliche E-Mail mit Claude, Versand über Gmail.](/wp-content/uploads/2026/10/ki-automatisierung-beispiel.jpg)

Das Beispiel zeigt gut, was möglich ist. Einen Punkt würde ich allerdings anders machen: Die E-Mail geht ohne Prüfung an einen potenziellen Kunden. Gerade bei den ersten Kontakten würde ich einen Freigabeschritt einbauen, bis klar ist, dass die Texte zuverlässig passen. Erste einfache Schritte in die Automatisierung zeige ich in den [vier Quick Wins für die Marketing Automation](/vier-quick-wins-fuer-die-marketing-automation/).

Martell schreibt, dass die zweite Stufe bereits an Bedeutung verliere. Sie sei zu technisch und funktioniere nur bei klar definierten Abläufen. Da widerspreche ich. Genau diese Eigenschaft ist ihre Stärke. Ein fester Ablauf macht jedes Mal dasselbe, ist nachvollziehbar und lässt sich prüfen. Für Rechnungen, Anmeldungen oder Datenübertragungen will ich keine KI, die jedes Mal neu überlegt.

## Stufe 3: KI-Agenten

Auf der dritten Stufe gibst du nur noch das Ziel vor. Ein KI-Agent plant die Schritte selbst, nutzt dafür Programme, durchsucht das Web, legt Dateien an und prüft seine Ergebnisse. Martell beschreibt das als Kreislauf aus Denken, Handeln und Beobachten. Während eine Automatisierung einem festen Pfad folgt, also „wenn X passiert, tue Y“, kann ein Agent mit offenen Aufgaben umgehen.

Sein Beispiel ist eine Kalenderprüfung: Der Agent soll die Termine der letzten 30 Tage durchgehen, wiederkehrende Meetings finden, die sich zusammenlegen lassen, und einen neuen Wochenplan vorschlagen, der fünf Stunden Arbeitszeit freimacht. Der Agent liest den Kalender, wertet ihn aus und liefert einen Bericht mit Vorschlägen. Passend dazu: [Zeitfresser Meeting und neun Gegenmaßnahmen](/zeitfresser-meeting-und-9-gegenmassnahmen/).

Die einzige Voraussetzung sei Zugriff, schreibt Martell: auf Google Drive, Notion, Slack, Kalender und E-Mail. Genau hier würde ich bremsen. Zugriff ist keine Kleinigkeit, sondern die eigentliche Entscheidung. Ein Agent mit Zugriff auf alle Postfächer und Dokumente kann auch Fehler in allen Postfächern und Dokumenten machen. Dazu kommen Datenschutz und Vertraulichkeit, gerade wenn Kundendaten betroffen sind. Grundsätzliches dazu steht im Artikel [Sicherheit bei der Nutzung von ChatGPT](/sicherheit-bei-der-nutzung-von-chatgpt-was-du-wissen-solltest/).

Am Ende des Kapitels geht Martell noch einen Schritt weiter. Er beschreibt einen „Digital Twin“, einen Agenten, der rund um die Uhr läuft und Aufgaben wie E-Mail-Sortierung, Kennzahlen und Nachfassen übernimmt, so wie du es tun würdest. Für genau diesen Zweck bewirbt er seine eigene Plattform. Die Idee ist spannend, aber hier wird das Cheat Sheet zur Produktwerbung.

## Prompts für die Gründung

Im Anhang enthält das Cheat Sheet 16 Prompt-Vorlagen für die Gründung eines Unternehmens. Sie decken acht Bereiche ab und folgen alle demselben Muster: Ziel nennen, dann fünf bis sieben Fragen stellen lassen, eine nach der anderen.

1. Geschäftsidee und Nutzenversprechen
2. Markt- und Wettbewerbsanalyse
3. Businessplan und Strategie
4. Rechtliche und organisatorische Grundlagen
5. Finanzplanung und Finanzierung
6. Marketing und Vertrieb
7. Unternehmenskultur und Team
8. Laufende Optimierung und Wachstum

Ein Beispiel auf Deutsch, angelehnt an die Vorlage zur Wettbewerbsanalyse:

> Ich möchte meine wichtigsten Wettbewerber finden und ihre Stärken, Schwächen und Nutzenversprechen vergleichen, damit ich mich abgrenzen kann. Bevor du das tust, stell mir fünf bis sieben Fragen zu meinem Produkt, meiner Preisstrategie und den Wettbewerbern, die ich schon kenne. Stell immer nur eine Frage.

Die Vorlagen sind ein guter Startpunkt, ersetzen aber keine Fachkenntnis. Die KI liefert dir eine Struktur und gute Fragen. Ob ein Marktvolumen stimmt oder eine Rechtsform zu dir passt, musst du prüfen oder prüfen lassen. Wie leicht KI bei Recherchen danebenliegt, zeige ich im Artikel zur [STORM-Methode](/storm-methode-ki-recherche/). Für die inhaltliche Arbeit helfen klassische Werkzeuge wie die [Wettbewerbsanalyse](/wettbewerbsanalyse-strategien-methoden-und-beispiele/), das [Value Proposition Canvas](/mit-dem-value-proposition-canvas-besser-kunden-gewinnen/) und die Prinzipien aus [Lean Startup](/lean-startup-die-wichtigsten-prinzipien-aus-dem-buch-von-eric-ries/).

## Was ich vom Cheat Sheet halte

Das Drei-Stufen-Modell ist eine gute Orientierung. Es hilft, ehrlich zu prüfen, wo ein Team steht, und zeigt, dass Chat allein nicht die ganze Geschichte ist. Reverse Prompting und der Trick mit dem System-Prompt sind einfache Werkzeuge, die sofort helfen.

Kritisch sehe ich drei Punkte:

**Die 92-Prozent-Regel ist eine Behauptung.** Martell verspricht, dass KI bei richtiger Einrichtung 92 Prozent der Ausführung übernimmt und du nur noch für die letzten 8 Prozent gebraucht wirst. Eine Quelle oder Messung dafür nennt er nicht. Ich würde die Zahl als Bild verstehen, nicht als Planungsgröße.

**Die Stufen lösen sich nicht ab, sie ergänzen sich.** Chat, feste Abläufe und Agenten haben jeweils eigene Stärken. Für wiederkehrende, prüfbare Prozesse ist eine feste Automatisierung oft die bessere Wahl als ein Agent.

**Kontrolle ist wichtiger als Zugriff.** Je mehr die KI selbstständig erledigt, desto wichtiger sind klare Grenzen: Was darf sie ohne Freigabe tun, was nicht, und wer prüft die Ergebnisse?

Mein Vorschlag für den Einstieg: Nimm eine Aufgabe, die du jede Woche erledigst. Probier Reverse Prompting aus, bis das Ergebnis stimmt. Lass dir dann den System-Prompt schreiben und speichere ihn. Erst wenn das zuverlässig klappt, lohnt sich der nächste Schritt zur Automatisierung oder zum Agenten.

Weitere Artikel zu Prompts, GPTs und KI im Marketing findest du im Handbuch-Kapitel [KI im Marketing](/thema/ki/).

*Quelle: [Dan Martell: The AI Business Cheat Sheet. How to Buy Back Your Time and Make AI Do 92% of the Work (PDF, danmartell.com)](https://www.danmartell.com/)*
