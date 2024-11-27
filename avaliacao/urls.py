from django.urls import path
from .views import (
    CursoCreate, CursoUpdate, CursoDelete, CursoList,
    DisciplinaList, DisciplinaCreate, DisciplinaUpdate, DisciplinaDelete, forum_disciplina,
    ComentarioCreate, ComentarioUpate, ComentarioDetail, ComentarioDelete, like_comment, edit_comentario_js
)

urlpatterns = [
    path('cadastrar/curso/', CursoCreate.as_view(), name="cadastrar-curso"),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name="editar-curso"),
    path('excluir/curso/<int:pk>/', CursoDelete.as_view(), name="excluir-curso"),
    path('listar/curso/', CursoList.as_view(), name="listar-curso"),

    path('listar/disciplinas/', DisciplinaList.as_view(), name='listar_disciplinas'),
    path('cadastrar/disciplina/', DisciplinaCreate.as_view(), name='adicionar_disciplina'),
    path('editar/disciplina/<int:pk>/', DisciplinaUpdate.as_view(), name='editar_disciplina'),
    path('excluir/disciplina/<int:pk>/', DisciplinaDelete.as_view(), name='excluir_disciplina'),

    path('forum/<int:disciplina_id>/', forum_disciplina, name='forum_disciplina'),
    
    path('editar_comentario/<int:pk>/', ComentarioUpate.as_view(), name='editar_comentario'),
    path('editar_comentario_js/<int:comment_id>/', edit_comentario_js, name='editar_comentario_js'),
    path('detalhes_comentario/<int:pk>/', ComentarioDetail.as_view(), name='detalhes_comentario'),
    path('excluir_comentario/<int:pk>/', ComentarioDelete.as_view(), name='excluir_comentario'),
    path('like-comment/<int:comment_id>/', like_comment, name='like_comment')
]
