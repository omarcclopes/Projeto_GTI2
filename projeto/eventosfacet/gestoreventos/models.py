from django.db import models

# Create your models here.

class Evento(models.Model):
    nome_evento = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_evento
        
class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    codigo_curso = models.IntegerField()

    def __str__(self):
        return self.nome_curso

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=150)   
    matricula = models.IntegerField()
    email_institucional = models.CharField(max_length=100)
    curso_vinculado = models.ForeignKey(Curso, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome_funcionario
        