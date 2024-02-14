from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .form.form_post import SignupForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account Created Successfully!!")
            form.save()
    else:
        form= SignupForm()
    return render(request, 'enroll/signup.html', {'form':form})