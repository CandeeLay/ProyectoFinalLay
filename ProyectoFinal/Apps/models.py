from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Adoptar(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    edad = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} - edad: {self.edad} - email: {self.email}"

class mascotas(models.Model):
    animal = models.CharField(max_length=10)
    edad = models.IntegerField()
    def __str__(self):
        return f"animal: {self.animal} - edad: {self.edad}"

class adopcion(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()
    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} - email: {self.email}"

class accesorios(models.Model):
    producto = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    def __str__(self):
        return f"producto: {self.producto} - descripcion: {self.descripcion} - precio: {self.precio}"
    
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank = True)