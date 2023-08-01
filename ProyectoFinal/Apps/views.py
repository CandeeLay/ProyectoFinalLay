from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from Apps.models import Adoptar
from Apps.forms import formAdoptar

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def adoptar(request):
    return render(request, "Adoptar.html")

def mascotas(request):
    return render(request, "mascotas.html")

def dar_adopcion(request):
    return render(request, "adopcion.html")

def accesorios(request):
    return render(request, "accesorios.html")

def setAdoptar(request):
    if request.method == 'POST':
        miFormulario = formAdoptar(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            adoptar = Adoptar(nombre=data["nombre"], apellido=data["apellido"], edad=data["edad"], email=data["email"])
            adoptar.save()
            return render(request, "inicio.html")
    else:
        miFormulario = formAdoptar()
    return render(request, "setAdoptar.html", {"miFormulario":miFormulario})

"""    if request.method == 'POST':
        adoptar = Adoptar(
            nombre=request.POST["nombre"],
            apellido=request.POST["apellido"],
            edad=request.POST["edad"],
            email=request.POST["email"]
        )
        adoptar.save()
        return redirect("inicio")  # Correct the redirect URL to 'inicio'
    return render(request, "setAdoptar.html")"""

def getAdoptar(request):
        return render(request, "getAdoptar.html")

def buscarAdoptar(request):
    if request.GET["nombre"]:
         nombre = request.GET["nombre"]
         adoptar = Adoptar.objects.filter(nombre = nombre)
         return render(request, "getAdoptar.html", {"adoptar":adoptar})
    else:
        respuesta = "No se enviaron datos"
    return  HttpResponse(respuesta)