from django.shortcuts import render

# Create your views here.
def fees(req):
    return render(req, 'fees.html')
