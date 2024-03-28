from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def accion(request):
    return render(request,'accion.html')

def aventura(request):
    return render(request,'aventura.html')

def clasico(request):
    return render(request,'clasico.html')

def formulario(request):
    return render(request,'formulario.html')

def infantil(request):
    return render(request,'infantil.html')

def terror(request):
    return render(request,'terror.html')
