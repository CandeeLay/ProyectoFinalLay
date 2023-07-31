from django.http import HttpResponse
from django.template import Template, Context, loader

def home(request):
    return HttpResponse("Holis")

def prueba(self):
    nombre = "Cande"
    apellido = "Lay"

    namelist = ["Carla", "Camila"]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist,
    }

#    mihtml = open("C:/Users/Candela/Documents/ProyectoFinalLay/ProyectoFinal/ProyectoFinal/plantillas/template1.html")
#    mihtml = loader.get_template("template.html")
    plantilla = loader.get_template("template1.html")
#    mihtml.close()
#    micontext = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)