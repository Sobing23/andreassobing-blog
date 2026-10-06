---
title: "Teslers Gesetz: Komplexität im UX-Design"
slug: "teslers-gesetz-komplexitaet-im-ux-design"
date: 2025-12-03T11:39:53
description: "Teslers Gesetz einfach erklärt: So verschiebst du Komplexität weg vom Nutzer. Mit Formel, Beispielen, KPIs und Checklisten."
image: "/wp-content/uploads/2025/12/laptop-3214756_640.png"
category: "marketing"
vgwort: "https://vg06.met.vgwort.de/na/08c8ddc122d248b8857086c255d30959"
wpId: 6971
---

Teslers Gesetz einfach erklärt: So verschiebst du Komplexität weg vom Nutzer. Mit Formel, Beispielen, KPIs und Checklisten für UX, Marketing und Produkt.

Du willst Produkte bauen, die sich leicht anfühlen? Dann hilft dir **Teslers Gesetz**. Es zeigt dir, wie du unvermeidbare Komplexität vom Nutzer in die Technik verschiebst. So steigt die Nutzbarkeit. So sinkt der Bedienaufwand. Das Prinzip ist zeitlos und passt zu UX, Marketing und Produktmanagement.

## Teslers Gesetz: Definition in einem Satz

**Teslers Gesetz** (Law of Conservation of Complexity) sagt: **Jedes System besitzt eine irreduzible Komplexität.** Du kannst sie nicht entfernen, nur **verlagern** – entweder trägt sie der **Nutzer** oder das **System/Team**. Ziel guter UX: Mehr Komplexität intern auffangen, weniger beim Nutzer abladen.

## Ursprung: Wer steckt hinter dem Gesetz?

Das Gesetz geht auf **Larry Tesler** zurück. Tesler prägte Modellosigkeit, Copy & Paste und nutzerfreundliche Interaktionen bei **Xerox PARC** und **Apple**. Seine Arbeit zeigt: Gute Produkte verbergen technische Last, statt sie dem Nutzer umzuhängen.

## Warum Teslers Gesetz heute wichtiger ist denn je

- **Mehr Features** erzeugen zwangsläufig mehr **Komplexität**.
- **Kognitive Last** (Cognitive Load) entscheidet, ob Nutzer dranbleiben.
- **Marketing-Conversion** leidet, wenn Reibungspunkte häufen.
- **B2B-Workflows** haben harte Randbedingungen, aber wenig Zeit.
- **Automatisierung** kann Lasten in die Maschine verlagern – das fühlt sich simpel an.

NN/g erinnert daran: **Komplexität aktiv verschieben**, um die UX zu vereinfachen. Genau hier setzt Teslers Gesetz an.

## Leitfragen: Wo liegt die Komplexität heute?

1. **Wer rechnet, wer entscheidet?** Nutzer oder System?
2. **Wo entstehen Fehler?** Bei Eingaben, Regeln, Berechnungen?
3. **Welche Ausnahmen lähmen?** Edge Cases, Sonderpreise, Genehmigungen?
4. **Wie sichtbar ist Relevantes?** Signal-zu-Rauschen im Interface?
5. **Wen belasten wir?** Neulinge, Power-User oder Support?

## Praxisbeispiele: Teslers Gesetz in typischen Szenarien

### Checkout im E-Commerce

- **Schlecht:** Viele Felder, keine Auto-Vervollständigung, kryptische Fehler.
- **Besser:** Adresse per Lookup, Klartext-Validierung, Zahlungspräferenzen merken.
- **Verlagerung:** Entwickler bauen Validierung und Adress-API → Nutzer tippt weniger.

### B2B-Dashboard

- **Schlecht:** 20 Filter, 8 Diagramme, unklare Achsen.
- **Besser:** Vordefinierte Sichten nach Rolle, progressive Filter, klare Defaults.
- **Verlagerung:** Data-Team kuratiert KPIs → Nutzer sieht nur Wesentliches.

### Lead-Formular im Marketing

- **Schlecht:** 12 Pflichtfelder, harte Abbrüche bei Fehlern.
- **Besser:** 4 Felder, Stufenformular, weiche Validierung, Auto-Enrichment.
- **Verlagerung:** Ops reichert Firmendaten per API an → Nutzer spart Zeit.

### Enterprise-Onboarding

- **Schlecht:** 40-seitiges PDF, manuelle Rechtevergabe.
- **Besser:** Geführter Setup-Wizard, Rollen-Templates, Sandbox-Demo.
- **Verlagerung:** Produktlogik kapselt Rollenmodelle → Nutzer klickt durch.

## Designprinzipien: Wie du Komplexität verschiebst

### 1) Informationsarchitektur zuerst

- Inhalte in **klare Domänen** schneiden.
- **Primärtasks** an die Spitze, **Sekundärtasks** nach hinten.
- Navigation mit **wenigen, sprechenden Labels**.

### 2) Progressive Disclosure

- Seltenes erst auf **Klick** zeigen.
- Defaults sind **vernünftige Voreinstellungen**.
- Expertenpfade bleiben vorhanden, aber **nicht dominant**.

### 3) Automatisierung & Regeln

- **Auto-Vervollständigung**, **Vorschläge**, **Validierung**.
- **Ableitungen** statt manuelle Eingaben (z. B. MwSt., Währungsformat).
- **Policy-Checks** im Hintergrund, statt Pop-up-Flut.

