from django.urls import path, include
from Apps.views import * #inicio,mascotas,dar_adopcion,adoptar,accesorios,setAdoptar,getAdoptar, buscarAdoptar

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
]