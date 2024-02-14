from django.shortcuts import render, HttpResponseRedirect
from .forms import Studentregd
from .models import User


# Add and show data 
def AddShow(request):
    if request.method == 'POST' :
        fm= Studentregd(request.POST)
        if fm.is_valid():
            name= fm.cleaned_data['name']
            email= fm.cleaned_data['email']
            password= fm.cleaned_data['password']
            reg= User(name=name, email=email, password= password)
            reg.save()
            fm= Studentregd()
        fm= Studentregd()
            
    else:
        fm= Studentregd()
        
    stud= User.objects.all()
        
        
    return render(request, 'enroll/add&show.html', {'form':fm, 'stud':stud})

# delete data
def deleteData(request, id):
    if request.method=='POST':
        delt= User.objects.get(pk=id)
        delt.delete();
    return HttpResponseRedirect('/')


# Update or Edit
def update(request, id):
    if request.method == 'POST':
        data= User.objects.get(pk= id)
        fm=Studentregd(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
            fm=Studentregd()
    else:
        data= User.objects.get(pk= id)
        fm=Studentregd(instance=data) 
    return render(request, 'enroll/updateStudent.html', { 'form':fm})