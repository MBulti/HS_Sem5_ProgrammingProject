# HS_Sem5_ProgrammingProject

HS Osnabrück - 5 Semester - Prüfungsleistung im Modul Programmierprojekt

## Hinweis

Nur Implementierung der API Schnittstelle.
Die Implementierung des Frontends wird in einem separaten Repository bearbeitet. (https://github.com/MBulti/HS_Sem5_ProgrammingProject_Frontend)

## Aufgabenbeschreibung

Netflix streams movies to its users andshared its data to provide improved
movie recommendations. You are tasked to create a recommenation system for its users.

To do this exercise, the company provides several files, such as information on the movies, and user ratings,
summing up to a total of 480189 unique users and 17770 movies.
As the movie details provided in the data-set you are expected to take advantage of publicly available information, such as the latest IMDb information here
https://www.imdb.com/interfaces/.

Further details can be found here
https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data

## Projektmanagement

Die Durchführung des Projektes erfolgt in drei Sprints. Das Management wird über Jira durchgeführt.
https://hsosprojekte.atlassian.net/jira/software/projects/PROG/boards/2/backlog

## Deployment

Die API wird über Heroku automatisch bei Änderungen gebaut und neu deployed.
Zurzeit ist sie über https://recommender-system-hs.herokuapp.com/ aufrufbar.

Eine detailierte Beschreibung folgt.

Rückgabe der Filme:
https://recommender-system-hs.herokuapp.com/movies

## How to use

git clone https://github.com/MBulti/HS_Sem5_ProgrammingProject.git
pip install virtualenv
python -m venv env
.\evn\Scripts\activate
pip3 install -r .\requirements.txt

### Run API

python .\main.py

### Create datafiles

Download combined_data 1 - 4 and put into data folder
python .\functions\data_prep.py prepare_data

delete data/recommendations.csv
python .\functions\data_prep.py create_similarity_matrix
