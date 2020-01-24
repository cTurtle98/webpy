"""
Ciaran Farley
webapp to host www.cturtle98.com
"""
import os
import json
import flask
from flask import request
from datetime import datetime
import socket


app = flask.Flask(__name__, template_folder='templates/', static_folder = 'static/')

trusted_proxies = {'127.0.0.1'}

@app.route('/')
def index() :
	return flask.render_template('home.jinja2',)

@app.route('/redirect/', methods=['GET'])
def redirectpage():
  url = flask.request.args.get('URL')
  linked_from = flask.request.args.get('linkedfrom')
  current_time = str(datetime.now())
  
  #fix for request.remote_addr not working
  # no longer needed
#  route = request.access_route + [request.remote_addr]
#  remote_addr = next((addr for addr in reversed(route) 
#                    if addr not in trusted_proxies), request.remote_addr)

  f=open("/array/www/webpy/webpy/data/redirect.csv", "a+", encoding='utf-8')
  f.write(current_time)
  f.write(",")
  f.write(request.remote_addr )
  f.write(",")
  
  try:
    f.write(socket.gethostbyaddr(request.remote_addr))
    f.write(",")
  except:
    f.write("no host name")
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
  f = open("/array/www/webpy/webpy/data/ham/my_equipment.json", encoding='utf-8')
  my_equipment = json.load(f)
  f.close
  
  equipment_wishlist = {}
  f = open("/array/www/webpy/webpy/data/ham/equipment_wishlist.json", encoding='utf-8')
  equipment_wishlist = json.load(f)
  f.close

  return flask.render_template('ham.jinja2', my_equipment=my_equipment, equipment_wishlist=equipment_wishlist)

@app.route('/wishlist/')
def wishlist() :

  wishlist = {}
  f = open("/array/www/webpy/webpy/data/wishlist.json", encoding='utf-8')
  wishlist = json.load(f)
  f.close
  
  wishlist_keys = sorted(wishlist.keys(), reverse=True, key=lambda x: wishlist[x]["want"] )

  return flask.render_template('wishlist.jinja2', wishlist=wishlist, wishlist_keys=wishlist_keys)

@app.route('/21bday/')
def twentyonebday() :
  return flask.render_template('21bday.jinja2')

if __name__ == '__main__' :
    app.run(host='::', port=80, debug=False)
