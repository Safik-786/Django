from django.urls import path
from . import views

urlpatterns = [
    path("",views.form),
    path("select/",views.userRegd),
    path("student/",views.studentRegd),
    path("teacher/",views.teacherRegd),
    path("message/",views.registrationMsg),
]
