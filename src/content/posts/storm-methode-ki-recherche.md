---
title: "Die STORM-Methode: Erst recherchieren, dann schreiben lassen"
seoTitle: "STORM-Methode von Stanford: So recherchierst du mit ChatGPT und Claude"
slug: "storm-methode-ki-recherche"
date: 2026-10-06T12:00:00
description: "Warum KI-Texte oft flach bleiben und wie du mit der STORM-Methode der Stanford University in drei Schritten bessere Recherchen mit ChatGPT oder Claude machst."
image: "/wp-content/uploads/2026/10/storm-methode-red-herring.jpg"
category: "ki-tools"
vgwort: "https://vg09.met.vgwort.de/na/e65d2b5cc1934762b57a7af7315cacf3"
tags:
  - "KI"
  - "ChatGPT"
  - "Claude"
  - "Recherche"
  - "Prompting"
---

Eine E-Mail, ein Social-Post, ein Produkttext: Das schreibt dir eine KI heute in Sekunden. Sobald es aber um eine echte Recherche geht, um ein Whitepaper, eine Marktanalyse oder die Hausarbeit im Studium, wird es dünn. Die Texte klingen gut und sagen wenig. Und manchmal stehen Quellen darin, die es gar nicht gibt.

Forscher der Stanford University haben sich genau dieses Problem angeschaut und ein System namens STORM gebaut. Die Idee dahinter kannst du ohne eine Zeile Code in deinen eigenen Arbeitsalltag übernehmen. Ich erkläre sie auch im Video:

<div class="video" data-provider="youtube" data-id="YPG3T4x0FfE"></div>

## Warum KI-Texte so oft flach bleiben

Die meisten Prompts sehen ungefähr so aus: „Schreib mir einen Artikel über X.“ Damit verlangst du von der KI zwei Dinge gleichzeitig. Sie soll das Thema erschließen und im selben Atemzug fertige Sätze formulieren. Heraus kommt eine Sammlung allgemeiner Fakten in gefälligem Ton.

Stell dir vor, du schreibst eine Seminararbeit und tippst den Text in dem Moment, in dem du das erste Fachbuch zum Thema aufschlägst. Das würde niemand ernsthaft so machen. Bei der KI machen wir es ständig.

## Die Grundidee: Recherche und Schreiben trennen

STORM (das steht für „Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking“) teilt die Arbeit in zwei Phasen.

In der ersten Phase, dem Prewriting, entsteht noch kein Fließtext. Das System sucht im Netz nach Quellen, sammelt Informationen und baut daraus eine detaillierte Gliederung. Erst wenn diese Gliederung steht, beginnt Phase zwei und der eigentliche Artikel wird geschrieben, auf Basis dessen, was vorher gefunden wurde.

Das klingt banal. Es ist aber genau der Schritt, den die meisten von uns beim Prompten überspringen.

## Der Trick mit dem simulierten Interview

Spannender wird es bei der Frage, wie die KI in Phase eins überhaupt gute Fragen stellt. Wenn du einer KI sagst „Stell mir Fragen zu Thema X“, bekommst du meistens Fragen, die du dir selbst auch hättest stellen können.

STORM löst das mit einem Rollenspiel. Ein KI-Agent übernimmt die Rolle eines Autors mit einer bestimmten Perspektive, etwa die eines Ökonomen oder einer Juristin. Dieser Agent interviewt einen zweiten Agenten, der seine Antworten aus einer Websuche zieht. Der Fragende hört zu, hakt nach und geht mit jeder Runde tiefer. Weil mehrere solcher Gespräche aus unterschiedlichen Blickwinkeln laufen, tauchen Aspekte auf, die ein einzelner Standard-Prompt nie zutage gefördert hätte.

## Co-STORM: Der Mensch bleibt am Steuer

Ein vollautomatisches System hat immer blinde Flecken. Deshalb hat das Stanford-Team mit Co-STORM eine Erweiterung entwickelt, bei der du selbst mitarbeitest. Mehrere KI-Agenten diskutieren das Thema, ein Moderator-Agent achtet darauf, wo noch Lücken sind, und das gesammelte Wissen wird laufend in einer Art Mindmap sortiert. Du kannst jederzeit eingreifen und die Richtung ändern.

Für mich ist das der interessanteste Teil. Die KI macht die Fleißarbeit, du entscheidest, wohin die Recherche geht.

## Was die Studie zeigt (und was nicht)

