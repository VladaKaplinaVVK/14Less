from flask import Flask, jsonify
from main import *

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<title>')
def get_movie_title(title):
    return get_movie_title(title)


@app.route('/movie/<int:year1>/to/<int:year2>')
def get_movie_by_release_year(years1: int, years2: int):
    return jsonify(get_movie_by_release_year(years1, years2))


@app.route('/rating/<category>')
def get_movie_by_rating(category):
    return jsonify(get_movie_by_rating(category))


@app.route('/genre/<genre>')
def get_movie_by_genre(genre):
    return jsonify(get_movie_by_genre(genre))


if __name__ == '__main__':
    app.run(debug=True)