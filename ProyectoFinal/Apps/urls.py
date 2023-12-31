from django.urls import path, include
from Apps.views import * #inicio,mascotas,dar_adopcion,adoptar,accesorios,setAdoptar,getAdoptar, buscarAdoptar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('mascotas/', mascotas, name="mascotas"),
    path('adopcion/', dar_adopcion, name="adopcion"),
    path('adoptar/', adoptar, name="adoptar"),
    path('accesorios/', accesorios, name="accesorios"),
    path('setAdoptar/', setAdoptar, name="setAdoptar"),
    path('getAdoptar/', getAdoptar, name="getAdoptar"),
    path('buscarAdoptar/', buscarAdoptar, name="buscarAdoptar"),
    path('editarAdoptar/<nombre_Adoptar>', editarAdoptar, name="editarAdoptar"),
    path('login/', loginweb, name="login"),
    path('registro/', registro, name="registro"),
    path('Logout/', LogoutView.as_view(next_page='login'), name="Logout"),
    path('perfil/', perfilview, name="perfil"),
    path('perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('perfil/changePass/', changePass, name="changePass"),
    path('perfil/editAvatar/', editAvatar, name="editAvatar"),
]