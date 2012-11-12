# -*- coding: utf-8 -*-
import os, re

#import random
#import time

# Retrieve Flask, our framework
# request module gives access to incoming request data
from flask import Flask, request, render_template, redirect, abort, flash
#from flask import render_template

#from mongoengine import *
#from models import *

#connect('mydatabase', host=os.environ.get('MONGOLAB_URI'))

# create the Flask app
app = Flask(__name__)
#app.secret_key='some secret'

# global variables
PROJECTNAME = "Stop Stories"

@app.route("/")	
def index():
	templateData={}
	templateData['title'] = PROJECTNAME + "- Home"
	templateData['welcomeMessage'] = "Welcome to Stop Stories!"
	templateData['welcomeDescription'] = "Gathering the stories of Stop and Frisk."		
	#templateData['displayMovies']=random.sample(Movie.objects,3)
	return render_template('home.html',**templateData)
	
@app.route("/addstory", methods=["GET","POST"])
def addstory():
 	templateData={}
 	
 	#take incoming form data and generate wtform object
 	story_form = StoryForm(request.form)
 	
	if request.method == "POST" and story_form.validate():
		story=Story()
		story.date=request.form.get('date', None)
		story.age=request.form.get('age',None)
		story.neighborhood=request.form.get('neighborhood', None)
		story.race=request.form.get('race', None)
		story.mid=int(time.time())
		story.save()
		
		# flash here http://flask.pocoo.org/docs/tutorial/views/		
		flash("Story submitted!", "submitFlash")
		return redirect('/addstory')
			
	templateData['title'] = PROJECTNAME + "- Add Story"		
	templateData['welcomeMessage'] = "Add Your Story"
	templateData['welcomeDescription'] = "Fill out the form below with information about what happened."
	templateData['form'] = story_form #passing movie_form with / without previously submitted form data.
		
	return render_template('addstory.html', **templateData)


# @app.route("/addreview")
# def addreview():
# 	templateData={}
# 	templateData['title'] = PROJECTNAME + "- Add Review"
# 	templateData['welcomeMessage'] = "Add Your Rating And Review"
# 	templateData['welcomeDescription'] = "Add a review to" + mid + "in the form below."
# 	return render_template('addreview.html', **templateData)
# 	
# 	
# @app.route("/moviepage/<int:mid>")
# def moviepage(mid):
# 	movie=False
# 	for m in Movie.objects:
# 		if mid==m.mid:
# 			movie=m
# 				
# 	templateData={}
# 	templateData['title'] = PROJECTNAME + " - " + movie.name
# 	templateData['welcomeMessage'] = movie.name
# 	templateData['welcomeDescription'] = movie.description
# 	return render_template('moviepage.html', **templateData)
# 	
# 	
# @app.route("/search")
# def search():
# 	query=request.args.get('query','')
# 	templateData={}
# 	matches = []
# 	for m in Movie.objects:
# 		if query.lower() in m.description.lower() or query.lower() in m.name.lower() or query.lower() in m.director.lower() or query.lower() in m.year.lower() or query.lower() in m.genre.lower():
# 			matches.append(m)
# 	templateData['matches']=matches
# 
# 	templateData['title'] = PROJECTNAME + "- Search"
# 	templateData['welcomeMessage'] = "Search Results"
# 	templateData['welcomeDescription'] = "Searching for '" + query + "'"
# 	return render_template('search.html', **templateData)
	

# start the webserver
if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)