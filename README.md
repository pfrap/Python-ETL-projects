# Python ETL projects

## Progetti (1 e 2)
Implementazione funzione di _webscraping_ con estrazione di dati strutturati da sito web, elaborazione dati, caricamento su file csv e database Sqlite3 (scrittura query di esempio tramite Sqlite3).  
Scrittura file log txt con le fasi della procedura. 
 
|PROGETTO|LINK JUPYTER NOTEBOOK|
|:-:|:-|
|Progetto 1|[Jupyter Notebook](./PROJ_1/etl_project_1.ipynb)|
|Progetto 2|[Jupyter Notebook](./PROJ_2/etl_project_2.ipynb)|

### Elenco librerie utilizzate
|LIBRERIA|UTILIZZO|
|:-:|:-|
|Requests|Download dati da web|
|BeautifulSoup|Interpretazione html|
|Pandas|Manipolazione dei dati|
|SQLite3|Lettura database|
|Datetime|Scrittura log file con data e ora|

_** Librerie utilizzate in entrambi i progetti._

## Funzione ETL
File Python con procedura ETL che cicla su file csv, json e XML in una cartella predefinita dall'utente, estrae e trasforma informazioni specifiche, le unifica in file csv e scrive file log.  

[Python file](./ETL/etl_1.py)

|LIBRERIE|UTILIZZO|
|:-:|:-|
|Glob|Lettura file su disco in base a parametri|
|Pandas|Manipolazione dei dati|
|ElementTree|Gestione file XML|
|Datetime|Scrittura log file con data e ora|

## Esercizi

|PROGETTO|LINK JUPYTER NOTEBOOK|
|:-:|:-|
|SQLite3|[Jupyter Notebook](./SQLITE_DB/sqlite_db.ipynb)|
|BeautifulSoup|[Jupyter Notebook](./WEB_SCRAPING/web_scraping.ipynb)|
|Packaging|[Folder](./PACKAGING/)|
|Pylint e Unit testing|[Folder](./CODING_PRACTICES/)|
