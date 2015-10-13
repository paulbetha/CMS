#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import cgi
import traceback
import json
import jinja2
import webapp2
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp.util import run_wsgi_app
from pprint import pprint
import datetime
from datetime import datetime


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

""" database models """

class Student(ndb.Model):
    """Sub model for storing user activity."""
    Student_Name= ndb.StringProperty(indexed=True)
    emailid = ndb.StringProperty(indexed=True)
    Grade_points_avg = ndb.IntegerProperty(indexed = True)
    time=ndb.DateTimeProperty(auto_now=True)

class Course(ndb.Model):
    """Sub model for storing course details."""
    Course_Name= ndb.StringProperty(indexed=True)
    Course_Credits = ndb.IntegerProperty(indexed = True)
    time=ndb.DateTimeProperty(auto_now=True)

class Enrollement(ndb.Model):
	"""Sub model for storing enrolled  details."""
	Student_Name= ndb.StringProperty(indexed=True)
	Course_Name= ndb.StringProperty(indexed=True)
	Grade_Points = ndb.IntegerProperty(indexed = True)
	time=ndb.DateTimeProperty(auto_now=True)



class homepage(webapp2.RequestHandler):
    """  handles rendering of index page """
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

"""addStudent"""
"""will get a json as input format{Student_name:"name" """

class addStudent(webapp2.RequestHandler):
    def post(self):
	    vals = json.loads(cgi.escape(self.request.body))
	    Student_name=vals['Student_name']
	    response = {}
	    if Student.query(Student.Student_Name==Student_name).get() is None :
	        s = Student(Student_Name=Student_name).put()
	        response['status'] = 'sucess'
	    else:
	        response['status'] = 'failure'
	    ss=json.dumps(response)
	    self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
	    self.response.write(ss)


"""addCourse"""
"""will get a json as input format{Course_name:"name" """

class addCourse(webapp2.RequestHandler):
	def post(self):
		vals = json.loads(cgi.escape(self.request.body))
		Course_name=vals['Course_name']
	   	Credits=vals['Course_credits']
		response = {}
		if Course.query(Course.Course_Name==Course_name).get() is None :
		    s = Course(Course_Name=Course_name,Course_Credits=int(Credits)).put()
		    response['status'] = 'sucess'
		else:
		    response['status'] = 'failure'
		ss=json.dumps(response)
		self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
		self.response.write(ss)	

"""renderEnrolStudent"""

class renderEnrolStudent(webapp2.RequestHandler):
	def post(self):
		enroll = {}
		Student_list = []
		Course_list = []
		students = Student.query()
		Courses = Course.query()
		for s in students:
			std = {"Student_name": s.Student_Name}
			Student_list.append(std)
		for c in Courses:
			cs = {"Course_name": c.Course_Name}
			Course_list.append(cs)
		enroll["Student_list"] = Student_list
		enroll["Course_list"] = Course_list
		ss=json.dumps(enroll)
		self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
		self.response.write(ss)
class enrollStudent(webapp2.RequestHandler):
	def post(self):
		response = {}
		vals = json.loads(cgi.escape(self.request.body))
		Course_name=vals['Course_name']
	   	Student_name=vals['Student_name']
	   	if Student.query(Student.Student_Name==Student_name).get() and Course.query(Course.Course_Name==Course_name).get():
	   		e = Enrollement(Student_Name=Student_name, Course_Name=Course_name, Grade_Points=0).put()
			response['status'] = 'sucess'
		else:
			response['status'] = 'failure'
		ss=json.dumps(response)
		self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
		self.response.write(ss)
class Awardgrade(webapp2.RequestHandler):
	def post(self):
		response = {}
		vals = json.loads(cgi.escape(self.request.body))
		Course_name=vals['Course_name']
	   	Student_name=vals['Student_name']
	   	grade=vals['grade']
	   	if Student.query(Student.Student_Name==Student_name).get() and Course.query(Course.Course_Name==Course_name).get() and Enrollement.query(Enrollement.Course_Name==Course_name, Enrollement.Student_Name==Student_name):
	   		e = Enrollement(Student_Name=Student_name, Course_Name=Course_name, Grade_Points=int(grade)).put()
			response['status'] = 'sucess'
		else:
			response['status'] = 'failure'
		ss=json.dumps(response)
		self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
		self.response.write(ss)
class computeGpa(webapp2.RequestHandler):
	def post(self):
		students = Student.query()
		enroll = Enrollement.query()
		sum = 0
		t_credits = 0
		for s in students:
			for e in enroll:
			    if s.Student_Name == e.Student_Name:
			        c = Course.query(Course.Course_Name==e.Course_Name).get()
			        sum = sum + (e.Grade_Points * c.Credits)
			        t_credits = t_credits + c.Credits
		gpavg = sum / t_credits
		print(gpavg,"submiteddfdf")
		logging.error("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		print(gpavg,"submiteddfdf")
		s.Grade_points_avg = gpavg
		print 
		s.put()
class rendertranscript(webapp2.RequestHandler):
	def post(self):
		students = Student.query()
		enroll = {}
		Student_list = []
		for s in students:
			std = {"Student_name": s.Student_Name}
			Student_list.append(std)
		enroll["Student_list"] = Student_list
		ss=json.dumps(enroll)
		self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
		self.response.write(ss)

class generateTranscript(webapp2.RequestHandler):
	def post(self):
		vals = json.loads(cgi.escape(self.request.body))
		Student_name=vals['Student_name']
		transcript = {}
		Course_list = []
		student=Student.query(Student.Student_Name==Student_name).get()
		enroll = Enrollement.query()
		for e in enroll:
		   if student.Student_Name == e.Student_Name:
				c = Course.query(Course.Course_Name==e.Course_Name).get()
				Course_details = {"Course_Name": c.Course_Name, "Course_Credits": c.Course_Credits}
				Course_list.append(Course_details)
				transcript["Student_Name"] = student.Student_Name
		transcript["Course_list"] = Course_list
		transcript["gpa"] = student.Grade_points_avg
		ss=json.dumps(transcript)
		self.response.headers.add_header('content-type', 'application/json', charset='utf-8')
		self.response.write(ss)

application = webapp2.WSGIApplication([
    ('/', homepage),
    ('/addStudent',addStudent),
    ('/addCourse',addCourse),
    ('/renderEnrolStudent',renderEnrolStudent),
    ('/enrollStudent',enrollStudent),
    ('/Awardgrade',Awardgrade),
    ('/computeGpa',computeGpa),
    ('/rendertranscript',rendertranscript),
    ('/generateTranscript',generateTranscript)
], debug=True)
