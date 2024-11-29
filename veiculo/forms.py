from django import forms
from .models import *
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, HTML, Field

class ConsertoForm(forms.ModelForm):
    class Meta:
        model = Conserto
        fields = ('veiculo', 'oficina','categoria','data','valor', 'obs', 'arq_nota')

    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

    def __init__(self, *args, **kwargs):
        super(ConsertoForm, self).__init__(*args, **kwargs)
        self.fields['arq_nota'].required = False

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = ('nome',)

class CategoriaConsertoForm(forms.ModelForm):
    class Meta:
        model = CategoriaConserto
        fields = ('categoria',)

class AbastecimentoForm(forms.ModelForm):
    class Meta:
        model = Abastecimento
        fields = ('veiculo', 'posto', 'data', 'requisicao', 'valor')
    
    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

class PostoForm(forms.ModelForm):
    class Meta:
        model = Posto
        fields = ('nome',)

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('nome','ano','placa','renavam','foto')

    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        self.fields['foto'].required = False
