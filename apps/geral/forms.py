from django import forms

from .models import Categoria


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        # filds = ['nome', 'descrição', 'tipo'] mostra apenas os campos listados
        # filds = '__all__'   mostra todos os campos
        exclude = ['usuario']
