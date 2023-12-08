from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("nissan/",views.nissan,name="nissan"),
    path("client/",views.client_details,name="client"),
    path("dataclient",views.dataclient,name="dataclient"),
    path("login/",views.login,name="login"),
    path("new",views.new,name="new")
]
