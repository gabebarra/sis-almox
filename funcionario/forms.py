from django import forms
from .models import *
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, HTML, Field

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'funcao', 'empresa', 'data', 'ativo')

    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

class Edit_FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ('nome', 'funcao', 'empresa', 'data', 'ativo')

class FuncaoForm(forms.ModelForm):
    class Meta:
        model = Funcao
        fields = ('nome',)

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nome',)