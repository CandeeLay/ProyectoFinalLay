from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from Apps.models import adoptar

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def adoptar(request):
    return render(request, "adoptar.html")

def mascotas(request):
    return render(request, "mascotas.html")

def dar_adopcion(request):
    return render(request, "adopcion.html")

def accesorios(request):
    return render(request, "accesorios.html")

def setAdoptar(request):
    if request.method == 'POST':
        adoptar = adoptar(nombre=request.POST["nombre"], apellido=request.POST["apellido"], edad=request.POST["edad"], email=request.POST["email"])
        adoptar.save()
        return redirect("Apps/inicio.html")
    return render(request, "setAdoptar.html")