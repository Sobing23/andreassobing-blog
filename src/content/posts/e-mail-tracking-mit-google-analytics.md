---
title: "E-Mail Tracking mit Google Analytics"
slug: "e-mail-tracking-mit-google-analytics"
date: 2022-11-14T22:16:41
description: "E-Mail Tracking mit Google Analytics. Neben den bereits vorgestellten Kennzahlen will man auch gerne weiterführende Analysen erhalten."
image: "/wp-content/uploads/2022/11/train-track-g303cfd892_6401.jpg"
category: "email-marketing"
vgwort: "https://vg06.met.vgwort.de/na/9d31b417514e4253a46242f8556f2a8f"
wpId: 4099
---

E-Mail Tracking mit Google Analytics: Neben den bereits vorgestellten Kennzahlen will man auch gerne weiterführende Analysen erhalten. Dies gilt speziell für den Zeitpunkt nach der Mailzustellung und die Reaktion bezogen auf diese. Dies könnte das Verhalten auf der Webseite in Bezug auf Produktkäufe oder die Anmeldung für einen Service. Diese Informationen erhält man mit einem Web Analytics Tool wie Google Analytics.

Dafür werden Kampagnenparameter an die URLs im Mailing angehängt. Und zusätzlich erhältst du Informationen von welcher Kampagne die Nutzer gekommen sind und wie effektiv und wirtschaftlich diese war. Und du kannst diese URL Parameter nicht nur für deine Mailings nutzen sondern auch für alle anderen Formate mit einem Link wie ein externes Werbemittel z.B. bei Facebook.

<div class="video" data-provider="youtube" data-id="zfCu8UDClDI"></div>

Bei einigen E-Mail Tools kannst du direkt die vorgegebenen Parameter in Felder dafür hinterlegen und es werden automatisch den URLs die Parameter angehängt. Ansonsten kannst du diese URLs aber auch selber erzeugen. Voraussetzung für die URL Parameter ist natürlich das Vorhandensein eines Google Analytics Konto für deine Webseite.

Hier einmal auch eine Anleitung und Erklärung von Google für die Tracking Parameter: <https://support.google.com/analytics/answer/1033863?hl=de#zippy=%2Cthemen-in-diesem-artikel>

Deinen URLs können bis zu fünf Parameter hinzugefügt werden:

- utm\_source: z. B. der Werbetreibende, z.B. Newsletter5
- utm\_medium: das Werbe- oder Marketingmedium, z. B. E-Mail
- utm\_campaign: beispielsweise der Kampagnenname, Slogan oder Gutscheincode für ein Produkt
- utm\_term: die Keywords für die bezahlte Suche. Bei der manuellen Tag-Kennzeichnung bezahlter Keyword-Kampagnen solltest du "utm\_term" verwenden, um das Keyword festzulegen.
- utm\_content: Abgrenzung ähnlicher Inhalte oder Links in derselben Anzeige. Wenn z. B. eine E-Mail zwei "Call-to-Action"-Links enthält, kannst du "utm\_content" verwenden und unterschiedliche Werte für die beiden Links festlegen, um so festzustellen, welche Version effektiv war.

Jeder Parameter muss mit einem von dir zugewiesenen Wert gepaart werden. Alle Parameter/Wert-Paare enthalten dann eindeutige Kampagneninformationen.

### Für die Kampagne Sale 2022 kannst du zum Beispiel die folgenden Parameter/Wert-Paare verwenden:

- utm\_source = rabatt-mail, um Zugriffe zu kennzeichnen, die von der E-Mail-Kampagne stammen
- utm\_medium = email, um zu sehen, welche Zugriffe von der E-Mail-Kampagne im Vergleich zu anderen Kampagnen stammen
- utm\_campaign = sale2022, um die Kampagne insgesamt zu kennzeichnen
- utm\_content = Headergrafik, um die einzelnen Elemente in der Mail zu kennzeichnen.

Die benutzerdefinierte Kampagnen-URL würde dann wie folgt aussehen:

<https://www.example.com/?utm_source=rabatt-mail&utm_medium=email&utm_campaign=sale2022&utm_content=headergrafik>

Bei den URL Parametern müssen immer utm\_source, utm\_medium und utm\_campaign enthalten sein. utm\_term und utm\_content sind optional. utm\_ ist einfach das erforderliche Präfix für diese Parameter. Ich arbeite bei allen Parametern mit utm\_content um eine bessere Unterscheidung der einzelnen Mailinhalte zu erhalten. Viele E-Mail Tools haben aber auch eine sogenannte Heatmap für die Klicks auf die einzelnen Mailelemente. Schreib am besten die Beschreibungen für die utm Parameter immer klein. So entstehen keine Verwechselung bei unterschiedlichen Kampagnen.

Solltest du die URL Parameter für das Tracking am Anfang selber erstelle müssen oder es gerne erst einmal ausprobieren, dann kannst du das Google Tool zur Erstellung nutzen: <https://ga-dev-tools.web.app/campaign-url-builder/>

Diese Tracking Parameter sind für die Klicks also die Aktionen der Empfänger. Aber wie bereits gesehen ist die Klickrate speziell in den Newsletter Kampagnen sehr gering. Hier gibt es dann die Möglichkeit auch die Öffnungen zu tracken. Hierfür kann man das sogenannte Measurement Protocols von Universal Analytics nutzen. Es wird ein Pixel erstellt, der einen Google Analytics-Aufruf erzeugt. Dazu wird eine Zählpixel URL aus verschiedenen Parametern zusammengebaut. Diese wird dann als Bild-URL in ein E-Mail-Template eingebunden. Dadurch kannst du feststellen welche E-Mail Öffnungen auch ohne Klick mit einem Kauf des Empfängers zusammen hängen.

Das Measurement Protocol ruft die eingebundene Bild-Datei auf den Google Analytics Servern auf. Google erhält mithilfe der URL-Parameter Informationen darüber, in welches Profil welche Daten getrackt werden sollen. Dabei werden keine persönlich identifizierbaren Daten übertragen.

Email Tracking - Measurement Protocol: <https://developers.google.com/analytics/devguides/collection/protocol/v1/email?hl=de>
