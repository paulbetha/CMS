from django.db import models
# Create your models here.
class Student(models.Model):
	Student_Name=models.CharField(max_length=200)

class Course(models.Model):
	Course_Name=models.CharField(max_length=200)
	Credits=models.IntegerField(default=0)

class Enrollement(models.Model):
	Student_Name=models.CharField(max_length=200)
	Course_Name=models.CharField(max_length=200)
	Grade_Points=models.IntegerField(default=0)
	
class Student(ndb.Model):
    """Sub model for storing user activity."""
    Student_Name= ndb.StringProperty(indexed=True)
    emailid = ndb.StringProperty(indexed=True)
    time=ndb.DateTimeProperty(auto_now=True)

class Course(ndb.Model):
    """Sub model for storing course details."""
    Course_Name= ndb.StringProperty(indexed=True)
    Credits = ndb.IntegerProperty(indexed = True)
    time=ndb.DateTimeProperty(auto_now=True)

class Enrollement(ndb.Model):
	"""Sub model for storing enrolled  details."""
	Student_Name= ndb.StringProperty(indexed=True)
	Course_Name= ndb.StringProperty(indexed=True)
	Grade_Points = ndb.IntegerProperty(indexed = True)
	time=ndb.DateTimeProperty(auto_now=True)