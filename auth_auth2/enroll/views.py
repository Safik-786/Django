from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User


# Signup/ register view function
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=SignupForm(request.POST)
            if form.is_valid():
                messages.success(request, "Account Created Successfully!!")
                form=SignupForm()
                form.save()
        else:
            form= SignupForm()
        return render(request, 'signup.html', {'form':form})
    else:
        return HttpResponseRedirect('/profile/')
    

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
        if request.method == 'POST':
            if request.user.is_superuser:
                fm= EditAdminProfileForm(request.POST, instance=request.user)
                users= User.objects.all()
            else:
                fm= EditUserProfileForm(request.POST, instance=request.user)
                users=None
            if fm.is_valid():
                messages.success(request, 'Profile Updated Successfully..')
                fm.save()
        else:
            if request.user.is_superuser:
                fm= EditAdminProfileForm(instance= request.user)
                users= User.objects.all()
            else:
                fm= EditUserProfileForm(instance= request.user)
                users=None;
        return render(request, 'profile.html' ,{'form':fm, 'users':users})
    else :
        return HttpResponseRedirect("/login/")


# logout
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# change password with old password
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
    
def userDetail(request, id):
    if request.user.is_authenticated:
        pi= User.objects.get(pk= id)
        fm= EditAdminProfileForm(instance= pi)
        return render(request, 'userdetail.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')