from datetime import datetime
from django.shortcuts import render
from django.db.models import Q
from .models import Usuario
# importar el modelo de tabla User 
from django.contrib.auth.models import User
# importar librerias que permitan la validacion del login
from django.contrib.auth import authenticate,logout,login as login_aut
# importar libreria decoradora que permite evitar el ingreso de usuarios a las paginas web
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/login/')
def accion(request):
    return render(request,'accion.html')

@login_required(login_url='/login/')
def aventura(request):
    return render(request,'aventura.html')

@login_required(login_url='/login/')
def clasico(request):
    return render(request,'clasico.html')

def formulario(request):
    contexto={}
    if request.POST:
        direccion = request.POST.get("txtdireccion")
        fecha_naci = request.POST.get("fechaNacimiento")
        correo =  request.POST.get("correoElectronico")
        password = request.POST.get("password")
        user_name = request.POST.get("nombreUsuario")
        ape_materno= request.POST.get("txtape_mat")
        ape_paterno = request.POST.get("txtape_pat")
        nombre = request.POST.get("txtnombre")
        try:
            
            usu = User()
            usu.first_name=nombre
            usu.last_name=ape_paterno
            usu.email=correo
            usu.username=user_name
            usu.set_password(password)
            usu.save()

            usuario = Usuario(
                nombre=nombre,
                apellido_pat=ape_paterno,
                apellido_mat=ape_materno,
                user_name=user_name,
                password=password,
                correo=correo,
                fecha_naci=fecha_naci,
                direccion=direccion
            )
            usuario.save()

            # us = authenticate(request,username=user_name,password=password)
            # login_aut(request,us)
            contexto["mensaje"]="Usuario Registrado"
        except BaseException as error:
            contexto["mensaje"]=error
            
    return render(request,'formulario.html',contexto)

@login_required(login_url='/login/')
def infantil(request):
    return render(request,'infantil.html')

@login_required(login_url='/login/')
def terror(request):
    return render(request,'terror.html')

@login_required(login_url='/login/')
def administracion(request):
    contexto={}
    nom_user = request.user.username # recupero del request el usuario (login)
    print(nom_user)
    datos= User.objects.get(username=nom_user)
    print(datos.is_staff)
    if datos.is_staff:
        contexto={"mensaje":"No Puede Ver El Perfil de un Administrador"}
        return render(request,'info.html',contexto)
    if request.POST:
        contexto={}# grabar cambios
        direccion = request.POST.get("direccion")
        fecha_naci = request.POST.get("fechaNacimiento")
        correo =  request.POST.get("correoElectronico")
        password = request.POST.get("password")
        user_name = request.POST.get("nombreUsuario")
        ape_materno= request.POST.get("txtape_mat")
        ape_paterno = request.POST.get("txtape_pat")
        nombre = request.POST.get("txtnombre")
        try:            
            usu = User.objects.get(username=user_name)
            usu.first_name=nombre
            usu.last_name=ape_paterno
            usu.email=correo
            usu.set_password(password)
            usu.save()

            usuario = Usuario.objects.get(user_name=user_name)
            usuario.nombre=nombre
            usuario.apellido_pat=ape_paterno
            usuario.apellido_mat=ape_materno
            usuario.password=password
            usuario.correo=correo
            usuario.fecha_naci=fecha_naci
            usuario.direccion=direccion
            usuario.save()

            # us = authenticate(request,username=user_name,password=password)
            # login_aut(request,us)
            contexto["mensaje"]="Usuario Modificado"
        except BaseException as error:
            contexto["mensaje"]=error
    else:
        # ver los datos
        usuario= Usuario.objects.get(user_name=nom_user)
        contexto["nombre"]=usuario.nombre
        contexto["apellido_pat"]=usuario.apellido_pat
        contexto["apellido_mat"]=usuario.apellido_mat
        contexto["user_name"]=usuario.user_name    
        contexto["password"]=usuario.password    
        contexto["correo"]=usuario.correo
        contexto["fecha_naci"]=str(usuario.fecha_naci)
        contexto["direccion"]=usuario.direccion
        print(usuario.fecha_naci)
    return render(request,'administrador.html',contexto)

def login(request):
    contexto={"mensaje":""}
    if request.POST:        
        usuario = request.POST.get("exampleInputUsuario")
        password= request.POST.get("exampleInputPassword1")
        print(usuario)
        print(password)
        try:
            usu = authenticate(request,username=usuario,password=password)
            if usu is not None and usu.is_active:
                login_aut(request,usu)
                return render(request,"index.html",contexto)
            else:
                contexto["mensaje"]="usuario o contraseña incorrecta"
        except BaseException as error:
            contexto["mensaje"]=error
    return render(request,'login.html',contexto)


def cerrar_sesion(request):
    logout(request)
    return render(request,"index.html")

def info(request,mensaje):
    contexto={}
    contexto["mensaje"]=mensaje
    return render(request,"info.html",contexto)