### 4) Verständliche Rückmeldungen

- Fehler in Alltagssprache.
- **Ursache + Lösung** im selben Satz.
- **Inline-Hinweise** statt abstrakter Codes.

### 5) Signal-zu-Rauschen erhöhen

- Irrelevantes weglassen oder **deutlicher abgrenzen**.
- Texte kürzen, **Typografie ordnen**, **Weißraum** nutzen.
- **Ein primärer CTA** pro Sicht.

## Entscheidungs-Trade-offs: Wann „mehr Technik“ sinnvoll ist

- **Skalierung:** Hohe Nutzerzahlen rechtfertigen höheren **Systemaufwand**.
- **Risiko:** Kritische Domänen (Finanzen, Medizin) brauchen **regelbasierte Checks**.
- **Lernkurve:** Für seltene Tasks lohnt **Guidance** statt „power user shortcuts“.
- **Variabilität:** Viele Sonderfälle → **Konfiguratoren** statt fixe Formulare.
- **Total Cost of Ownership:** Mehr Code ist ok, wenn **Supportkosten** sinken.

## Schritt-für-Schritt: Teslers Gesetz in deinem Projekt

1. **Ist-Last erfassen**  
   Zähle Felder, Klicks, Fehlermuster, Abbrüche.
2. **Hotspots finden**  
   Suche Stellen mit hoher **Interaktionslast**.
3. **Verlagerungsideen sammeln**  
   Welche Regeln kann das System übernehmen?
4. **Hypothesen formulieren**  
   „Wenn Auto-Lookup, dann −20 % Tippzeit.“
5. **A/B-Testen**  
   Variante mit **weniger Nutzerlast** gegen Kontrolle.
6. **Operativ absichern**  
   Dokumentiere Regeln, Monitore, Fallbacks.
7. **Iterieren**  
   Edge Cases einsammeln, Regeln erweitern.

## Häufige Fehler: So fällt man bei Teslers Gesetz um

- **„Einfach“ gleich „weniger Funktionen“** missverstehen.
- **Alles** im Frontend lösen wollen, statt Regeln zu kapseln.
- **Fehlende Defaults**, die Jede\*r neu einstellen muss.
- **Unklare Labels**, die Auswahlstress erhöhen.
- **Dark Patterns**, die kurz wirken, aber langfristig schaden.

## FAQ zu Teslers Gesetz

Gilt das nur für Software?  
Nein. Auch Verträge, Services und interne Prozesse profitieren.

Muss das Team immer mehr bauen?  
Oft ja. Doch Schulung und Support werden kleiner.

Woran erkenne ich gute Verlagerung?  
Task-Zeit und Fehlerrate fallen. Der Nutzen bleibt gleich oder steigt.

Wie bleibe ich flexibel?  
Arbeite mit modularen Regeln, Feature-Flags und klarer Governance.

## Mini-Case: Von 12 auf 5 Felder

Ausgangslage: 12 Pflichtfelder, 8 Prozent Conversion, 2 Minuten Task-Zeit.  
Maßnahme: Stufenformular, Auto-Vervollständigung, Daten-Enrichment.  
Ergebnis: 12 Prozent Conversion, 1 Minute 10 Sekunden Task-Zeit, 18 Prozent weniger Supporttickets.  
Interpretation: Nutzerlast sinkt. Systemlast steigt. Gesamtwert klar positiv.

## Checkliste: 10-Minuten-Review

- Ist der Primärtask glasklar?
- Gibt es sinnvolle Defaults?
- Fängt das System Fehler früh und verständlich ab?
- Sind seltene Optionen versteckt, aber auffindbar?
- Ist ein einziger, klarer CTA gesetzt?

## Fazit: Teslers Gesetz bewusst nutzen

Die beste UX fühlt sich leicht an, weil dein Team Lasten intern trägt. Teslers Gesetz erinnert dich daran: Du entfernst Komplexität selten, du verlagert sie. Plane Regeln, setze Defaults, automatisiere klug, miss die Wirkung und iteriere. So nutzt du Teslers Gesetz für Produkte, die Menschen gern verwenden und die sich für das Business rechnen.

## Tabelle: Kurz-Zusammenfassung

| Bereich | Kernaussage | Haupthebel | KPI |
| --- | --- | --- | --- |
| Definition | Komplexität ist irreduzibel, aber verlagert | Last vom Nutzer ins System | Task-Zeit, Fehlerrate |
| Analyse | Last als Bilanz denken | Hotspots finden | Interaktionslast |
| Design | Zeige nur Relevantes | IA, Defaults, Progressive Disclosure | Conversion |
| Technik | Maschine rechnet, Nutzer klickt weniger | Validierung, Enrichment, Automatisierung | Supporttickets |
| Business | Weniger Reibung, mehr Umsatz | Kürzere Flows, klare CTAs | Umsatz pro Besucher |

 
Sieh dir auch diesne Beitrag von mir an: [Wie man OKRs erfolgreich in 4 effektiven Schritten implementiert](/wie-man-okrs-erfolgreich-in-4-effektiven-schritten-implementiert/)
Inspiriert hat mich folgender Artikel: [Tesler’s Law: Shift Complexity to Simplify UX](https://www.nngroup.com/videos/teslers-law/)
