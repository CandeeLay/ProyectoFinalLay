from django.urls import path, include
from Apps.views import inicio,mascotas,dar_adopcion,adoptar,accesorios,setAdoptar

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('mascotas/', mascotas, name="mascotas"),
    path('adopcion/', dar_adopcion, name="adopcion"),
    path('adoptar/', adoptar, name="adoptar"),
    path('accesorios/', accesorios, name="accesorios"),
    path('setAdoptar/', setAdoptar, name="setAdoptar"),
]
