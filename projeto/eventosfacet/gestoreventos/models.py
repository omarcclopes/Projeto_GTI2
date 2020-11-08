from django.db import models

# Create your models here.
# Omar Cantidiano da Cunha Lopes

class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    codigo_curso = models.IntegerField()

    def __str__(self):
        return self.nome_curso

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=150)   
    matricula = models.IntegerField()
    email_institucional = models.CharField(max_length=100)
    curso_vinculado = models.ForeignKey(Curso, on_delete=models.RESTRICT, blank=True, null=True)
    setor = models.CharField(max_length=100, default='Secretaria')

    def __str__(self):
        return self.nome_funcionario

class Palestrante(models.Model):
    nome_palestrante = models.CharField(max_length=150)
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False)
    cpf = models.CharField(max_length=11)
    email_palestrante = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    titulacao = models.CharField(max_length=100, default='Mestre')

    def __str__(self):
        return self.nome_palestrante

class Evento(models.Model):
    nome_evento = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300, blank=True, null=True)
    tema = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, default='www.faculdadedetimbauba.edu.br')
    local = models.CharField(max_length=100, default='Auditório FACET')
    data_inicio = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    data_final = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    curso_organizador = models.ForeignKey(Curso, on_delete=models.RESTRICT, blank=True, null=True)
    palestrantes = models.ForeignKey(Palestrante, on_delete=models.RESTRICT, blank=True, null=True)
    organizador = models.ForeignKey(Funcionario, on_delete=models.RESTRICT, blank=True, null=True)
    carga_horaria = models.IntegerField(default=4)

    def __str__(self):
        return self.nome_evento
        