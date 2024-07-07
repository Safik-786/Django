from django.shortcuts import render, HttpResponse

# Create your views here.
def setsession(request):
    request.session['name']='safik Mahammad'
    request.session['email']='ytsafik2@gmail.com'
    return render(request, 'setsession.html')
def getsession(request):
    # name= request.session['name']
    if 'name' in request.session:
        request.session.modified=True
        name= request.session.get('name', default='guest')
        email= request.session.get('email', default='guest')
        age= request.session.setdefault('age', '21')
        return render(request, 'getsession.html', {'key':name, 'key2':email, 'age':age})
    else:
         return HttpResponse('Your Session has expired')
def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    # delete all session
    return render(request, 'delsession.html')

