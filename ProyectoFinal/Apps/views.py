from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from Apps.models import Adoptar, Avatar
from Apps.forms import formAdoptar, useredit, changeform, Avatarform
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def inicio(request):
    return render(request, "inicio.html")

def adoptar(request):
    return render(request, "Adoptar.html")

@login_required
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
            return render(request, "inicio.html")
        else:
            return render(request, "login.html", {'error': 'Usuario o contraseña incorrecto'})
    else:
        return render(request, "login.html")
    
def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate.is_valid():
            userCreate.save()
            return redirect('login')
        else:
            return render(request, 'registro.html')
    else:
        return render(request, 'registro.html')

@login_required
def perfilview(request):
    return render(request, 'Perfil/perfil.html',)

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = useredit(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'Perfil/perfil.html')
        else:
            form = useredit(initial= {'username': usuario.username, "email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})
            return render(request, "Perfil/editarPerfil", {"form": form})

@login_required
def changePass(request):
    usuario = request.user
    if request.method == "POST":
        form = changePass(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
                return HttpResponse("Las contraseñas no coinciden")
        return render(request, "inicio.html")
    else:
        form = changeform(user = usuario)
        return render(request, 'changePass.html', {"form": form})
    
def editAvatar(request):
    if request.method == "POST":
        form = Avatarform(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "inicio.html", {"avatar": avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = Avatarform()
        except:
            form = Avatarform()