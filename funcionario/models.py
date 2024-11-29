from django.db import models
from datetime import datetime

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=50)

    def __str__(self):
        return (self.nome)

class Funcao(models.Model):
    nome = models.CharField('Função', max_length=50, unique=True)

    def __str__(self):
        return (self.nome)

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100, blank=False, null=False)
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE, related_name='Funcoes', null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='Empresas', null=True)
    data = models.DateTimeField('Data Admissão', null=True)

    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
    
    def get_absolute_url(self):
        return ('funcionarios/' + self.slug)

    def get_data(self):
        return self.data.strftime('%d/%m/%Y')