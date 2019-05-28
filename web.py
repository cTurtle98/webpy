"""
Ciaran Farley
webapp to host www.cturtle98.com
"""
import os
import json
from flask import Flask, render_template, send_from_directory


app = Flask(__name__, template_folder='html/templates/', static_folder = 'html/static')


@app.route('/')
def index() :
	return render_template('home.jinja2',)

@app.route('/ham/')
def ham() :

  my_equipment = {}
  equipment_wishlist = {}

  try:
    f = open("html/data/ham/my_equipment.json")
    my_equipment = json.load(f)
    f.close
    f = open("html/data/ham/equipment_wishlist.json")
    equipment_wishlist = json.load(f)
    f.close
  except:
    return("couldn't load data")

    

  return render_template('ham.jinja2', my_equipment=my_equipment, equipment_wishlist=equipment_wishlist)

if __name__ == '__main__' :
    app.run(host='::', port=80, debug=False)
