"""
Ciaran Farley
webapp to host www.cturtle98.com
"""
import os
import json
import flask
from datetime import datetime


app = flask.Flask(__name__, template_folder='html/templates/', static_folder = 'html/static')


@app.route('/')
def index() :
	return flask.render_template('home.jinja2',)

@app.route('/redirect/', methods=['GET'])
def redirectpage():
  url = flask.request.args.get('URL')
  linked_from = flask.request.args.get('linkedfrom')
  current_time = str(datetime.now())

  f=open("html/data/redirect.csv", "a+")
  f.write(current_time)
  f.write(",")
  f.write(flask.request.environ.get('HTTP_X_REAL_IP', flask.request.remote_addr)  )
  f.write(",")
  f.write(url)
  f.write(",")
  f.write(linked_from)
  f.write("\n")
  f.close()

  return flask.redirect(url)


@app.route('/ham/')
def ham() :

  my_equipment = {}
  f = open("html/data/ham/my_equipment.json")
  my_equipment = json.load(f)
  f.close
  
  equipment_wishlist = {}
  f = open("html/data/ham/equipment_wishlist.json")
  equipment_wishlist = json.load(f)
  f.close

  return flask.render_template('ham.jinja2', my_equipment=my_equipment, equipment_wishlist=equipment_wishlist)

@app.route('/wishlist/')
def wishlist() :

  wishlist = {}
  f = open("html/data/wishlist.json")
  wishlist = json.load(f)
  f.close

  return flask.render_template('wishlist.jinja2', wishlist=wishlist)

@app.route('/21bday/')
def twentyonebday() :
  return flask.render_template('21bday.jinja2')

if __name__ == '__main__' :
    app.run(host='::', port=80, debug=False)
