from flask import Flask, render_template

app = Flask(__name__)

from controllers.index import index
app.register_blueprint(index)

if __name__ == '__main__':
	app.debug = True
	app.run()
