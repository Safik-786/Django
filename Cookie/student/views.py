from django.shortcuts import render, HttpResponse

# Create your views here.

def  defaultfun(request):
    return HttpResponse("<a href='/set'>Set Cookie </a> <br><br><br>  <a href='/get'>Get Cookie </a> <br><br><br> <a href='/del'>Delete Cookie </a>")

def setCookie(request):
    response= render( request,'setcookie.html')
    response.set_cookie('name', 'Safik mahammad')
    return response


def getCookie(request):
    # name= request.COOKIES['name', 'Guest']
    #       or
    name= request.COOKIES.get('name', 'Guest')
    return render( request,'getcookie.html' , {'key':name})

def delCookie(request):
    response= render( request,'delcookie.html')
    response.delete_cookie('name')
    return response



