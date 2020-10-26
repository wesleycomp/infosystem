from django import forms
from .models import Funcao


class FuncaoForm(forms.ModelForm):

    class Meta:
        model = Funcao
        fields = (
            'descricao',
            'cbo'
        )
