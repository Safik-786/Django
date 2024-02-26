from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth.models import User, Group
from . import forms


def homepage(request):
    postdata= Post.objects.all()
    return render(request, 'blog/home.html', {'data':postdata})
def aboutpage(request):
    return render(request, 'blog/about.html')
def contactpage(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts= Post.objects.all()
        fullname= request.user.get_full_name()
        user= User.objects.filter(username= request.user)
        print(user)
        return render(request, 'blog/dashboard.html', {'post':posts, 'user':user, 'fullname':fullname} )
    else:
        return HttpResponseRedirect('/login/')

def signup(request):
    if request.method== 'POST':
        fm= forms.SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Congratulation! You are now Author😎')
            user= fm.save()
            group= Group.objects.get(name='Author')
            user.groups.add(group)
            fm= forms.SignupForm()
            return HttpResponseRedirect('/login/')
    else:
        fm= forms.SignupForm()
    return render(request, 'blog/signup.html', {'form':fm})

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method== 'POST':
            fm= forms.LoginForm(request=request,  data=request.POST)
            if fm.is_valid():
                uname= fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                user= authenticate(username= uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully ')
                    return HttpResponseRedirect('/dashboard/')
        else:  
            fm= forms.LoginForm()
        return render(request, 'blog/login.html', {'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/login/")

# Add New Post
def addpost(request):
    if  request.user.is_authenticated:
        if request.method== 'POST':
            fm= PostForm(request.POST)
            if fm.is_valid():
                messages.success(request, "Blog Posted Successfully😎")
                fm.save()
                fm=PostForm()
        else:
            fm=PostForm()
        return render(request, 'blog/addpost.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
# Update the existing post
def updatepost(request, id):
    if  request.user.is_authenticated:
        if request.method=='POST':
            data= Post.objects.get(pk=id)
            fm= PostForm(request.POST, instance=data)
            if fm.is_valid():
                messages.success(request, "Blog Updated Successfully😎")
                fm.save()
                return HttpResponseRedirect('/dashboard/')
        data= Post.objects.get(pk=id)
        fm= PostForm(instance=data)
        return render(request, 'blog/updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
# Delete the existing post
def deletepost(request, id):
    if  request.user.is_authenticated:
        if request.method=='POST':
            datafordelete= Post.objects.get(pk=id) 
            datafordelete.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
    
    
def editprofile(request , id):
    if  request.user.is_authenticated:
        if request.method=='POST':
            data= User.objects.get(pk=id)
            fm= forms.EditUserProfileForm(request.POST, instance= data)
            if fm.is_valid():
                messages.success(request, "Profile Updated Successfully")
                fm.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            data= User.objects.get(pk=id)
            fm= forms.EditUserProfileForm(instance=data)
        return render(request, 'blog/editprofile.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')

    