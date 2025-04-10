
from flask import Flask, render_template, request, redirect, url_for, flash

import pymysql
import pymysql.cursors
from dbCode import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

# 
@app.route('/')
def index():
    countries = get_countries_list()
    return render_template('index.html', results=countries)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)