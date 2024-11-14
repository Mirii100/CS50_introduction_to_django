from django.urls import path
from . import views

urlpatterns=[
    path("",views.nav, name='navbar'),
    path("login",views.login, name='login'),
    path("add",views.add, name='add'),
    path("portfolio",views.service, name='portfolio'),
    path("serve",views.services, name='service'),
    path("about",views.about, name='about'),
    path("Resume",views.resume, name='resume'),
    path("contact",views.contactUs, name='contact'),
]