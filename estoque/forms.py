from django import forms
from .models import *
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, HTML, Field

class UnidadeForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = ('unidade',)

class PrateleiraForm(forms.ModelForm):
    class Meta:
        model = Prateleira
        fields = ('nome', 'descricao',)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('categoria',)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nome', 'unidade', 'estoque', 'prateleira', 'estoque_min', 'valor', 'categoria','vencimento')

class EntradaForm(forms.ModelForm):
    class Meta:
        model = EntradaItem
        fields = ('item', 'quantidade', 'data', 'obs', 'funcionario', 'obra')

    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

class EmprestimoDevolverForm(forms.ModelForm):
    class Meta:
        model = EntradaItem
        fields = ('quantidade', 'obs', 'data')

    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

class EmprestimoSubstituirForm(forms.ModelForm):
    class Meta:
        model = SaidaItem
        fields = ('obs',)

class EditEntradaForm(forms.ModelForm):
    class Meta:
        model = EntradaItem
        fields = ('item', 'quantidade', 'data', 'obs', 'funcionario', 'obra')

class EditSaidaForm(forms.ModelForm):
    class Meta:
        model = EntradaItem
        fields = ('item', 'quantidade', 'data', 'obs', 'funcionario', 'obra')

class EntradaUnicaForm(forms.ModelForm):
    class Meta:
        model = EntradaItem
        fields = ('quantidade', 'data', 'obs', 'funcionario', 'obra')
    
    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

class SaidaUnicaForm(forms.ModelForm):
    class Meta:
        model = SaidaItem
        fields = ('quantidade', 'data', 'obs', 'funcionario', 'obra')

    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

class SaidaForm(forms.ModelForm):
    class Meta:
        model = SaidaItem
        fields = ('item','quantidade', 'data', 'obs', 'funcionario', 'obra')

    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

class EmprestimoUnicoForm(forms.ModelForm):
    class Meta:
        model = SaidaItem
        fields = ('quantidade', 'data', 'obs', 'funcionario','obra')

    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )
        