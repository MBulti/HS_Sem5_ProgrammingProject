import pandas as pd
from models.movie import Movie
from models.recommendation import Recommendation

listOfMovies = []


def getListOfMovies():
    global listOfMovies
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for line in f:
            listOfMovies.append(create_movie(line))
        return listOfMovies


def create_movie(line):
    movie = line.split(',')
    movie_id = movie[0]
    movie_title = movie[1]
    movie = movie[2:-1]
    if (movie.count('') < len(movie)):
        movie_title += ','.join(movie)
    return Movie(id=movie_id, title=movie_title)


def getListOfRecommendations(movies: list[int]):
    movie_recommendations = []
    for movie in movies:
        if(movie > 17700):
            raise ValueError('The given id is not an actual movie')
        df = pd.read_csv('data/recommendation.csv', header=None)
        recommendations = (df.loc[df[0] == movie].values).tolist()[0]
        movie_recommendations.append(Recommendation(movie_id=movie, recommendations=recommendations[1:6]))
    return(movie_recommendations)
