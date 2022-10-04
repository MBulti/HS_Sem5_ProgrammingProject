import os
import sys
import pandas as pd
import numpy as np

from logging import error
from datetime import datetime
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity


def prepare_data():
    start = datetime.now()
    datasets = ['data/combined_data_1.txt', 'data/combined_data_2.txt',
                'data/combined_data_3.txt', 'data/combined_data_4.txt']
    for file in datasets:
        if not os.path.isfile(file):
            raise FileNotFoundError(
                'Not all the required files exist. Please download them and move the to the data folder!')

    if not os.path.isfile('data/netflix_rating.csv'):
        with open("data/netflix_rating.csv", mode="w") as w:
            review_counter = 0
            for file in datasets:
                print(file)
                with open(file) as f:
                    for line in f:
                        line = line.strip()
                        if line.endswith(":"):
                            movie_id = line.replace(":", "")
                            review_counter = 0
                        else:
                            if (review_counter < 500):
                                row_data = []
                                row_data = [item for item in line.split(",")]
                                row_data.insert(0, movie_id)
                                row_data.pop()
                                if (int(row_data[2]) >= 3):
                                    w.write(",".join(row_data))
                                    w.write('\n')
                                    review_counter += 1
    else:
        raise FileExistsError(
            'File already exists. Please delete to try again!')
    print('Time taken :', datetime.now() - start)


def create_similarity_matrix():
    start = datetime.now()
    df = pd.read_csv('data/netflix_rating.csv', sep=',',
                     names=['movie', 'user', 'rating'])
    if not os.path.isfile('data/sparse_matrix.npz'):
        sparse_matrix = sparse.csr_matrix((
            df.rating.values, (df.user.values, df.movie.values)
        ))
        sparse.save_npz("data/sparse_matrix.npz", sparse_matrix)
        print('Created sparse Matrix')
    else:
        sparse_matrix = sparse.load_npz('data/sparse_matrix.npz')

    if not os.path.isfile('data/movie_similarity.npz'):
        start = datetime.now()
        movie_similarity = cosine_similarity(
            X=sparse_matrix.T, dense_output=False)
        # Store this sparse matrix in disk before using it. For future purposes.
        sparse.save_npz("data/movie_similarity.npz", movie_similarity)
        print('Created similarity Matrix')
    else:
        movie_similarity = sparse.load_npz("data/movie_similarity.npz")

    if not os.path.isfile('data/recommendation.csv'):
        movie_ids = np.unique(movie_similarity.nonzero()[1])
        with open('data/recommendation.csv', mode='w') as m:
            for movie in movie_ids:
                sim_movies = movie_similarity[movie].toarray().ravel().argsort()[
                    ::-1][1:]
                current_movies = list(sim_movies[:20])
                current_movies.insert(0, movie)
                print(current_movies)
                m.write(",".join(str(e) for e in current_movies))
                m.write('\n')
        print('Created similatiry csv for top 20 movies')

    print('Time taken :', datetime.now() - start)


if __name__ == '__main__':
    args = sys.argv
    if (len(args) <= 1):
        error('No Parameters were set. No Function will be executed!')
    else:
        globals()[args[1]]()
