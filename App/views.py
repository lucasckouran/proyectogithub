from django.http import HttpResponse
from datetime import datetime as dt
from django.template import Template, Context, loader
from App.models import Curso

def canejo(request):
    return HttpResponse("Hola Canejin")

def pruebita(request):
    return HttpResponse("<br> Vamos con esta prueba en la segunda linea")

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)


# def template(self):
    # miHTML = open(".\\Proyecto1\\plantillas\\template.html")
    # plantilla = Template(miHTML.read())
    # miHTML.close()
    # miContexto = Context()
    # documento = plantilla.render(miContexto)
# return HttpResponse(documento)

# Probamos con el loader
def contexto(request):
    nombre = "Canejo"
    notas = [4,5,6,7,8,9]
    dic = {"nombre": nombre,"ahora": str(dt.now()), "notas":notas}

    plantilla = loader.get_template('template.html')
    documento = plantilla.render(dic)
    loader.get_template('template.html')

    return HttpResponse(documento)

def curso(request,nombre, numero):
    curso = Curso(nombre=nombre, camada=int(numero))
    curso.save
    documento = f"Curso: {curso.nombre}<br>Camada:  {curso.camada}"
    return HttpResponse(documento)

def index(request):
    
    plantilla = loader.get_template('index.html')
    documento = plantilla.render()
    loader.get_template('index.html')

    return HttpResponse(documento)