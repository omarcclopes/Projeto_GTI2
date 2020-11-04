from django.contrib import admin

# Import dos modelos
from gestoreventos.models import Curso, Funcionario, Palestrante, Evento

# Register your models here.
admin.site.register(Curso)
admin.site.register(Funcionario)
admin.site.register(Palestrante)
admin.site.register(Evento)