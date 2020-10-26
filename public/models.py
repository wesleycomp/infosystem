from django.db import models

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DateTimeField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Funcao(Base):
    descricao = models.CharField('Descrição', max_length=100)
    cbo = models.CharField('Cbo', max_length=50)

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'

    def __str__(self):
        return self.descricao
