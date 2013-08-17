from pony.orm import *
db = Database('sqlite', ':memory:')

class User(db.Entity):
	"""All posts are stored in this table"""
	id = PrimaryKey(int, auto=True)
	name = Required(unicode)
	email = Required(unicode)
	posts = Set("Post")