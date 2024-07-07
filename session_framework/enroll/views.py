from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='safik Mahammad'
    request.session['email']='ytsafik2@gmail.com'
    return render(request, 'setsession.html')
def getsession(request):
    # name= request.session['name']
    name= request.session.get('name', default='guest')
    email= request.session.get('email', default='guest')
    age= request.session.setdefault('age', '21')
    
    return render(request, 'getsession.html', {'key':name, 'key2':email, 'age':age})
def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        
    # delete all session
    request.session.flush()

    return render(request, 'delsession.html')