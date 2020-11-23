from django.forms import ModelForm, Textarea, TextInput
from crispy_forms.layout import Submit, Layout
from .models import *


class FuncaoForm(ModelForm):
    class Meta:
        model = Funcao
        fields = '__all__'





