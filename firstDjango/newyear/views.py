from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from  django.http import HttpResponse

mtask=[]
class NewTaskForm(forms.Form):
    mtask=forms.CharField(label="New task")
    priority=forms.IntegerField(label="priority",min_value=1)

# Create your views here.
def  home(request):
    return render(request,"homepage.html")

def mydate(request):
    now=datetime.datetime.now()


    return render(request,"date.html",{"newyear ":now.month==1 and now.day==1})

def task(request):
    if "mtask" not in request.session:
        request.session['mtask']=[]
        pass
    return render(request,"tasks.html",{"tasks: ":request.session['mtask'] })



def addtask(request):
    # adding a condition 
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
          request.session['tasks'] +=[mtask]
          mtask.append(task) 
          return HttpResponseRedirect(reverse("task:index"))

        else:
            return render(request,"tasks.html",{
                "addData":mtask
            })
        
    return render(request,"homepage.html",{"form":NewTaskForm})