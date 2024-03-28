# mi urls
from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name="IND"),
    path('/accion',accion,name="ACC"),
    path('/aventura',aventura,name="AVE"),
    path('/terror',terror,name="TER"),
    path('/infantil',infantil,name="INF"),
    path('/clasico',clasico,name="CLA"),
    path('/formulario',formulario,name="FORM"),
]
