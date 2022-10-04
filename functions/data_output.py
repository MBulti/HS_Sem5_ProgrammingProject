import pandas as pd

from models.movie import Movie
from models.recommendation import Recommendation

__all__ = ['Recommendation', 'Movie']


def get_list_of_movies() -> list[Movie]:
    """
    returns the list of movies that are available
    opens the movie titles csv and creates a movie instance based on the data
    """
    listOfMovies: list[Movie] = []
    with open("data/movie_titles.csv", encoding='latin-1') as f:
        for line in f:
            listOfMovies.append(create_movie(line))
        return listOfMovies


def create_movie(line: str) -> Movie:
    """
    creates a movie based on the csv line given by the get_list_of_movies function
    splits the line by ,
    replaces the \\n at the end
    if the movie contains a , it will join the remaining title
    """
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


def get_list_of_recommendation(movies: list[int]) -> list[Recommendation]:
    """
    returns a list of recommendations based on the given movie ids
    filters the recommendation.csv by the movie id and gets the values
    gives the top 5 Movies bases as a recommendation and casts into a Recommendation instance
    """
    movie_recommendations: list[Recommendation] = []
    for movie in movies:
        if (movie > 17700):
            raise ValueError('The given id is not an actual movie')
        df = pd.read_csv('data/recommendation.csv', header=None)
        recommendations = (df.loc[df[0] == movie].values).tolist()[0]
        movie_recommendations.append(Recommendation(
            movie_id=movie, recommendations=recommendations[1:6]))
    return movie_recommendations
