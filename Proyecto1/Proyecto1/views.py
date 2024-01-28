from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
    return HttpResponse("Hola Django Coder")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: {nombre}"
    return HttpResponse(documentoDeTexto)

def plantilla(request):
   
    mi_html = open(r'C:\Users\Ale\Documents\Python curse prueba\Proyecto1\Proyecto1\templates\template1.html', 'r')
   
    plantilla = Template(mi_html.read()) # Se carga en memoria nuestro documento
    # # OJO: Importar Template y Context con: from django.template import Template, Context
   
    mi_html.close() # Cerramos el archivo
   
    mi_contexto = Context() # Le doy al contexto mi nombre y apellido

    documento = plantilla.render(mi_contexto) # Aca renderizamos la plantilla en documento
   
    return HttpResponse(documento)