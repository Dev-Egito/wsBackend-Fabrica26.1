import requests
from django.shortcuts import render, redirect
from .models import Filme, Critica

from django.contrib.auth.models import User

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
    criticas = None
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
            criticas = Critica.objects.filter(filme=filme_obj)
            
    print("API:", filme_api)
    print("OBJ:", filme_obj)

    return render(request, 'filmes/buscar.html', {
        'filme': filme_api,
        'filme_obj': filme_obj,
        'criticas': criticas,
    })

def criar_critica(request, filme_id):
    filme = Filme.objects.get(id=filme_id)

    if request.method == "POST":
        comentarios = request.POST.get("comentarios")
        nota = request.POST.get("nota")

        usuario_manual = User.objects.first()

        Critica.objects.create(
            usuario = usuario_manual,
            filme = filme,
            comentarios = comentarios,
            nota = nota,
        )

        return redirect(f'/filmes/?titulo={filme.titulo}')

    return render(request, 'filmes/criar_critica.html', {'filme': filme})
    
# Create your views here.
