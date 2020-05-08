"""
Webserver for cturtle98.com/game/
Ciaran Farley

"""
#module imports
import flask

#import flask enviroment
from webpy import app

@app.route('/game/ftb-academy/')
def ftb-academy():
  return flask.render_template('game_ftb-academy.jinja2')
