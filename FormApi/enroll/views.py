from django.shortcuts import render
from enroll.forms import FormPost, StudRegestration ,StudentRegistration, TeacherRegistration
from .models import User
from django.contrib import messages
# Create your views here.

def form(request):
    if request.method=='POST':
        frm= FormPost(request.POST)
        if frm.is_valid():
            # print(frm)
            print(frm.cleaned_data)
            
            nm= frm.cleaned_data['name']
            em= frm.cleaned_data['email']
            ps= frm.cleaned_data['password']
            # reg =User(id=2,name=nm, email=em, password=ps)
            # reg.save()
            delete= User(id=1)
            delete.delete()
    else:
        frm=FormPost()
        print('message from get request')
        
    return render(request, 'enroll/form.html' ,{'frm': frm})

def userRegd(req):
    fm = StudRegestration()
    return render(req, 'enroll/userRegistration.html', {'form':fm})
    
def studentRegd(req):
    if req.method== 'POST':
        fm= StudentRegistration(req.POST)
        if fm.is_valid():
            fm.save()
            fm= StudentRegistration()
    else :
        fm= StudentRegistration()
    return render(req, 'enroll/student.html', {'form':fm})
def teacherRegd(req):
    if req.method== 'POST':
        fm= TeacherRegistration(req.POST)
        if fm.is_valid():
            fm.save()
            fm= TeacherRegistration()
    else :
        fm= TeacherRegistration()
    return render(req, 'enroll/teacher.html', {'form':fm})

def registrationMsg(request):
    messages.info(request, "this is information")
    messages.warning(request, "this is Warning")
    messages.error(request, "this is Error")
    messages.success(request, "this is Success")
    if request.method=='POST':
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save();
            # messages.add_message(request, messages.SUCCESS ,"Data Saved Succesfully...")
            messages.success(request, "Data Saved Succesfully...")
            fm= StudentRegistration()
            
    else:
        fm= StudentRegistration()
        
    return render(request, 'enroll/userMsg.html', {'form':fm})
        
        
