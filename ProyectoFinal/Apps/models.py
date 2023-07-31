from django.db import models

# Create your models here.

class adoptar(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    edad = models.IntegerField()
    email = models.EmailField()

class mascotas(models.Model):
    animal = models.CharField(max_length=10)
    edad = models.IntegerField()

class adopcion(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    email = models.EmailField()

class accesorios(models.Model):
    producto = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
