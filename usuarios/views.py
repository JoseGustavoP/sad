
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from .forms import UsuarioForms
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth import login, logout


class UsuarioCreate(CreateView):
    template_name = "usuarios/form.html"
    form_class = UsuarioForms
    success_url = reverse_lazy('inicio')
    #coloca o usuario em um grupo, nessa caso o de aluno
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Alunos")
        url = super().form_valid(form)

        # Alterar para user, não object
        user = form.save()
        user.groups.add(grupo)

        # Faça login automaticamente após o registro
        login(self.request, user)
        
        return url


class AlterarSenhaView(PasswordChangeView):
    template_name = 'usuarios/alterar_senha.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        messages.success(self.request, 'Senha alterada com sucesso.')
        return super().form_valid(form)

def minha_view_de_logout(request):
    logout(request)
    return redirect('login')