import unittest

from functions.data_output import getListOfMovies
from models.movie import Movie


class TestApiFunctionallity(unittest.TestCase):

    def test_movie_list(self):
        newmov = Movie(id='1', title='Dinosaur Planet')
        list = getListOfMovies()
        # act
        self.assertEqual(newmov, list[0])
        # assert

    def test_empty_movie_list(self):
        list = getListOfMovies()
        assert list is not []


if __name__ == '__main__':
    unittest.main()
