from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ("Nebulosa", "Nebulosa"), 
        ("Estrela", "Estrela"), 
        ("Galáxia", "Galáxia"), 
        ("Planeta", "Planeta")
        ]

    nome = models.CharField(max_length=100, null=False, blank=False) #(maximo 100 caracteres, não pode ser vazia)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User, #usuario
        on_delete=models.SET_NULL,   #caso seja deletado, o user seja classificado como null
        null=True,
        blank=False,
        related_name='user',
    )

    def __str__(self):
        return self.nome