# Lernwortschatz Transkription zu JSON

## Projektübersicht

Dieses Projekt konzentriert sich darauf, Vokabeln (Lernwortschatz) aus einem deutschen Sprachlehrbuch in ein strukturiertes JSON-Format zu transkribieren. Ziel ist es, eine digitale Version der Vokabelliste zu erstellen, die das deutsche Wort, die englische Übersetzung, einen Beispielsatz mit ausgelassenem Wort und das ursprüngliche Wort enthält.

## Zweck

Das Ziel dieses Projekts ist es, den Lernwortschatz aus dem Lehrbuch zu digitalisieren. So können die Daten leichter zugänglich gemacht und in Sprachlern-Apps, Tools oder Datenbanken integriert werden. Das JSON-Format sorgt dafür, dass die Daten gut strukturiert, durchsuchbar und programmatisch verwendbar sind.

## Wie es funktioniert

### Aufgabenübersicht

Die Aufgabe besteht darin, die Vokabeln und die dazugehörigen Beispielsätze manuell aus den bereitgestellten Bildern des Lehrbuchs zu transkribieren. Jeder Vokabeleintrag wird in vier spezifische Spalten unterteilt:

1. **Wort**: Das deutsche Vokabelwort (einschließlich aller Formen) wie es im Lehrbuch steht.
2. **Übersetzung**: Die englische Übersetzung des Wortes, basierend auf dem Beispielsatz.
3. **Beispielsatz**: Ein Beispielsatz aus dem Lehrbuch, bei dem das Vokabelwort durch einen Unterstrich ersetzt wurde. Dies dient als Lückentext.
4. **Antwort**: Das ursprüngliche Vokabelwort, das im Beispielsatz ersetzt wurde.

### Ausgabeformat

Die Ausgabe ist ein JSON-Array, in dem jedes Vokabelwort und die zugehörigen Details als Objekt dargestellt werden. Hier ist ein Beispiel für das Ausgabeformat:

```json
[
  {
    "Word": "weil",
    "Translation": "because",
    "Example Sentence": "Ich bin traurig, ______ ich hier keinen Menschen kenne.",
    "Answer": "weil"
  }
]
```
