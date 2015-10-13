from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Course, Enrollement
import json
import cgi
# Create your views here.
""" landing page"""

def index(request):
    return render(request, 'coursemanagement/index.html')


"""addStudent"""
"""will get a json as input format{Student_name:"name" """


def addStudent(request):
    """return HttpResponse("Hello, world. You're at the polls index.")"""
    data = json.loads(request.body)
    response = {}
    if not Student.objects.get(Student_Name=data.Student_name):
        s = Student(Student_Name=data.Student_name).save()
        response['status'] = 'sucess'
    else:
        response['status'] = 'failure'
    json_data = json.dumps(response)
    return HttpResponse(json_data, content_type = "application/json")


"""addCourse"""
"""will get a json as input format{Course_name:"name" """


def addCourse(request):
    data = json.loads(request.body)
    response = {}
    if not Course.objects.get(Student_Name=data.Student_name):
        s = Student(Course_name=data.Course_name, Credits=data.Credits).save()
        response['status'] = 'sucess'
    else:
        response['status'] = 'failure'
    json_data = json.dumps(response)
    return HttpResponse(json_data, content_type = "application/json")


"""renderEnrolStudent"""


def renderEnrolStudent(request):
    enroll = {}
    Student_list = []
    Course_list = []
    students = Student.objects.all()
    Courses = Course.objects.all()
    for s in students:
        std = {"Student_name": s.Student_name}
        Student_list.append(std)
    for c in Courses:
        cs = {"Student_name": s.Student_name}
        Course_list.append(cs)
    enroll["Student_list"] = Student_list
    enroll["Course_list"] = Course_list
    json_data = json.dumps(enroll)
    return HttpResponse(json_data, content_type = "application/json")


"""enrollStudent"""
"""will get a json as input format{Student_name ,Course_name:name }"""


def enrollStudent(request):
    data = json.loads(request.body)
    response = {}
    if Student.objects.get(Student_Name=data.Student_name) and Course.objects.get(Student_Name=data.Student_name):
        e = Enrollement(Student_Name=data.Student_name, Course_name=data.Course_name, Grade_Points=0).save()
        response['status'] = 'sucess'
    else:
        response['status'] = 'failure'
    json_data = json.dumps(response)
    return HttpResponse(json_data, content_type = "application/json")


"""renderawarGrade"""


def renderawardgrade(request):
    enroll = {}
    Student_list = []
    Course_list = []
    students = Student.objects.all()
    Courses = Course.objects.all()
    for s in students:
        std = {"Student_name": s.Student_name}
        Student_list.append(std)
    for c in Courses:
        cs = {"Student_name": s.Student_name}
        Course_list.append(cs)
    enroll["Student_list"] = Student_list
    enroll["Course_list"] = Course_list
    json_data = json.dumps(enroll)
    return HttpResponse(json_data, content_type = "application/json")


"""Awardgrade"""
"""will get a json as input format{Student_name, Course_name ,Grade_points} """


def Awardgrade(request):
    data = json.loads(request.body)
    response = {}
    if Student.objects.get(Student_Name=data.Student_name) and Course.objects.get(Course_Name=data.Course_name):
        e = Enrollement.objects.get(Student_Name=data.Student_name, Course_Name=data.Course_name)
        e.Grade_Points = data.Grade_points
        e.save()
        response['status'] = 'sucess'
    else:
        response['status'] = 'failure'
    json_data = json.dumps(response)
    return HttpResponse(json_data, content_type = "application/json")


"""computeGpa"""


def computeGpa(request):
    students = Student.objects.all()
    enroll = Enrollement.objects.all()
    sum = 0
    t_credits = 0
    for s in students:
        for e in enroll:
            if s.Student_Name == e.Student_Name:
                c = Course.objects.get(Course_Name=e.Course_Name)
                sum = sum + (e.Grade_Points * c.Credits)
                t_credits = t_credits + c.Credits
        gpavg = sum / t_credits
        s.Grade_points_avg = gpavg
        s.save()


"""generateTranscript"""
""" will get input as json file as {Student_Name:Student_name}"""


def generateTranscript(request):
    data = json.loads(request.body)
    transcript = {}
    Course_list = []
    student = Student.objects.get(Student_Name=data.Student_name)
    enroll = Enrollement.objects.all()
    for e in enroll:
        if student.Student_Name == e.Student_Name:
            c = Course.objects.get(Course_Name=e.Course_Name)
            Course_details = {"Course_Name": c.Course_Name, "Grade_points": c.Grade_Points}
            Course_list.append(Course_details)
    transcript["Student_Name"] = student.Student_Name
    transcript["Course_list"] = Course_list
    transcript["gpa"] = student.Grade_points_avg
    json_data = json.dumps(transcript)
    return HttpResponse(json_data, content_type = "application/json")
