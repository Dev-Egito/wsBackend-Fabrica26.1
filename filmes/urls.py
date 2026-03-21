from django.urls import path
from .views import buscar_filme, criar_critica

urlpatterns = [
    path('', buscar_filme, name = 'buscar_filme'), 
    path('criar_critica/<int:filme_id>/', criar_critica, name = 'criar_critica'),
]