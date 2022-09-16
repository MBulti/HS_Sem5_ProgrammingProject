import csv

# os, multiprocessing as mp

# from itertools import count
# from multiprocessing import process

listOfMovies = []
listOfRecommendations = []


def getListOfMovies():
    global listOfMovies
    with open("data/movie_titles.csv", newline='', encoding='latin-1') as f:
        reader = csv.reader(f) 
        if not listOfMovies:          
            listOfMovies = list(reader)
        return listOfMovies


def getListOfRecommendations(movies):
    return movies


def getRecommendation():
    return None


def load_data():
    with open("netflix_rating.csv", mode = "w") as nf:
        rating_files = ['combined_data_4.txt'] 
        for file in rating_files:
            with open(file) as f:
                for line in f:
                    line = line.strip()
                    if line.endswith(":"):
                        movie_id = line.replace(":", "")
                    else:
                        row_data = []
                        row_data = [item for item in line.split(",")]
                        row_data.insert(0, movie_id)
                        nf.write(",".join(row_data))  
                        nf.write('\n')

    