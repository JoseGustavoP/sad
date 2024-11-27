from django.contrib import admin
from .models import Curso, Disciplina, Comentario


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ["curso", "sigla", "nome", "ch"]

admin.site.register(Disciplina, DisciplinaAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ["nome"]

admin.site.register(Curso, CursoAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ["data_publicacao","disciplina","autor" ]

admin.site.register(Comentario, ComentarioAdmin)
