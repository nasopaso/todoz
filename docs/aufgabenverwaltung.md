---
title: "Aufgabenverwaltung"
tags: [projekt]
created: 2026-11-19
description: "Projektübersicht der Aufgabenverwaltung für die Kommandozeile."
---

# Aufgabenverwaltung

## Inhaltsverzeichnis

- [Zusammenfassung](#zusammenfassung)
- [Problem](#problem)
- [Lösung](#lösung)
- [Was die Lösung unterscheidet](#was-die-lösung-unterscheidet)
- [Zielgruppe](#zielgruppe)
- [Erfolgskriterien](#erfolgskriterien)
- [Umfang](#umfang)
- [Was benötigt wird](#was-benötigt-wird)
- [Vision](#vision)

## Zusammenfassung

Die Aufgabenverwaltung ist ein Python-Programm für die Kommandozeile. Es verwaltet Aufgaben in einer lokalen JSON-Datei.

## Problem

Wer Aufgaben festhalten und ihren Erledigungsstatus nachverfolgen möchte, benötigt eine Möglichkeit, diese Informationen zwischen Programmaufrufen zu speichern.

## Lösung

Das Programm kann Aufgaben hinzufügen, alle Aufgaben anzeigen und Aufgaben als erledigt markieren. Es speichert sie in `aufgaben.json` im aktuellen Arbeitsverzeichnis. Eine fehlende Datei wird beim ersten Hinzufügen angelegt.

## Was die Lösung unterscheidet

Die Bedienung erfolgt über drei Kommandozeilenbefehle. Die Daten liegen lokal in einer JSON-Datei; das Programm hat keine Python-Laufzeitabhängigkeiten außerhalb der Standardbibliothek.

## Zielgruppe

Das Programm eignet sich für Personen, die Aufgaben über die Kommandozeile lokal verwalten möchten. Eine darüber hinausgehende Zielgruppe ist nicht festgelegt.

## Erfolgskriterien

Als überprüfbare Kriterien für die vorhandenen Funktionen bieten sich an:

- Aufgaben lassen sich hinzufügen und bei späteren Aufrufen anzeigen.
- Offene und erledigte Aufgaben sind in der Liste unterscheidbar.
- Eine Aufgabe lässt sich anhand ihrer ID als erledigt markieren.
- Die Tests laufen mit `uv run pytest`, ohne vorhandene Aufgabendaten zu verändern.

## Umfang

Zum aktuellen Funktionsumfang gehören die Befehle `add`, `list` und `done` sowie die lokale Speicherung. Eine grafische Oberfläche oder Synchronisation zwischen Geräten ist nicht implementiert.

## Was benötigt wird

Für die Nutzung werden Python 3.7 oder neuer und `uv` benötigt. Für die Tests installiert `uv` die Entwicklungsabhängigkeiten aus `uv.lock`.

## Vision

Eine langfristige Projektvision ist noch nicht festgelegt.
