from django.shortcuts import render
import datetime
from django import forms
from  django.http import HttpResponse
# Create your views here.
def  home(request):
    return render(request,"homepage.html")

def mydate(request):
    now=datetime.datetime.now()


    return render(request,"date.html",{"newyear ":now.month==1 and now.day==1})
mtask=['learrn','play','jump over']
def task(request):
    return render(request,"tasks.html",{"tasks: ":mtask })


class NewTaskForm(forms.Form):
    mytask=forms.CharField(label="New task")
    priority=forms.IntegerField(label="priority",min_value=1)

def addtask(request):
    return render(request,"homepage.html",{"form":NewTaskForm})