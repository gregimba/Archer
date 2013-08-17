from user import User
from datetime import date
from pony.orm import *

db = Database('sqlite', ':memory:')


class Post(db.Entity):
	"""All posts are stored in this table"""
	id = PrimaryKey(int, auto=True)
	author = Required(User)
	title = Required(unicode)
	text = Required(unicodelong)
	date = Required(date)

db.generate_mapping(create_tables=True)
user = User(name='grant',email='grant@gregimba.com',)