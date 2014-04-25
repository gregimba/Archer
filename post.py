import pickle
from datetime import datetime
import click



@click.group()
def cli():
	pass



@click.command()
@click.argument("title")
@click.argument("text")
def create_post(title,text):
	posts = pickle.load(open("posts.pkl", "rb"))
	posts.append({"title":title,"text":text , "date":str(datetime.now())})
	#Dump the archive
	pickle.dump(posts,open("posts.pkl","wb")) 

@click.command()
def initdb():
	posts = []
	pickle.dump(posts,open("posts.pkl","wb"))

cli.add_command(create_post)
cli.add_command(initdb)

if __name__ == '__main__':
	cli()

