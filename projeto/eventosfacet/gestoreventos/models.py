from django.db import models

# Create your models here.

class Evento(models.Model):
    nome_evento = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_evento
        