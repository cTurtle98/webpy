"""

Ciaran Farley

webserver to host cturtle98.com/ham/

"""

# import the webserver
from webpy import app

# imports for this page
import flask
import json


@app.route('/ham/')
def ham() :

  my_equipment = {}
  f = open("/var/www/webpy/webpy/data/ham/my_equipment.json", encoding='utf-8')
  my_equipment = json.load(f)
  f.close
  
  equipment_wishlist = {}
  f = open("/var/www/webpy/webpy/data/ham/equipment_wishlist.json", encoding='utf-8')
  equipment_wishlist = json.load(f)
  f.close

  return flask.render_template('ham.jinja2', my_equipment=my_equipment, equipment_wishlist=equipment_wishlist)

