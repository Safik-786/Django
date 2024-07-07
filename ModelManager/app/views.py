from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    stud= Student.objects.all()
    stud_ord= Student.students.all()
    return render(request, "home.html", { 'student': stud , 'stu_ord': stud_ord})

