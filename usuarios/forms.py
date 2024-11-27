from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
class UsuarioForms(UserCreationForm):
    matricula = forms.CharField(max_length=20, label="Matrícula")
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ['username', 'matricula', 'password1', 'password2']
        labels = {
            'username': 'Usuário:',
            'matricula': 'Matrícula:',
            'password1': 'Senha:',
            'password2': 'Confirme a senha:',
        }


    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError(_("A senha deve ter pelo menos 8 caracteres."))
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password1 != password2:
            raise ValidationError(_("As senhas não correspondem."))
        return password2