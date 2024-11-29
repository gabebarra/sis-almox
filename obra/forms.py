from django import forms
from .models import *
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, HTML, Field


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ('nome','local','data','cliente')

    data = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date',
            'value': datetime.now().strftime("%Y-%m-%d")}
        )
    )

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome',)