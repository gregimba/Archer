import pickle


posts = []
#create your posts here
hello = {"title" : "Hello, World","text" : "This is a test post don't be alarmed"}
goodbye = {"title": "Goodbye, World","text":"This is a goodbye post, Goodbye"}

#end posts append them here
posts.append(hello)
posts.append(goodbye)

#Dump the archive
pickle.dump(posts,open("posts.pkl","wb"))