from django.shortcuts import render, HttpResponse

# Create your views here.
def home(req):
    print("i am view function")
    return HttpResponse('This is home page')


