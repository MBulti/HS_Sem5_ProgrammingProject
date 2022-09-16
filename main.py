"""
Implementation of Programming Project Flask API
This returns the movie recommendation based on a entered movie
"""
import os
from pkgutil import get_data
import wget

from os.path import exists
from flask import Flask, request
from recommendation import *

if(not exists('combined_data_4.txt')):
    print('yep')
    wget.download('https://zenodo.org/record/4556134/files/combined_data_4.txt?download=1')
else:
    print('nop')
    
app = Flask(__name__)

@app.route('/test')
def test_routes():
    if(not exists('netflix_rating.csv')):
        load_data()
    return 'Data loaded', 200

@app.route('/data')
def test_routes():
        load_data()
        return 200

@app.route('/movies')
def get_movies():
    return getListOfMovies()


@app.route('/recommendation')
def get_recommendation():
    requestData = request.form.get('movies')
    if (requestData is None):
        return 'No input data was given', 400
    movieList = requestData.split(',')
    if (movieList is None):
        return 'The input data is not in the correct format', 400
    return getListOfRecommendations(movieList)


if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port, debug=True)