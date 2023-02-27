"""
Lab 2 task 3
Main Function
Creates web application, where user inputs artist's name and gets readdressed\
to map with colored and marked available markets
"""

from flask import Flask, render_template, request
from create_map_page import create_map_page
app = Flask(__name__)

@app.route('/markets_map', methods=['POST'])
def map_page():
    """Creates map and readdresses user there"""
    while True:
        artists_name = request.form['Artist name']
        if create_map_page(artists_name):
            break
        return render_template('entry.html', the_title='Retry and enter valid name')
    return render_template('Available_markets.html')

@app.route('/')
@app.route('/entry')
def entry_page():
    """Main page"""
    return render_template('entry.html',
                           the_title='Input artist name and get map with available markets')

if __name__ == '__main__':
    app.run(debug = True)
