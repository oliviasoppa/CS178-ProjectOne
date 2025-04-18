
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

# Create 
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

@app.route('/update-rating', methods=['GET', 'POST'])
def update_rating():
    country = request.args.get('country') if request.method == 'GET' else request.form.get('country')
    if request.method == 'POST':
        username = request.form['username']
        new_rating = int(request.form['rating'])
        new_year = request.form['year']
        try:
            table.update_item(
                Key={'Country': country, 'Username': username},
                UpdateExpression="SET Rating = :r, YearVisited = :y",
                ExpressionAttributeValues={':r': new_rating, ':y': new_year}
            )
            flash("Rating updated successfully!", "success")
        except Exception as err:
            flash(f"Error: {err}", "danger")
        return redirect('/')
    return render_template('update_rating.html', country=country)

@app.route('/delete-rating', methods=['GET', 'POST'])
def delete_rating():
    country = request.args.get('country') if request.method == 'GET' else request.form.get('country')
    if request.method == 'POST':
        username = request.form['username']
        try:
            table.delete_item(Key={'Country': country, 'Username': username})
            flash("Rating deleted successfully!", "success")
        except Exception as err:
            flash(f"Error: {err}", "danger")
        return redirect('/')
    return render_template('delete_rating.html', country=country)

@app.route('/display-rating', methods=['GET', 'POST'])
def display_rating():
    country = request.args.get('country') if request.method == 'GET' else request.form.get('country')
    result = None
    if request.method == 'POST':
        username = request.form['username']
        try:
            response = table.get_item(Key={'Country': country, 'Username': username})
            result = response.get('Item')
        except Exception as err:
            flash(f"Error: {err}", "danger")
            return redirect('/')
        return render_template('display_rating.html', country=country, result=result)

    return render_template('display_rating.html', country=country, result=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)