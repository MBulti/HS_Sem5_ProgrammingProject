import unittest

from models.movie import Movie
from functions.data_output import get_list_of_movies

__all__ = ['get_list_of_movies', 'Movie']


class TestApiFunctionallity(unittest.TestCase):
    '''
    API Unit tests
    '''

    def test_movie_list(self) -> None:
        '''
        tests if the movie list contains the first movie
        '''
        movie_to_test = Movie(id='1', release_year='2003',
                              title='Dinosaur Planet')
        list_of_movies = get_list_of_movies()

        self.assertEqual(movie_to_test, list_of_movies[0])

    def test_empty_movie_list(self) -> None:
        '''
        tests if the given list is not empty
        '''
        list_of_movies = get_list_of_movies()
        assert list_of_movies is not []


if __name__ == '__main__':
    '''
    enables execution of the tests as a seperate file for ci/cd
    '''
    unittest.main()
