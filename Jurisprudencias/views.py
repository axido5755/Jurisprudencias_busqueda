import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import jurisprudencias
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json

# Create your views here.

def list_jurisprudencias(request):
    # Consulta todos los objetos de la tabla Jurisprudencia
    jurisprudencias_objet = jurisprudencias.objects.all()

    # Pasa los objetos al contexto y renderiza la plantilla
    return render(request, 'lista_bdd.html', {'jurisprudencias': jurisprudencias_objet})





def create_jurisprudencias(request):
    if request.method == 'POST':
        #todo el codigo de minado de datos
        Nombre = request.POST.get('Nombre', '')
        response = requests.post("https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list", 
        json={"page": 1, "pageSize": 10, "search": Nombre, "orden": "nuevo"},
        headers={"Content-Type":"application/json"}
        )
        json_data = json.loads(response.text)
        jurisprudencias_llamado = json_data['jurisprudencias']
        #todo el codigo de minado de datos

        #guardado de los datos
        for jurisprudencia in jurisprudencias_llamado:
            if not jurisprudencias.objects.filter(id_jurisprudencias=jurisprudencia['id']).exists(): #sin que se repita
                fecha_sentencia = jurisprudencia['fechaSentencia'] #arreglar fecha
                fecha_objeto = datetime.datetime.strptime(fecha_sentencia, '%d-%m-%Y')
                fecha_formateada = fecha_objeto.strftime('%Y-%m-%d')

                jurisprudencias_new = jurisprudencias(
                id_jurisprudencias  = jurisprudencia['id'],
                tipoCausa           = jurisprudencia['tipoCausa'],
                rol                 = jurisprudencia['rol'],
                caratula            = jurisprudencia['caratula'],
                nombreProyecto      = jurisprudencia['nombreProyecto'],
                fechaSentencia      = fecha_formateada,
                descriptores        = jurisprudencia['descriptores'],
                linkSentencia       = jurisprudencia['linkSentencia'],
                urlSentencia        = jurisprudencia['urlSentencia'],
                activo              = jurisprudencia['activo'],
                tribunal            = jurisprudencia['tribunal'],
                valores             = jurisprudencia['valores'],
                tipo                = jurisprudencia['tipo'],
                relacionada         = jurisprudencia['relacionada'],
                visitas             = jurisprudencia['visitas'],
                )
                jurisprudencias_new.save()
        

        return render(request, 'lista_busqueda.html', {'jurisprudencia': jurisprudencias_llamado , 'Nombre': Nombre})

            

   
        