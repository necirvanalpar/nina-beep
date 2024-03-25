[TR](https://github.com/necirvanalpar/nina-beep/blob/main/LANGS/README_TR.md)
# Nina Warnungen Alarm

Dieses Python-Skript wurde erstellt, um sofort über Nina-Warnungen in Deutschland informiert zu werden. Wenn Warnungen erkannt werden, die für eine bestimmte ARS-Nummer und ein Risikolevel von "Immediate" für eine Region gelten, wird ein Alarmton auf Ihrem Computer ausgegeben.

## Erste Schritte

Um dieses Skript zu verwenden, müssen die [Python](https://www.python.org/) und [requests](https://pypi.org/project/requests/) und [json-Bibliotheken](https://docs.python.org/3/library/json.html) installiert sein. Der `winsound`-Modul funktioniert nur unter Windows-Betriebssystemen.

```bash
pip install -r requirements.txt
```

## Verwendung

1. Geben Sie in der Variable `ninaBaseUrl` die URL des Nina-Servers an.
2. Aktualisieren Sie die [ARS-Nummer](https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json) in der Variable `arsNo` entsprechend Ihrer Region.
3. Stellen Sie die Gefahrenstufe in der Variable `tehlike_seviyesi` ein.
4. Geben Sie den Namen der JSON-Datei in der Variable `filename` an.
5. Führen Sie das Skript aus: `python main.py`

## Mitwirken

Bitte erstellen Sie bei Problemen oder Vorschlägen ein GitHub-Problem oder senden Sie eine Pull-Anforderung.
