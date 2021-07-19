"""
Ciaran Farley

Webserver for www.cturtle98.com/wishlist/
"""

# import the web server
from webpy import app

# imports for this page
import flask
import json

@app.route('/wishlist/')
def wishlist() :

  wishlist = {}
  f = open("/array/www/webpy/webpy/data/wishlist.json", encoding='utf-8')
  wishlist = json.load(f)
  f.close
  
  wishlist_keys = sorted(wishlist.keys(), reverse=True, key=lambda x: wishlist[x]["want"] )

  return flask.render_template('wishlist.jinja2', wishlist=wishlist, wishlist_keys=wishlist_keys)

