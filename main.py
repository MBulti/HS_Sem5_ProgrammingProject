"""
Implementation of Programming Project Flask API
This returns the movie recommendation based on a entered movie
"""
import os

from flask_cors import CORS
from flask import Flask, request, render_template
from functions.data_output import getListOfMovies, getListOfRecommendations

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        return getListOfMovies()
    except Exception as e:
        return 'There was an error with the data. The message was: ({0})'.format(e), 400


@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    requestData = request.args.get('movies')
    if (requestData is None):
        return 'No input data was given', 400
    try:
        if ',' in requestData:
            movie_ids = [int(mov) for mov in requestData.split(',')]
            if (len(movie_ids) > 5):
                return 'No more than five movies can be selected at a time', 400
        else:
            movie_ids = [int(requestData)]
        return getListOfRecommendations(movie_ids)
    except Exception as e:
        return 'The input data is not in the correct format. The message was: ({0})'.format(e), 400


if __name__ == '__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port, debug=True)
