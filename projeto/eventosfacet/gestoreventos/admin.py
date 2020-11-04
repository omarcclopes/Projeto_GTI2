from django.contrib import admin

#from gestoreventos.models import Curso, Funcionario, Palestrante, Evento
from gestoreventos.models import Curso, Funcionario, Palestrante, Evento

# Register your models here.
admin.site.register(Curso)
admin.site.register(Funcionario)
admin.site.register(Palestrante)
admin.site.register(Evento)