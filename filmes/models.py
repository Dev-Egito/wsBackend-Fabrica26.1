from django.db import models
from django.contrib.auth.models import User 

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    imbd_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.titulo


class Critica(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    comentarios = models.TextField()
    nota = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.filme}"

    class Meta:
        unique_together = ('usuario', 'filme')



# Create your models here.