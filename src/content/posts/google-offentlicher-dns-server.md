---
title: "Google - Öffentlicher DNS Server"
slug: "google-offentlicher-dns-server"
date: 2009-12-11T11:05:43
updated: 2021-10-14T06:35:03
description: "Das sind die Ziele für seinen eigenen Google DNS-Server. Der Dienst steht allen kostenlos zur Verfügung."
category: "ki-tools"
vgwort: "https://vg06.met.vgwort.de/na/93e7f86612104867a64145c14d6e5c96"
tags:
  - "Google"
wpId: 421
---

Schneller, sicherer und zuverlässiger: Das sind die Ziele, die Google sich für seinen eigenen DNS-Server gesetzt hat. Der Dienst steht allen Interessierten kostenlos als Alternative zum Server ihres Internet-Anbieters zur Verfügung. Ein höheres Tempo soll er dadurch erreichen, dass er DNS-Einträge aktualisiert, bevor ihre Gültigkeitsdauer (time to live, TTL) abgelaufen ist.
Gegen bekannte DNS-Angriffe will Google den Dienst gehärtet haben. Er führe einfache Gültigkeitsprüfungen durch und weise etwa "verdächtige" Antworten anderer Nameserver sofort ab. Dazu gehören fehlerhafte Nachrichten ebenso wie solche, in denen die zurückübermittelte Anfrage-ID, Quell-IP oder -Port oder der Name der Query nicht zu denen der Original-Anfrage passen. Da diese Datenfelder relativ klein sind, können Angreifer jedoch durch eine hinreichend große Menge gefälschter Antworten zufällig passende Werte verwenden und damit dem Server eine falsche Namensauflösung unterschieben.
Interessenten können Googles DNS-Dienst unter den IP-Adressen 8.8.8.8 und 8.8.4.4 erreichen. Allerdings sollte man sich die aktuellen Einstellungen für den Nameserver notieren, bevor man die Einträge dauerhaft ändert, warnt Google.
Quelle: heise online
Hier noch ein kleines Video der Google Story von Nick Scott Studio.
[The Google Story](https://vimeo.com/7285062) from [Nick Scott Studio](https://vimeo.com/studiohansa) on [Vimeo](https://vimeo.com/).
Das Domain Name System (DNS) ist einer der wichtigsten Dienste in vielen IP-basierten Netzen. Seine Hauptaufgabe besteht darin, auf Anfragen zur Namensauflösung zu antworten. DNS funktioniert ähnlich wie Verzeichnisabfragen. Der Benutzer kennt die Domäne (den Namen eines Computers im Internet, an den sich die Leute erinnern können) – zum Beispiel example.org. Diese schickt er als Anfrage ins Internet. Anschließend wird die Domain per DNS in die zugehörige IP-Adresse (die „Verbindungsnummer“ im Internet) umgewandelt – beispielsweise eine IPv4-Adresse oder IPv6-Adresse im Format 192.0.2.42, wie 2001: db8: 85a3: 8d3: 1319: 8a2e: 370: 7347-und mit dem richtigen Computer verbinden.
