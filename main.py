"""
Implementation of Programming Project Flask API
"""
import os

from flask_cors import CORS
from flask import Flask, request, render_template
from functions.data_output import get_list_of_movies, get_list_of_recommendation
from functions.database_operations import init_database

# This enables ide support for our custom functions and models
__all__ = ['get_list_of_movies', 'get_list_of_recommendation', 'init_database']

# enables flask
app = Flask(__name__)

# enables CORS
CORS(app)


@app.route('/', methods=['GET'])
def index():
    """
    Enpoint home route
    returns the index html 
    """
    return render_template('index.html')


@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Endpoint for the movies
    trys to execute the get_list_of_movies function 
    returns the result as a json
    """
    try:
        return get_list_of_movies()
    except Exception as e:
        return 'There was an error with the data. The message was: ({0})'.format(e), 400


@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    """
    Endpoint for the recommendations
    checks if the url contains ?movies=
    checks if the data is either an int or list[int] and adds to a list
    trys to execute the get_list_of_recommendations with this data
    returns the recommendations or a 400 if anything goes wrong
    """
    request_data = request.args.get('movies')
    if (request_data is None):
        return 'No input data was given', 400
    try:
        if ',' in request_data:
            movie_ids = [int(mov) for mov in request_data.split(',')]
            if (len(movie_ids) > 5):
                return 'No more than five movies can be selected at a time', 400
        else:
            movie_ids = [int(request_data)]
        return get_list_of_recommendation(movie_ids)
    except Exception as e:
        return 'The input data is not in the correct format. The message was: ({0})'.format(e), 400


if __name__ == '__main__':
    """
    configures the port and hosting for the flask api
    """
    init_database()
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)
