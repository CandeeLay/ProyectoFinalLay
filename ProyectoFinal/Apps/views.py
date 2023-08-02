from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from Apps.models import Adoptar
from Apps.forms import formAdoptar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def adoptar(request):
    Adoptar = Adoptar.objects.all()
    return render(request, "Adoptar.html", {"Adoptar": Adoptar})

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

def leerAdoptar(request):
    Adoptar = Adoptar.objects.all()
    return render(request, "Adoptar.html", {"Adoptar": Adoptar})

def editarAdoptar(request, nombre_Adoptar):
    adoptar = Adoptar.objects.get(nombre = nombre_Adoptar)

    if request.method == 'POST':
        miFormulario = formAdoptar(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            
            adoptar.nombre = data['nombre']
            adoptar.apellido = data['apellido']
            adoptar.edad = data['edad']
            adoptar.email = data['email']
            adoptar.save()
            miFormulario = formAdoptar()
            Adoptar = Adoptar.objects.all()
            return render(request, "setAdoptar.html", {"miFormulario":miFormulario, "Adoptar":Adoptar})
    else:
        miFormulario = formAdoptar()
    return render(request, "editarAdoptar.html", {"miFormulario":miFormulario})

def loginweb(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['usuario'], password = request.POST['contraseña'])
        if user is not None:
            login(request, user)
            return HttpResponse("inicio.html")
        else:
            return render(request, "login.html", {'error': 'Usuario o contraseña incorrecto'})
    else:
        return render(request, "login.html")