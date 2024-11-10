from django.shortcuts import render
# importing httpp response for django
from  django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse('hello  this is the introduction to django by cs50')
    
def Alex(request):
    return HttpResponse('my name is Alex and i am practising  django at this level')
    pass
# greet globally
def greet(request,name):
    return HttpResponse(f'hello  and  me {name}')
    pass
 # lets start rendering requests
def all(request):
    return render(request,"hello/index.html")
    pass
# creating views that utilizes context
def helloThere(request,name):
    return render(request,"hello/greeting.html",{"name":name.Capitalize()})

def ourName(request,name):
     return render(request,"hello/h.html",{"name":name.upper()})
    