from django.db import models
from datetime import datetime

# Create your models here.

class Veiculo(models.Model):
    nome = models.CharField('Nome', max_length=50, null=False, blank=False)
    ano = models.CharField('Ano', max_length=50)
    placa = models.CharField('Placa', max_length=50)
    renavam = models.CharField('Renavam', max_length=50)

    foto = models.FileField('Foto', upload_to='veiculos', null=True)

    def get_absolute_url(self):
        return ('detalhe/' + str(self.id))

    def get_conserto_url(self):
        return ('conserto/adicionar/' + str(self.id))

    def get_abastecimento_url(self):
        return ('abastecimento/adicionar/' + str(self.id))

    def get_excluir_url(self):
        return ('veiculo/excluir/' + str(self.id))

    def __str__(self):
        return (self.nome)

class Posto(models.Model):
    nome = models.CharField('Nome', max_length=70)

    def __str__(self):
        return (self.nome)

class Abastecimento(models.Model):
    posto = models.ForeignKey(Posto, related_name='Postos', verbose_name='Posto', on_delete=models.CASCADE)
    data = models.DateField('Data')
    requisicao = models.CharField('Requisição', max_length=70)
    veiculo = models.ForeignKey(Veiculo, related_name='Veiculos_Abastecidos', verbose_name='Veiculo', on_delete=models.CASCADE)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return (self.veiculo.nome) + ' Req:' + (self.requisicao) + ' Valor:' + str((self.valor))

    def get_data(self):
        return self.data.strftime('%d/%m/%y')

    def get_abastecimento_excluir_url(self):
        return ('../abastecimento/excluir/' + str(self.id))

class CategoriaConserto(models.Model):
    categoria = models.CharField('Categoria', null=False, blank=False, max_length=50)

    def __str__(self):
        return (self.categoria)

class Oficina(models.Model):
    nome = models.CharField('nome', max_length=50, null=False)

    def __str__(self):
        return (self.nome)

class Conserto(models.Model):
    veiculo = models.ForeignKey(Veiculo, related_name='Veiculos_Consertados', verbose_name='Veículo', on_delete=models.CASCADE)
    oficina = models.ForeignKey(Oficina, related_name='Oficina', verbose_name='Oficina', on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaConserto, related_name='Categoria', verbose_name='Categoria', on_delete=models.CASCADE)
    data = models.DateField('Data')
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2, default=0)
    arq_nota = models.FileField('Arquivo Nota', upload_to='veiculos', null=True)
    obs = models.CharField('Obs', max_length=150, null=True)

    def __str__(self):
        return (self.categoria.categoria) + ' ' + (self.veiculo.nome) + ' ' + str((self.valor))

    def get_data(self):
        return self.data.strftime('%d/%m/%y')

    def get_absolute_url(self):
        return ('/' + str(self.id))

    def get_conserto_excluir_url(self):
        return ('../conserto/excluir/' + str(self.id))