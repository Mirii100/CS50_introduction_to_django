from django.urls import path

from . import views
urlpatterns=[
    path("",views.hello, name='hello'),
    path("<str:name>",views.ourName, name='myname'),
    path("Alex",views.Alex, name='hello'),
    # for greeting rendom user
    #path("<str:name>",views.greet, name='greetings'),
    path("all",views.all,name='all'),
    path("helloThere",views.helloThere,name='my greetings')
]