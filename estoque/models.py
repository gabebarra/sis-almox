from django.db import models
from funcionario.models import Funcionario
from obra.models import Obra
from django.core.exceptions import ValidationError

# Create your models here.
class Unidade(models.Model):
    unidade = models.CharField('Unidade', max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.unidade

class Prateleira(models.Model):
    nome = models.CharField('Nome', max_length=50, blank=False, null=False, unique=True)
    descricao = models.CharField('Descrição', max_length=50, default='-')
    slug = models.SlugField('Atalho')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)

class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=50)

    def __str__(self):
        return self.categoria

class Item(models.Model):
    nome = models.CharField('nome', max_length=80, blank=False, null=False)
    unidade = models.ForeignKey(Unidade, verbose_name='Unidade', on_delete=models.CASCADE)
    estoque = models.PositiveIntegerField('Estoque', blank=False, default=0)
    prateleira = models.ForeignKey(Prateleira, verbose_name='Prateleira', on_delete=models.CASCADE)
    estoque_min = models.PositiveIntegerField('Estoque Min', blank=False, default=0)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='Categorias')
    vencimento = models.IntegerField('Vencimento (em Dias)', default=0, blank=True)


    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return ('detalhe/' + str(self.id))

    class Meta:
        ordering = ('nome',)

class Epi(models.Model):
    nome = models.CharField('Nome', max_length=80, blank=False, null=False, unique=True)
    unidade = models.ForeignKey(Unidade, verbose_name='Unidade', on_delete=models.CASCADE, null=True)
    ca = models.CharField('CA', blank=True, max_length=50)
    prateleira = models.ForeignKey(Prateleira, verbose_name='Prateleira', on_delete=models.CASCADE)
    estoque = models.PositiveIntegerField('Estoque', blank=False, default=0)
    estoque_min = models.PositiveIntegerField('Estoque Min', blank=False, default=0)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)

class EntradaItem(models.Model):
    item = models.ForeignKey(Item, verbose_name='Item', on_delete=models.CASCADE)
    emprestimo = models.BooleanField('Emprestimo', null=True, blank=True, default=False)
    quantidade = models.IntegerField('Qtde')
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    obs = models.CharField('Obs', max_length=50, blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, verbose_name='Funcionario', on_delete=models.CASCADE, null=True, blank=True)
    obra = models.ForeignKey(Obra, verbose_name='Obra', on_delete=models.CASCADE, null=True, blank=True)

    def get_data(self):
        return self.data.strftime('%d/%m/%y')

    def save(self, *args, **kwargs):
        item = self.item
        item.estoque = item.estoque + self.quantidade
        item.save()
        super(EntradaItem, self).save(*args, **kwargs)

class SaidaItem(models.Model):
    emprestimo = models.BooleanField('Emprestimo', null=True, blank=True, default=False)
    entregue = models.BooleanField('Entregue', default=False)
    devolucao = models.DateField('Devolucao', auto_now=False, auto_now_add=False, blank=True, null=True)

    item = models.ForeignKey(Item, verbose_name='ItemS', on_delete=models.CASCADE)
    quantidade = models.IntegerField('Qtde')
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    obs = models.CharField('Obs', max_length=50, blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, verbose_name='Funcionario', on_delete=models.CASCADE, null=True, blank=True)
    obra = models.ForeignKey(Obra, verbose_name='Obra', on_delete=models.CASCADE, null=True, blank=True)
    galeria = models.BooleanField("Galeria", blank=True, default=False)

    def get_data(self):
        return self.data.strftime('%d/%m/%y')

    def get_devolucao(self):
        return self.devolucao.strftime('%d/%m/%y')

    class Meta:
        ordering = ('data',)
    
    def save(self, *args, **kwargs):
        item = self.item
        item.estoque = item.estoque - self.quantidade
        item.save()
        super(SaidaItem, self).save(*args, **kwargs)

class FotosSaida(models.Model):
    saida = models.ForeignKey(SaidaItem, verbose_name="Saidaid", on_delete=models.CASCADE)
    foto = models.ImageField('Foto', upload_to='saidas', null=True)