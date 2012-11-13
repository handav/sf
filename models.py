# -*- coding: utf-8 -*-
from mongoengine import *

from flask.ext.mongoengine.wtf import model_form
from datetime import datetime


# class Review(EmbeddedDocument):
# 	rating = IntField()
# 	text = StringField()
# 	submitterName = StringField()
# 	timestamp = DateTimeField(default=datetime.now())
	
#mongoengine document
class Story(Document):
	title=StringField(required=False,verbose_name="Title")
	date = StringField(required=True, verbose_name="Date")
	age = IntField(required=False, verbose_name="Age")
	race = StringField(required=False, verbose_name="Race")
	neighborhood = StringField(required=True, verbose_name="Neighborhood")
	#figure out what a large text box is called in mongoengine and see if it converts to wtform.
	text = StringField(required=True, verbose_name="Story")
	mid = IntField(required=False)
	#reviews = ListField(EmbeddedDocumentField(Review))

# wt form purposes: validation object + display tool
StoryForm = model_form(Story)



	


