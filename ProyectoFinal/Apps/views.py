from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from Apps.models import Adoptar

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def Adoptar(request):
    return render(request, "Adoptar.html")

def mascotas(request):
    return render(request, "mascotas.html")

def dar_adopcion(request):
    return render(request, "adopcion.html")

def accesorios(request):
    return render(request, "accesorios.html")

def setAdoptar(request):
    if request.method == 'POST':
        adoptar = Adoptar(
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            edad=request.POST["edad"],
            email=request.POST["email"]
        )
        adoptar.save()
        return redirect("inicio")  # Correct the redirect URL to 'inicio'
    return render(request, "setAdoptar.html")