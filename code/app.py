from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import os
from backend.rating_data import RatingData


# Create global variables to store the contents of the datasets
rating_data = None
# populari_data = None

app = Flask(__name__, static_url_path='')
CORS(app)


# Load the datasets before the very first user request and have it available during the entire lifespan of the application.
# Hence, time taken for file I/O is reduced as the csv files (i.e datasets) are only read once and not for every user request.
@app.before_first_request
def load_datasets():
	print("Loading datasets...")
	global rating_data
	rating_data = RatingData()
	# global holed_data
	# holed_data = HoledData()


@app.route('/init', methods=['GET'])
def init():
    # "test method"
    return "Init method called"


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/popularity_based')
def popularity():

    return render_template('index.html')


@app.route('/handle_input', methods=['POST'])
def handle_input():
    if request.method == "POST":
    	return redirect(url_for('home'), code=307)
    else:
    	return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=int(os.environ.get("PORT", 8001)))