import os
import sys
import pandas as pd
import numpy as np
import json

from logging import error
from datetime import datetime
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from database_operations import insert_into_recomendations_table, insert_into_movies_table

__all__ = ['insert_into_movies_table', 'insert_into_recomendations_table']


def get_user_ids_to_drop():
    user_ids_to_drop = []
    f = open('data/testset.json')
    data = json.load(f)
    for i in data:
        user_ids_to_drop.append(i['User_Id'])
    return user_ids_to_drop


def prepare_movies_db() -> None:
    '''
    Prepares the movie db
    for this to work the data folder needs the movie_titles.csv file
    '''
    if not os.path.isfile('data/movie_titles.csv'):
        raise ValueError(
            'The required files are missing. Please check installation guide')
    list_of_movies: list[str] = []
    with open('data/movie_titles.csv', encoding='latin-1') as f:
        for line in f:
            list_of_movies.append(create_movie(line))

    insert_into_movies_table(list_of_movies)
    # print(list_of_movies)


def create_movie(line: str) -> str:
    '''
    creates a movie based on the csv line given by the get_list_of_movies function
    splits the line by ,
    replaces the \\n at the end
    if the movie contains a , it will join the remaining title
    returns a touple for the db entry
    '''
    movie = line.split(',')
    movie[-1] = movie[-1].replace('\n', '')
    movie_id = movie.pop(0)
    movie_year = movie.pop(0)
    if (len(movie) > 1):
        movie_title = movie.pop(0)
        movie_title += ','.join(movie)
    else:
        movie_title = movie[0]
    return (movie_id, movie_year, movie_title)


def get_user_ids_to_drop():
    user_ids_to_drop = []
    f = open('data/testset.json')
    data = json.load(f)
    for i in data:
        user_ids_to_drop.append(i['User_Id'])
    return user_ids_to_drop


def prepare_data() -> None:
    '''
    Creates a combined csv file from the txt files of the netflix price data
    In order for this to work the data folder needs to be filed with the combined_data 1 - 4
    This uses only the ratings above 3 and only 500 reviews per movie
    '''
    user_ids_to_drop = get_user_ids_to_drop()
    start_time = datetime.now()
    datasets = ['data/combined_data_1.txt', 'data/combined_data_2.txt',
                'data/combined_data_3.txt', 'data/combined_data_4.txt']
    for file in datasets:
        if not os.path.isfile(file):
            raise FileNotFoundError(
                'Not all the required files exist. Please download them and move the to the data folder!')

    if not os.path.isfile('data/netflix_rating.csv'):
        with open('data/netflix_rating.csv', mode='w') as w:
            review_counter = 0
            for file in datasets:
                print(file)
                with open(file) as f:
                    for line in f:
                        line = line.strip()
                        if line.endswith(':'):
                            movie_id = line.replace(':', '')
                            print(movie_id)
                            review_counter = 0
                        else:
                            if (review_counter <= 500):
                                row_data = []
                                row_data = [item for item in line.split(',')]
                                row_data.insert(0, movie_id)
                                row_data.pop()
                                if (int(row_data[2]) in user_ids_to_drop):
                                    continue
                                if (int(row_data[2]) == 5):
                                    w.write(','.join(row_data))
                                    w.write('\n')
                                    review_counter += 1
    else:
        raise FileExistsError(
            'File already exists. Please delete to try again!')
    print('Time taken :', datetime.now() - start_time)


def create_similarity_matrix() -> None:
    '''
    Creates a similarty matrix based on the rating csv file
    In order for this to work the prepare data function must have been executed 
    A sparse matrix will be created base on which we create a movie to movie similarity
    Since this is 1 17700 x 17700 matrix we create a top 20 matrix based on this
    The results are entered into a csv file
    '''
    start_time = datetime.now()
    df = pd.read_csv('data/netflix_rating.csv', sep=',',
                     names=['movie', 'user', 'rating'])
    if not os.path.isfile('data/sparse_matrix.npz'):
        print('Creating sparse matrix')
        sparse_matrix = sparse.csr_matrix((
            df.rating.values, (df.user.values, df.movie.values)
        ))
        sparse.save_npz('data/sparse_matrix.npz', sparse_matrix)
        print('Created sparse Matrix')
    else:
        sparse_matrix = sparse.load_npz('data/sparse_matrix.npz')

    if not os.path.isfile('data/movie_similarity.npz'):
        print('Creating similarity Matrix')
        start_time = datetime.now()
        movie_similarity = cosine_similarity(
            X=sparse_matrix.T, dense_output=False)
        sparse.save_npz('data/movie_similarity.npz', movie_similarity)
        print('Created similarity Matrix')
    else:
        movie_similarity = sparse.load_npz('data/movie_similarity.npz')

    if not os.path.isfile('data/recommendation.csv'):
        print('Creating similatiry db table for top 15 movies')
        recommendations = []
        movie_ids = np.unique(movie_similarity.nonzero()[1])
        for movie in movie_ids:
            sim_movies = movie_similarity[movie].toarray().ravel().argsort()[
                ::-1][1:]
            current_movies = list(sim_movies[:20])
            recommendations.append(
                (int(movie), ','.join(str(e) for e in current_movies)))
        insert_into_recomendations_table(recommendations)
        print('Created similatiry csv for top 20 movies')

    print('Time taken :', datetime.now() - start_time)


if __name__ == '__main__':
    '''
    We create this to anable the usage of this file with python execution paramenters
    Usage:
    python -m data_prep.py prepare_data
    or:
    py.exe .\functions\data_prep.py prepare_data 
    '''
    args = sys.argv
    if (len(args) <= 1):
        error('No Parameters were set. No Function will be executed!')
    else:
        globals()[args[1]]()
