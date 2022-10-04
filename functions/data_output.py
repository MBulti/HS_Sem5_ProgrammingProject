import pandas as pd
from models.movie import Movie
from models.recommendation import Recommendation


def getListOfMovies():
    listOfMovies = []
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for line in f:
            listOfMovies.append(create_movie(line))
        return listOfMovies


def create_movie(line):
    movie = line.split(',')
    movie[-1] = movie[-1].replace('\n', '')
    movie_id = movie.pop(0)
    movie_date = movie.pop(0)
    if (len(movie) > 1):
        movie_title = movie.pop(0)
        movie_title += ','.join(movie)
    else:
        movie_title = movie[0]
    return Movie(id=movie_id, release_year=movie_date, title=movie_title)


def getListOfRecommendations(movies: list[int]):
    movie_recommendations = []
    for movie in movies:
        if (movie > 17700):
            raise ValueError('The given id is not an actual movie')
        df = pd.read_csv('data/recommendation.csv', header=None)
        recommendations = (df.loc[df[0] == movie].values).tolist()[0]
        movie_recommendations.append(Recommendation(
            movie_id=movie, recommendations=recommendations[1:6]))
    return movie_recommendations
