from django.urls import path

from . import views
urlpatterns=[
    path("",views.home, name='homepage'),
    path("newyear",views.mydate, name='date'),
     path("add",views.addtask, name='addtask'),
    path("tasks",views.task, name='tasks'),
]