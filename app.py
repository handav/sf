# -*- coding: utf-8 -*-
import os, re

import random
import time

# Retrieve Flask, our framework
# request module gives access to incoming request data
from flask import Flask, request, render_template, redirect, abort, flash
from flask import render_template

from mongoengine import *
from models import *

connect('mydatabase', host=os.environ.get('MONGOLAB_URI'))

# create the Flask app
app = Flask(__name__)
app.secret_key='some secret'

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
		story.title=request.form.get('title',None)
		story.date=request.form.get('date', None)
		story.age=request.form.get('age',None)
		story.neighborhood=request.form.get('neighborhood', None)
		story.race=request.form.get('race', None)
		story.text=request.form.get('text', None)
		story.mid=int(time.time())
		story.save()
		
		# flash here http://flask.pocoo.org/docs/tutorial/views/		
		flash("Story submitted!", "submitFlash")
		return redirect('/addstory')
			
	templateData['title'] = PROJECTNAME + "- Add Story"		
	templateData['welcomeMessage'] = "Add Your Story"
	templateData['welcomeDescription'] = "Fill out the form below with information about what happened."
	templateData['form'] = story_form #passing story_form with / without previously submitted form data.
		
	return render_template('addstory.html', **templateData)


@app.route("/storypage/<int:mid>")
def storypage(mid):
	story=False
	for m in Story.objects:
		if mid==m.mid:
			story=m			
	templateData={}
	templateData['title'] = PROJECTNAME + " - " + movie.name
	templateData['welcomeMessage'] = movie.name
	templateData['welcomeDescription'] = movie.description
	return render_template('storypage.html', **templateData)
	

@app.route("/search")
def search():
	query=request.args.get('query','')
	#logger.error('---test in test!')
	templateData={}
	matches = []
	for m in Story.objects:
		app.logger.debug(m)
		for field in [m.text, m.neighborhood, m.date, m.title, m.race]:
			if query.lower() in field.lower():
				matches.append(m)
		#if query.lower() in m.text.lower() or if query.lower() in m.neighrborhood.lower():			
	templateData['matches']=matches
	templateData['title'] = PROJECTNAME + "- Search"
	templateData['welcomeMessage'] = "Search Results"
	templateData['welcomeDescription'] = "Searching for '" + query + "'"
 	return render_template('search.html', **templateData)
 
@app.route("/allstories")
def viewstories():
	templateData={}
	matches = []
	for m in Story.objects:
		matches.append(m)
	templateData['matches']=matches
	templateData['title'] = PROJECTNAME + " - All Stories"
	templateData['welcomeMessage'] = "All Stories"
	templateData['welcomeDescription'] = ""
	return render_template('allstories.html', **templateData)
	

	

# start the webserver
if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)