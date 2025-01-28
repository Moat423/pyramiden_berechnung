# pyramiden_berechnung

Ein sehr einfach Python Program zur Berechnung der Seitenkantenlänge von n-Grundflächen Pyramiden
Es beinhaltet ein grafisches Programm zur Berechnung und Visualisierung von Pyramiden.

![Pyramid Calculation](pictures/pyramid.png)

## Voraussetzungen

Stellen Sie sicher, dass Sie Python auf Ihrem Computer installiert haben. Sie können Python von der [offiziellen Website](https://www.python.org/downloads/) herunterladen und installieren.

## Installation unter Windows

### Schritt 1: Öffnen der Eingabeaufforderung (Command Line)

1. Drücken Sie die `Windows`-Taste auf Ihrer Tastatur.
2. Geben Sie `cmd` ein und drücken Sie die `Enter`-Taste. Dadurch öffnet sich die Eingabeaufforderung.

### Schritt 2: Herunterladen des Repositorys

1. Wechseln Sie in das Verzeichnis, in dem Sie das Repository speichern möchten. Zum Beispiel:
    ```bash
    cd C:\Benutzer\IhrBenutzername\Dokumente
    ```

2. Laden Sie das Repository herunter (=klonen) mit Git:
    ```bash
    git clone https://github.com/Moat423/pyramiden_berechnung.git
    ```

3. Wechseln Sie in das Verzeichnis des Projekts:
    ```bash
    cd pyramiden_berechnung
    ```

### Schritt 3: Erstellen einer virtuellen Umgebung

1. Erstellen Sie eine virtuelle Umgebung:
    ```bash
    python -m venv venv
    ```

2. Aktivieren Sie die virtuelle Umgebung:
    ```bash
    venv\Scripts\activate
    ```

### Schritt 4: Installieren der benötigten Bibliotheken

1. Installieren Sie die benötigten Bibliotheken:
    ```bash
    pip install -r requirements.txt
    ```

### Schritt 5: Programm ausführen

1. Um das Programm zu starten, führen Sie das Python-Skript aus:
    ```bash
    python graf_pyramiden_rechner.py
    ```

## Alternative Methode (ohne virtuelle Umgebung)

Falls die virtuelle Umgebung nicht funktioniert (Schritt 3) oder Probleme auftreten, können Sie die alternative Version `pyramiden_rechner.py` verwenden, die nur mit standardmäßig installierten Bibliotheken funktioniert.

### alternativer Schritt 5: Programm ausführen

1. Um das alternative Programm zu starten, führen Sie das Python-Skript aus:
    ```bash
    python pyramiden_rechner.py
    ```

## Installation unter macOS und Linux

    ```bash
    git clone https://github.com/Moat423/pyramiden_berechnung.git
    cd pyramiden_berechnung
    python -m venv venv
	source venv/bin/activate
    pip install -r requirements.txt
    python graf_pyramiden_rechner.py
    ```
### altertnativ:
	
    ```bash
    python pyramiden_rechner.py
    ```

## Hinweise

- Stellen Sie sicher, dass Sie sich in der virtuellen Umgebung befinden, bevor Sie das Programm `graf_pyramiden_rechner.py` ausführen (Schritt 3).
- Wenn Sie Probleme haben, überprüfen Sie, ob alle Voraussetzungen erfüllt sind und alle Schritte korrekt ausgeführt wurden.

## Kontakt

Bei Fragen oder Problemen können Sie mich über GitHub kontaktieren.

Viel Spaß mit dem Programm zur Pyramidenseitenlängenberechnung!
