from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def get_disciplinas(self):
        lista = Disciplina.objects.filter(curso__id = self.id).order_by('nome')        
        return lista

    def __str__(self):
        return "{}".format(self.nome)

class Disciplina(models.Model):
    sigla = models.CharField(max_length=4, null=False)
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(null=False)
    ch = models.PositiveIntegerField(null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False)
    avaliacao_media = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)  
    imagem = models.ImageField(upload_to='static/img', null=True) 

    def __str__(self):
        return "{} ({})".format(self.sigla, self.curso)


class Comentario(models.Model):
    texto = models.TextField(max_length=469)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    curtida = models.ManyToManyField(User, related_name='comentarios_curtidos', blank=True)
    avaliacao = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])  # Adicionado campo de avaliação

    def __str__(self):
        return f"Nome{self.autor} Comentário {self.pk} Data{self.data_publicacao}"

    
