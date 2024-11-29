from django.db import models
from datetime import datetime
from decimal import Decimal

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.nome

class Obra(models.Model):
    nome = models.CharField('Descrição', max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='Clientes', null=False)
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    local = models.CharField('Local', max_length=50)

    def __str__(self):
        return self.nome

    def get_data(self):
        return self.data.strftime('%d/%m/%y')