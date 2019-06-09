"""
Ciaran Farley
webapp to host www.cturtle98.com
"""
import os
import json
from flask import Flask, render_template, send_from_directory, request
from datetime import datetime


app = Flask(__name__, template_folder='html/templates/', static_folder = 'html/static')


@app.route('/')
def index() :
	return render_template('home.jinja2',)

@app.route('/redirect/', methods=['GET'])
def redirect():
  url = request.args.get('URL')
  linkedfrom = request.args.get('linkedfrom')

  f=open("html/data/redirect.csv", "a+")
  f.write(datetime)
  f.write(",")
  f.write(url)
  f.write(",")
  f.write(linkedfrom)
  f.write("\n")
  f.close()

  return redirect(url)


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

  return render_template('ham.jinja2', my_equipment=my_equipment, equipment_wishlist=equipment_wishlist)

@app.route('/wishlist/')
def wishlist() :

  wishlist = {}
  f = open("html/data/wishlist.json")
  wishlist = json.load(f)
  f.close

  return render_template('wishlist.jinja2', wishlist=wishlist)

@app.route('/21bday/')
def twentyonebday() :
  return render_template('21bday.jinja2')

if __name__ == '__main__' :
    app.run(host='::', port=80, debug=False)
