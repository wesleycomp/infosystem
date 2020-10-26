from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('descricao','cbo','ativo')
    exclude = ('criacao','modificado')
