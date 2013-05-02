from pony.orm import *
from models.post import Post

from flask import Blueprint, render_template

show = Blueprint('show', __name__,
                        template_folder='templates')

@show.route('/show')
def Show():
	db = Database('sqlite', '/Users/grant/Documents/Archer/db.sqlite')
	posts = []
	for post in Post.select():
		posts.append({"id": post.id,
					  "title": post.title,
					  "text": post.text })

	return render_template("list.html",list=posts)