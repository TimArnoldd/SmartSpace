# SmartSpace

SmartSpace ist ein Programm welches über Computer Vision Parkplätze analysieren und auswerten kann. Dabei können mehrere Kameras verwendet werden und die Daten über eine REST-API freigegeben.

## Benutzeranleitung

### Parkplätze erfassen

Um Parkplätze zu erfassen kann das Script ```parkingSpacePicker.py``` gestartet werden. Hierbei muss der Name der Datei, welche die Parkplätze speichert, und das Bild, welches als Vorlage dient, angegeben werden.

Anschliessend können mit Linksklick viereckige Polygone erstellt und mit einem Rechtsklick ein bestehendes Polygon entfernt werden.

Um die Konfiguration abzuspeichern und die Applikation zu beenden, kann die Escape-Taste betätigt werden.

### Parkplatzanalyse starten

Um die Parkplatzanalyse zu starten, kann das Script ```main.py``` gestartet werden. Die analysierten Werte werden fortlaufend in die .json-Datei geschrieben.

### Kameras konfigurieren

Um mehrere Kameras zu verwenden kann in der Datei ```main.py``` dies entsprechend angepasst werden. Dabei muss eine Videoquelle, eine Parkplatz-Datendatei und eine Id angegeben werden.















@github sry for the german language :()
