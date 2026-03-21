import requests
from django.shortcuts import render 

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
    filme = None
    titulo = request.GET.get('titulo')

    if 'titulo' in request.GET:
        filme = buscar_filme_api(titulo)
    
    return render(request, 'filmes/buscar.html', {'filme': filme})
    
# Create your views here.
