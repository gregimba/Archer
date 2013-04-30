from pony.orm import *

from models.post import Post

from flask import Blueprint, render_template, request

new = Blueprint('new', __name__,
                        template_folder='templates')

@new.route('/new', methods=['GET', 'POST'])
def New():
	db = Database('sqlite', '/Users/grant/Documents/Flaskr/db.sqlite')

	if request.method == 'POST':
		newPost = Post(title=request.form['title'],text=request.form['text'])
		commit()
		return render_template("new.html")
	else:
		return render_template("new.html")