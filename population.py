from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Define a function to fetch data from the database for a specific country
def get_country_data(country):
    conn = sqlite3.connect('population_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM your_table WHERE country_name=?", (country,))
    data = c.fetchall()
    conn.close()
    return data

# Define route for the homepage displaying Italy data
@app.route('/')
def index():
    # Get data for Italy
    italy_data = get_country_data('Italy')
    return render_template('index.html', country='Italy', data=italy_data)

# Define route for Korea data
@app.route('/korea')
def korea():
    # Get data for Korea
    korea_data = get_country_data('Korea')
    return render_template('index.html', country='Korea', data=korea_data)

# Define route for Japan data
@app.route('/japan')
def japan():
    # Get data for Japan
    japan_data = get_country_data('Japan')
    return render_template('index.html', country='Japan', data=japan_data)

if __name__ == '__main__':
    app.run(debug=True)