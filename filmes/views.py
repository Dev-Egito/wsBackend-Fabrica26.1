import requests
from django.shortcuts import render 
from .models import Filme

def buscar_filme_api(titulo):
    url = f"http://www.omdbapi.com/?t={titulo}&apikey=6f10a1dc"
    response = requests.get(url)

    data = response.json()
    print(data)

    if response.status_code == 200: 
        if data.get("Response") == "True":
            return data
    return None

def buscar_filme(request):
    filme_api = None
    filme_obj = None
    titulo = request.GET.get('titulo')

    if 'titulo' in request.GET:
        filme_api = buscar_filme_api(titulo)

        if filme_api:
            filme_obj, created = Filme.objects.get_or_create(
                imdb_id=filme_api["imdbID"],
                defaults={
                    "titulo": filme_api["Title"]
                }
            )
            
    print("API:", filme_api)
    print("OBJ:", filme_obj)

    return render(request, 'filmes/buscar.html', {
        'filme': filme_api,
        'filme_obj': filme_obj,
    })
    
# Create your views here.
