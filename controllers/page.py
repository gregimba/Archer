from flask import Blueprint, render_template
from config import blog_title
import pickle


index = Blueprint('index', __name__,
                        template_folder='templates')

@index.route('/')
def show():
	posts = pickle.load(open("posts.pkl", "rb"))
	return render_template("index.html",blog_title=blog_title,posts=posts)