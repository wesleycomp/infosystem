from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('nome_funcao','cbo','ativo')
    exclude = ('criacao','modificado','idusuariocadastro')

@admin.register(UnidadeClinica)
class UnidadeClinicaAdmin(admin.ModelAdmin):
    list_display = ('nome_unidade','cnpj','endereco','telefone','cep','cidade')
    exclude = ('criacao','modificado')
