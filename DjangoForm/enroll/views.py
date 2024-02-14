from django.shortcuts import render
from enroll.forms import StudendRegistration, StudRegd

# Create your views here.

def showformdata(request):
    fm= StudendRegistration()
    return render(request, 'enroll/userregd.html', {'form': fm})
def userdata(request):
    if request.method== 'POST':
        frm= StudRegd(request.POST)
        print('Successssssssss')
        if frm.is_valid() :
            print('Success')
            print('Name:',frm.cleaned_data['name']) 
            name= frm.cleaned_data['name']
            print('Email:',frm.cleaned_data['email']) 
            print('Password:',frm.cleaned_data['password']) 
            
            return render(request, 'enroll/error.html', {'name':name})
    else:
        frm=StudRegd()
        if frm.is_valid() :
            print(frm.cleaned_data)

    return render(request, 'enroll/error.html', {'form':frm})
    
