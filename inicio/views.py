from django.views.generic import TemplateView
from avaliacao.models import Curso
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cursos"] = Curso.objects.all()
        return context
    

