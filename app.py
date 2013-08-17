#Vodka Imports
from flask import Flask, render_template
from flask.ext.restful import Resource, Api
from pony.orm import *

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config.cfg')
db = Database('sqlite', '/Users/grant/Documents/Archer/db.sqlite')

#controllers imports
from controllers.index import Index

api.add_resource(Index,'/')

if __name__ == '__main__':
	app.run()