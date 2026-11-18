## Drei Stufen

Lies nie direkt den Volltext aller Dateien aus. Erst eingrenzen, dann lesen.
Kein Treffer ist auch ein Ergebnis, das du melden sollst und fragst, was du tun sollst.

**Stufe 1: Dateinamen.** Immer zuerst, für jede Anfrage:
```bash
find content -type f -name '*.md' \
  -not -path 'content/_templates/*' \
  -not -path 'content/_skills/*' \
  -not -path 'content/.*' | sort
```
Aus der Liste die 5 Pfade auswählen, die am besten zur Anfrage passen.

**Stufe 2: Frontmatter.** Nur für diese 5 Dateien:
```bash
for f in <die 5 ausgewählten Pfade>; do
  echo "=== $f ==="
  awk '/^---$/{if(s)exit; s=1; next} s{print}' "$f"
  echo
done
```

Aus der Liste die 5 Treffer auswählen, die am besten zur Anfrage passen. Reihenfolge: Description-Match zuerst, dann Titel, dann Tags, dann created.

**Stufe 3: Inhalt.** Nur die verbliebenen Treffer komplett mit `Read` lesen.

**Zeitraum (z. B. „letzte 2 Wochen")
- Dateien im Zeitraum über `-mtime -N` oder `created:` finden
- `mtime` zeigt nur den letzten Edit, `created:` nur die Erstellung. Für ein festes Datum in der Vergangenheit gilt die Commit-Historie:
```bash
git log --since="2026-08-11 00:00" --until="2026-08-12 00:00" --name-only -- content
```
