
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addStudent/$', views.addStudent, name='addStudent'),
    url(r'^addCourse/$', views.addCourse, name='addCourse'),
    url(r'^renderEnrolStudent/$', views.renderEnrolStudent, name='renderEnrolStudent'),
    url(r'^enrollStudent/$', views.enrollStudent, name='enrollStudent'),
    url(r'^renderawardgrade/$', views.renderawardgrade, name='renderawardgrade'),
    url(r'^Awardgrade/$', views.Awardgrade, name='Awardgrade'),
    url(r'^computeGpa/$', views.computeGpa, name='computeGpa'),
    url(r'^generateTranscript/$', views.generateTranscript, name='generateTranscript'),
]
