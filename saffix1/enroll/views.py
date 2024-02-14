from django.shortcuts import render

# Create your views here.
from enroll.models import Student
def studinfo(request):
    stud= Student.objects.all()
    # stud= Student.objects.get(pk=2)
    return render (request, 'enroll/studetails.html', {'stu': stud})
