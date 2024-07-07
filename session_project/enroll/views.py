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
    if 'name' in request.session:
        del request.session['name']
        
    # delete all session
    return render(request, 'delsession.html')

# Small project

def homecounter(request):
    cnt= request.session.get('count', 0)
    newcount= cnt+1
    request.session['count']= newcount
    return render (request, 'pagecounter.html', {'count': newcount})