Die Forscher haben ihre Ergebnisse von zehn erfahrenen Wikipedia-Autoren bewerten lassen. Verglichen wurde STORM mit einem einfacheren Verfahren, bei dem eine KI zwar auch Suchergebnisse nutzt, aber ohne den Zwischenschritt mit Perspektiven und Gliederung. Im Vergleich wurden 25 Prozentpunkte mehr STORM-Artikel als gut strukturiert bewertet und 10 Prozentpunkte mehr als inhaltlich breit aufgestellt.

Das ist ein ordentliches Ergebnis. Ein Wundermittel ist STORM aber nicht, und das sagen die Forscher selbst. Die Autoren fanden die Texte weniger informativ als echte Wikipedia-Artikel. Sieben von zehn bemängelten, dass die Texte stellenweise einseitig oder wertend klingen, weil die KI den Ton ihrer Internetquellen übernimmt.

Und dann ist da noch der „Red Herring“, auf Deutsch der rote Hering. Gemeint ist ein Fehler, der heimtückischer ist als eine glatt erfundene Quelle: Die KI nimmt zwei Fakten, die beide stimmen, und verknüpft sie zu einer Aussage, die nicht stimmt. Genau dieses Muster haben die Wikipedia-Autoren auch in den STORM-Texten gefunden. Die Methode macht KI-Recherchen besser, prüfen musst du das Ergebnis trotzdem.

Noch ein Detail für alle, die über Kosten nachdenken: Das Open-Source-Projekt erlaubt es, für die vielen Fragerunden ein günstiges Sprachmodell einzusetzen und das teure Modell nur für den finalen Text. Das spart spürbar Geld, wenn du so etwas regelmäßig laufen lässt.

## Drei Schritte für deine Arbeit mit ChatGPT oder Claude

Du brauchst STORM nicht, um von der Idee zu profitieren. Diese drei Schritte kannst du ab sofort in jedem Chat anwenden.

### 1. Erst die Gliederung, dann der Text

Bitte die KI im ersten Schritt nie um einen fertigen Text. Ein Prompt wie dieser funktioniert deutlich besser:

> Recherchiere im Internet nach verlässlichen Quellen zum Thema X. Erstelle mir zuerst nur eine detaillierte Gliederung mit den wichtigsten Fakten und den Quellen dazu. Schreib noch keinen Fließtext.

Erst wenn du mit der Struktur zufrieden bist, gibst du den Auftrag zum Schreiben.

### 2. Lass die KI Rollen einnehmen

Statt nach „Fragen zum Thema“ zu fragen, gibst du der KI eine Perspektive:

> Nimm die Rolle einer kritischen Wissenschaftsjournalistin ein. Welche fünf Fragen müsstest du stellen, um blinde Flecken in diesem Thema aufzudecken?

Noch besser: Lass zwei Experten mit unterschiedlicher Sicht miteinander diskutieren, zum Beispiel eine Performance-Marketerin und einen Markenstrategen. Die Reibung zwischen den beiden bringt meist mehr als jede Einzelantwort.

### 3. Prüf die Gliederung wie ein Redakteur

Bevor geschrieben wird, gehst du die Gliederung selbst durch. Achte besonders auf die roten Heringe: Stimmen die Verbindungen zwischen den Fakten, oder klingen sie nur plausibel? Ergänze eigene Gedanken, streich, was nicht passt, und schick die KI gegebenenfalls noch einmal los. Die Vorarbeit kann die KI übernehmen. Das Denken solltest du behalten.

## Mein Fazit

Die KI wird deine Recherche nicht ersetzen. Sie verschiebt aber deine Rolle: weniger selbst tippen, mehr steuern und prüfen. Gerade im Marketing, wo wir ständig Themen, Zielgruppen und Märkte erschließen müssen, ist das ein großer Hebel. Ob du gerade studierst oder seit Jahren im Job bist, macht dabei kaum einen Unterschied.

Wenn du STORM selbst ausprobieren willst: Stanford bietet unter [storm.genie.stanford.edu](https://storm.genie.stanford.edu/) eine kostenlose Testversion an. Der Code liegt offen auf [GitHub](https://github.com/stanford-oval/storm).

Quellen: [Shao et al. (2024): Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](https://arxiv.org/abs/2402.14207), [Jiang et al. (2024): Into the Unknown Unknowns (Co-STORM)](https://arxiv.org/abs/2408.15232)