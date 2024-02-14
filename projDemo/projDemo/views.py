from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    data={
        'title':"home New",
        "info":" hii i am safik",
        "clist":['php','java','python'],
        'student_details':[
           { "name": 'safik', 'number':'8079877526'},
           { "name": 'rahul', 'number':'9979879526'}
        ],
        "numbers":[23,50,34,86,68,32,26,96,39,91]
    }
    return render(request , "index.html", data)
def aboutus(request):
    return render(request, "about.html")
def course(request):
    return render(request, 'course.html')

# dynammic routing

def courseDetails(request,courseid):
    return HttpResponse(f"Hii this is course -:   {courseid}")