"""
Ciaran Farley
webapp to host www.cturtle98.com
"""
import os
import json
import flask


app = flask.Flask(__name__, template_folder='templates/', static_folder = 'static/')

trusted_proxies = {'127.0.0.1'}

# homepage of my website
@app.route('/')
def index() :
	return flask.render_template('home.jinja2',)


# import my pages
from webpy import redirect
from webpy import ham
from webpy import wishlist
from webpy import bwfs


@app.route('/21bday/')
def twentyonebday() :
  return flask.render_template('21bday.jinja2')

if __name__ == '__main__' :
    app.run(host='::', port=80, debug=False)
