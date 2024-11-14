from django.shortcuts import render

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