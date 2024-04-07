# mi urls
from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name="IND"),
    path('accion/',accion,name="ACC"),
    path('aventura/',aventura,name="AVE"),
    path('terror/',terror,name="TER"),
    path('infantil/',infantil,name="INF"),
    path('clasico/',clasico,name="CLA"),
    path('formulario/',formulario,name="FORM"),
    path('login/',login,name="LOGIN"),
    path('cerrar/',cerrar_sesion,name="CERRAR"),
    path('administracion/',administracion,name="ADMIN"),
    path('info/',info,name="INFO"),

]
