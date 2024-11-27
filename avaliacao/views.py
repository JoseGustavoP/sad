from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models import Curso, Disciplina, Comentario
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .forms import DisciplinaForm, ComentarioForm
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Avg
from django.urls import reverse
from django import forms
from django.db import models
class CursoCreate(GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Admin"
    model = Curso
    fields = ['nome']
    template_name = "registrar/registrar_curso.html"
    success_url = reverse_lazy('inicio')

class CursoUpdate(GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Admin"
    model = Curso
    fields = ['nome']
    template_name = "registrar/update_curso.html"
    success_url = reverse_lazy('inicio')

class CursoDelete(GroupRequiredMixin, DeleteView):
    group_required = u"Admin"
    login_url = reverse_lazy('login')
    model = Curso
    template_name = "registrar/excluir-cursos.html"
    success_url = reverse_lazy('inicio')

class CursoList(GroupRequiredMixin, ListView):
    group_required = u"Admin"
    login_url = reverse_lazy('login')
    model = Curso
    template_name = "registrar/listas/cursos.html"

class DisciplinaCreate(GroupRequiredMixin, CreateView):
    group_required = u"Admin"
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'registrar/registrar_disciplina.html'
    success_url = reverse_lazy('inicio')
    

class DisciplinaUpdate(GroupRequiredMixin, UpdateView):
    group_required = u"Admin"
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'registrar/update_disciplina.html'
    context_object_name = 'disciplina'
    success_url = reverse_lazy('listar_disciplinas')

class DisciplinaDelete(GroupRequiredMixin, DeleteView):
    group_required = u"Admin"
    model = Disciplina
    template_name = 'registrar/excluir-disciplina.html'
    context_object_name = 'disciplina'
    success_url = reverse_lazy('listar_disciplinas')

class DisciplinaList(GroupRequiredMixin, ListView):
    group_required = u"Admin"
    model = Disciplina
    template_name = 'registrar/listas/disciplina.html'
    context_object_name = 'disciplinas'


class ComentarioCreate(LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
    model = Comentario
    form_class = ComentarioForm
    template_name = 'disciplinas/forum_disciplina.html'

    def get_success_url(self):
        return reverse_lazy('forum_disciplina', args=[self.kwargs['disciplina_id']])

    def form_valid(self, form):
        disciplina = get_object_or_404(Disciplina, pk=self.kwargs['disciplina_id'])
        form.instance.disciplina = disciplina
        form.instance.autor = self.request.user
        disciplina.save()
        
        return super().form_valid(form)


def forum_disciplina(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    comentarios = Comentario.objects.filter(disciplina=disciplina).order_by('-data_publicacao')

    by_like = request.GET.get("by_like")
    if by_like:
        comentarios = comentarios.annotate(num_curtidas = models.Count("curtida")).order_by("-num_curtidas")
    else:
        comentarios = comentarios.order_by('-data_publicacao')

    # Adiciona um atributo 'user_has_liked' a cada comentário
    for comentario in comentarios:
        comentario.user_has_liked = request.user in comentario.curtida.all()

    # Configurar a paginação
    paginator = Paginator(comentarios, 4)  # 4 comentários por página
    page = request.GET.get('page')

    try:
        comentarios_pagina = paginator.page(page)
    except PageNotAnInteger:
        # Página não é um número inteiro, mostra a primeira página
        comentarios_pagina = paginator.page(1)
    except EmptyPage:
        # Página está fora dos limites, mostra a última página disponível
        comentarios_pagina = paginator.page(paginator.num_pages)

    # Calcular a média de avaliação da disciplina considerando todos os comentários
    media_avaliacao = Comentario.objects.filter(disciplina=disciplina).aggregate(Avg('avaliacao'))['avaliacao__avg']
    media_avaliacao = round(media_avaliacao, 2) if media_avaliacao is not None else 0.0
    # Adiciona o formulário de adicionar comentário
    form = ComentarioForm()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.disciplina = disciplina
            comentario.autor = request.user
            comentario.save()
            return HttpResponseRedirect(reverse('forum_disciplina', args=[disciplina_id]))

    return render(request, 'disciplinas/forum_disciplina.html', {
        'disciplina': disciplina,
        'comentarios': comentarios_pagina,
        'media_avaliacao': media_avaliacao,
        'form': form,
    })


class ComentarioUpate(LoginRequiredMixin ,UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'disciplinas/editar_comentario.html'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(autor=self.request.user)

    def get_success_url(self):
        return reverse_lazy('forum_disciplina', args=[self.object.disciplina.id])

class ComentarioDetail(LoginRequiredMixin ,DetailView):
    login_url = reverse_lazy('login')
    model = Comentario
    template_name = 'disciplinas/detalhes_comentario.html'


class ComentarioDelete(LoginRequiredMixin,DeleteView):
    login_url = reverse_lazy('login')
    model = Comentario
    template_name = 'disciplinas/excluir_comentario.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def get_success_url(self):
        return reverse_lazy('forum_disciplina', args=[self.object.disciplina.id])


def like_comment(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comentario, pk=comment_id)

        if request.user in comment.curtida.all():
            # O usuário já curtiu este comentário, então descurta
            comment.curtida.remove(request.user)
            liked = False
        else:
            # O usuário ainda não curtiu este comentário, então curta
            comment.curtida.add(request.user)
            liked = True

        return JsonResponse({'liked': liked, 'num_likes': comment.curtida.count()})
    else:
        return JsonResponse({'error': 'Você deve estar autenticado para curtir um comentário.'})
    

def edit_comentario_js(request, comment_id):
    if request.user.is_authenticated :
        comment = Comentario.objects.get(pk=comment_id)

        if comment is not None and request.user == comment.autor:
            form = ComentarioForm(instance=comment)
            form.fields["avaliacao"] = forms.CharField(widget=forms.TextInput(attrs={"type": "number", "min":"1", "max":"5"}))
            return render (request, "disciplinas/editar_comentario_js.html", {'object':comment, 'form':form})
        else:            
            return JsonResponse({'error': 'Você deve ser autor do comentário para editá-lo.'})
    else:
        return JsonResponse({'error': 'Você deve estar autenticado para curtir um comentário.'})
        
    

