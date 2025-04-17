
from flask import Flask, render_template, request, redirect, url_for, flash

import pymysql
import pymysql.cursors
from dbCode import *

dynamodb = boto3.resource('dynamodb', region_name='us-east-2') 
table = dynamodb.Table('CountryNotes')

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

# 
@app.route('/')
def index():
    countries = get_countries_list()
    return render_template('index.html', results=countries)

@app.route('/add-rating', methods=['GET', 'POST'])
def add_rating():
    country = request.args.get('country') if request.method == 'GET' else request.form.get('country')

    if request.method == 'POST':
        username = request.form['username']
        rating = int(request.form['rating'])
        year = request.form['year']
        try:
            table.put_item(Item={
                'Country': country,
                'Username': username,
                'Rating': rating,
                'YearVisited': year
            })
            flash("Rating added successfully!", "success")
        except Exception as err:
            flash(f"Error: {err}", "danger")
        return redirect('/')
    
    return render_template('add_rating.html', country=country)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)