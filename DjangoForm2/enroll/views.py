from django.shortcuts import render
from enroll.forms import StudendRegistration,FormPost, RegdWidget
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def showformdata(request):
    fm= StudendRegistration()
    return render(request, 'enroll/userregd.html', {'form': fm})
def widget(request):
    form= RegdWidget()
    return render(request, 'enroll/widget.html',{"fm":form})
def thankyou(req):
    return render(req,'enroll/success.html')
def form(request):
    if request.method== 'POST':
        frm= FormPost(request.POST)
        if frm.is_valid():
            messages.success(request, "submited Successfully")
            print('formdata',frm)
            print(frm.cleaned_data)
            name= frm.cleaned_data['name']
            # or
            name= request.POST['name']    # itis another way but is not an efficient way as it dont give cleaned data
            email=frm.cleaned_data['email']
            price=frm.cleaned_data['price']
            print(name)
            print(email)
            print(price)
            print('message from post request')
            # way-1
            return render(request, 'enroll/success.html', {'name': name})
            # way-2
            # return HttpResponseRedirect('/success')
    else:
        frm=FormPost()
        print('message from get request')
        
    return render(request, 'enroll/form.html' ,{'frm': frm})
    
