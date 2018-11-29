"""
Ciaran Farley
webapp to host www.cturtle98.com
"""
import os
from flask import Flask, render_template, send_from_directory



app = Flask(__name__, template_folder='templates/')

@app.route('/')
def index() :
	return render_template('template.html',
		page_title = "cTurtle98.com",
		head = "",
		title = "cTurtle98.com",
		subtitle = "The projects of Ciaran farley",
		content = """webcome to my projects, look around, maybe you will find something interesting"""
		)
"""
@app.route('/main.css')
def main_css():
	f = open('include/main.css')
	css = f.read()
	f.close()
	return css
"""


if __name__ == '__main__' :
    app.run(host='::', port=8088)
