import csv, os, multiprocessing as mp

from itertools import count
from multiprocessing import process

listOfMovies = []
listOfRecommendations = []


def getListOfMovies():
    global listOfMovies
    with open("data/movie_titles.csv", newline='') as f:
        reader = csv.reader(f) 
        if not listOfMovies:          
            listOfMovies = list(reader)
        return listOfMovies


def getListOfRecommendations(movies):
    return movies


def getRecommendation():
    return None
