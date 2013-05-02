#Flask Imports
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

#Blueprint imports
from controllers.index import index
app.register_blueprint(index)

from controllers.show import show
app.register_blueprint(show)

from controllers.new import new
app.register_blueprint(new)

#Pony ORM
from pony.orm import *
db = Database('sqlite', '/Users/grant/Documents/Archer/db.sqlite',create_db=True)
from models.post import Post



if __name__ == '__main__':
	app.run()