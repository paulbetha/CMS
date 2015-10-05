from django.db import models
# Create your models here.
class Student(models.Model):
	Student_Name=models.CharField(max_length=200)

class Course(models.Model):
	Course_Name=models.CharField(max_length=200)
	Credits=models.IntegerField(default=0)

class Enrollement(models.Model):
	Student_Name=models.ForeignKey(Student)
	Course_Name=models.ForeignKey(Course)
	Grade_Points=models.IntegerField(default=0)
	
