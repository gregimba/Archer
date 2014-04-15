import pickle
import datetime


posts = []
#create your posts here
hello = {"title" : "Hello, World","text" : "This is a test post don't be alarmed","date": datetime.date(2014,4,14)}
goodbye = {"title": "Goodbye, World","text":"This is a goodbye post, Goodbye","date": datetime.date(2014,4,14)}

#end posts append them here
posts.append(hello)
posts.append(goodbye)

#Dump the archive
pickle.dump(posts,open("posts.pkl","wb"))