from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Signup/ register view function
def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account Created Successfully!!")
            form.save()
    else:
        form= UserCreationForm()
    return render(request, 'signup.html', {'form':form})

# Login
def userLogin(request):
   
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=AuthenticationForm(request=request,  data= request.POST)
            if form.is_valid():
                username= form.cleaned_data['username']
                userpass= form.cleaned_data['password']
                user= authenticate(username=username, password=userpass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login Successfully!!")
                    return HttpResponseRedirect('/profile/')
                form=AuthenticationForm()
        else:
            form= AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/profile/')

# profile

def userprofile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else :
        return HttpResponseRedirect("/login/")


# logout
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# change password with old password
@login_required
def userChangePass(request):
    if request.user.is_authenticated:
        if request.method== 'POST':
            fm= PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Change Successfully')
                return HttpResponseRedirect('/profile/')
            
        else:
            fm= PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')