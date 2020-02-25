"""

Ciaran Farley

webserver code for my redirection tracking engine
"""

from webpy import app

import flask
from flask import request
from datetime import datetime
import socket


@app.route('/redirect/', methods=['GET'])
def redirectpage():
  url = flask.request.args.get('URL')
  linked_from = flask.request.args.get('linkedfrom')
  current_time = str(datetime.now())

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

