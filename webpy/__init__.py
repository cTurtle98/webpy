"""
Ciaran Farley
webapp to host www.cturtle98.com
"""
import os
import json
import flask


app = flask.Flask(__name__, template_folder='templates/', static_folder = 'static/')

trusted_proxies = {'127.0.0.1'}

@app.route('/')
def index() :
	return flask.render_template('home.jinja2',)

from webpy import redirect

@app.route('/ham/')
def ham() :

  my_equipment = {}
  f = open("/array/www/webpy/webpy/data/ham/my_equipment.json", encoding='utf-8')
  my_equipment = json.load(f)
  f.close
  
  equipment_wishlist = {}
  f = open("/array/www/webpy/webpy/data/ham/equipment_wishlist.json", encoding='utf-8')
  equipment_wishlist = json.load(f)
  f.close

  return flask.render_template('ham.jinja2', my_equipment=my_equipment, equipment_wishlist=equipment_wishlist)

from webpy import wishlist

@app.route('/21bday/')
def twentyonebday() :
  return flask.render_template('21bday.jinja2')

@app.route('/bwfs/', methods=['GET', 'POST'])
def bwfs() :

  fs = {
    "count" : None,
    "cucumber" : None,
    "watermellon" : None,
    "pinapple" : None,
    "lime" : None
  }

  fs["count"] = flask.request.args.get('FS_count')

  if fs["count"] == None :
    fs["count"] = 15

  fs["count"] = int(fs["count"])

  fs["cucumber"]    = fs["count"] * 3 / 4
  fs["watermellon"] = fs["count"] / 6
  fs["pinapple"]    = fs["count"] * 2 / 8
  fs["lime"]        = fs["count"] * 1 / 4

  return flask.render_template('bwfs_calc.jinja2', fs=fs)

if __name__ == '__main__' :
    app.run(host='::', port=80, debug=False)
