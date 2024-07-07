from django.shortcuts import render

# Create your views here.
def course(req):
    return render(req, 'course.html')
def home(req):
    return render(req, 'home.html')