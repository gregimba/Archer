from pony.orm import *
from models.post import Post

from flask import Blueprint, render_template

index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
@with_transaction
def Show():
	db = Database('sqlite', '/Users/grant/Documents/Archer/db.sqlite')
	posts = []
	for post in Post.select():
		posts.append({"id": post.id,
					  "title": post.title,
					  "text": post.text })

	return render_template("index.html",posts=posts)