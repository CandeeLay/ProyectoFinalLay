from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    return HttpResponse("Holis")

def prueba(self):
    nombre = "Cande"
    apellido = "Lay"

    namelist = ["Carla", "Camila"]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
    }

    mihtml = open("C:/Users/Candela/Documents/ProyectoFinalLay/ProyectoFinal/ProyectoFinal/plantillas/template1.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontext = Context()
    documento = plantilla.render(micontext)
    return HttpResponse(documento)