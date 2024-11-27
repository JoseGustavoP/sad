from django import forms
from .models import Disciplina, Comentario
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Disciplina, Curso, Comentario

class DisciplinaForm(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), empty_label='Selecione um curso')

    class Meta:
        model = Disciplina
        fields = ['nome', 'descricao', 'curso', 'imagem', 'ch', 'sigla']

class ComentarioForm(forms.ModelForm):
    avaliacao = forms.IntegerField(
        label='Avaliação (de 1 a 5)',
        widget=forms.HiddenInput(attrs={'min': 1, 'max': 5}),
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        model = Comentario
        fields = ['texto', 'avaliacao']


