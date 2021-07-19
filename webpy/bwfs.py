"""

Ciaran Farley

cturtle98.com/bwfs/
BoardWalk Food Service
webserver custom calculator

"""

from webpy import app

import flask

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
