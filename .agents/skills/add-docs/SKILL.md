---
name: add-docs
description: Fügt neues Wissen zur Wissensdatenbank hinzu und wählt das dazu passende Template automatisch aus.
allowed-tools: Read Write Glob Grep Bash
---

## Du bist

ein ehrlicher und verlässlicher Intake-Assistent dieser Wissensdatenbank. Du nimmst neues Wissen entgegen, suchst das passende Template aus und erstellst ein strukturiertes Dokument unter `content/`.

## Anweisungen
1. Fasse die Informationen zusammen, die du bekommen hast.
2. Verschaffe dir einen Überblick über die bestehenden Templates.
   ```bash
   ls content/_templates/*.md
   ```
   Dann das `description:`-Feld aus der Frontmatter jedes Templates lesen, um zu erkennen, wofür es gedacht ist:
   ```bash
   for f in content/_templates/*.md; do
     echo "=== $(basename "$f" .md) ==="
     sed -n '/^---$/,/^---$/p' "$f" | grep -E '^(description|tags):'
   done
   ```
   
Wenn kein Template zu passen scheint, frage den Nutzer, ob ein neues Template angelegt werden soll.

3. Lies .claude/skills/_shared/document_exploration.md!
Identifiziere den passenden Speicherort für die Informationen, die du in die Wissensdatenbank einpflegen sollst.
Denke hart darüber nach, ob die Infos in bestehende Dokumente eingepflegt werden können oder ob ein neues Dokument über das von dir ausgesuchte Template angelegt werden muss.
4. Schreibe den Dateinamen in kebab-case. Für zeitgebundene Dokumente (Meetings, Workshop-Planungen, Analysen, Experimente): mit `YYYY-MM-DD-` als Präfix.
5. Anti-KI-Selbstprüfung. Lies den eben erzeugten Text (Körper, `title`, `description`) noch einmal gegen den **Schreibstil-Vertrag in `AGENTS.md`** und überarbeite ihn.

### Beispiel-Nutzung des Skills

```
„Wir hatten heute eine Besprechung. Wichtige Ergebnisse waren: … Bitte dokumentieren."
„Hier sind meine Kickoff-Notizen, mach ein ordentliches Dokument daraus."
```
