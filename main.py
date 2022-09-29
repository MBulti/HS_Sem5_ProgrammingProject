"""
Implementation of Programming Project Flask API
This returns the movie recommendation based on a entered movie
"""
import os


from flask_cors import CORS
from flask import Flask, request, render_template
from recommendation import getListOfMovies, getListOfRecommendations


__all__ = [getListOfMovies, getListOfRecommendations]
    
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')

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