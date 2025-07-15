from django import forms
from .models import Diretoria

class DiretoriaForm(forms.ModelForm):
    class Meta:
        model = Diretoria
        fields = ['cargo', 'nome', 'contato']