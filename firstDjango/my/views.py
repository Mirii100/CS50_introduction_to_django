from django.shortcuts import render
from .models import Destination
# Create your views here.

def nav(request):
    return render(request,"index.html",{})

def login(request):
    return render(request,"login.html")

def add(request):
    var1=int(request.POST['num1'])
    var2=int(request.POST["num2"])
    res=var1 + var2
    return render(request,"practice.html",     {"result":res })
def service(request):
    return render(request,"portfolio-details.html")


def services(request):
    return render(request,"service-details.html")

def about(request):
    return render(request,"about.html")

def resume(request):
    return render(request,"resume.html")
def contactUs(request):
    return render(request,"contact.html")
def start(request):
    return render(request,"starter-page.html")

def gallary(request):
    dest1=Destination() 
    dest1.price=10
    dest1.name='Alex'
    dest1.img='gallery-1.jpg'
    dest2=Destination()
    dest2.name="Njuguna"
    dest2.price=30
    dest2.img='hero.jpg'
    dest3=Destination() 
    dest3.price=20
    dest3.name='Mirii'
    dests=[dest1,dest2,dest3]

     # creating an object of destination 
    return render(request,"gallary.html",{'dests':dests})