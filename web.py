"""
Ciaran Farley
webapp to host www.cturtle98.com
"""
import os
from flask import Flask, render_template, send_from_directory



app = Flask(__name__, template_folder='html/templates/', static_folder = 'html/static')

@app.route('/')
def index() :
	return render_template('home.html',)

@app.route('/ham/')
def ham() :
	return render_template('ham.html')

if __name__ == '__main__' :
    app.run(host='::', port=80)
