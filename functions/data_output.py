import pandas as pd

from models.movie import Movie
from models.recommendation import Recommendation
from .database_operations import get_all_movies, get_recommendation_for_movie_id

__all__ = ['Recommendation', 'Movie', 'get_all_movies', 'get_recommendation_for_movie_id']


def get_list_of_movies() -> list[Movie]:
    """
    returns the list of movies that are available
    opens the movie db and casts each value into a movie
    """
    return [Movie(id=full_title[0], release_year=full_title[1], title=full_title[2]) for full_title in get_all_movies()]



def get_list_of_recommendation(movies: list[int]) -> list[Recommendation]:
    """
    returns a list of recommendations based on the given movie ids
    filters the recommendation.csv by the movie id and gets the values
    gives the top 5 Movies bases as a recommendation and casts into a Recommendation instance
    """
    movie_recommendations: list[Recommendation] = []
    for movie in movies:
        if (movie > 17770):
            raise ValueError('The given id is not an actual movie')
        recommendation = get_recommendation_for_movie_id(movie)
        movie_recommendations.append(Recommendation(movie_id=movie, recommendations=[int(f) for f in recommendation[0][1].split(',')]))
    # for movie in movies:
    #     if (movie > 17770):
    #         raise ValueError('The given id is not an actual movie')
    #     df = pd.read_csv('data/recommendation.csv', header=None)
    #     recommendations = (df.loc[df[0] == movie].values).tolist()[0]
    #     movie_recommendations.append(Recommendation(
    #         movie_id=movie, recommendations=recommendations[1:6]))
    return movie_recommendations
