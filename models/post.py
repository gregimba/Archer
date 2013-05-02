from pony.orm import *

db = Database('sqlite', '/Users/grant/Documents/Archer/db.sqlite')

class Post(db.Entity):
	"""The class that all posts are created from"""
	title = Required(unicode)
	text = Required(unicode)

db.generate_mapping(create_tables=True)