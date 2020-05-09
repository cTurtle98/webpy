"""
Webserver for cturtle98.com/game/
Ciaran Farley

"""
#module imports
import flask

#import flask enviroment
from webpy import app

@app.route('/game/ftb-academy/')
def game_ftbacademy():
  return flask.render_template('game_ftb-academy.jinja2')
