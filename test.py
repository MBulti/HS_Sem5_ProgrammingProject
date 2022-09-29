import unittest

from recommendation import getListOfMovies
    

class TestApiFunctionallity(unittest.TestCase):
    
    def test_movie_list(self):
        subset = {'1': 'Dinosaur Planet'}
        list = getListOfMovies()
        # act
        self.assertDictContainsSubset(subset=subset, dictionary= list)
        # assert
    
    def test_empty_movie_list(self):
        subset = {}
        list = getListOfMovies()
        assert list is not subset
        
if __name__ == '__main__':
    unittest.main()        