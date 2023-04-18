from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

LISTA_CATEGORIAS = (
    ("GESTAO", "Gestão "),
    ("EDUCACAO_PERMANENTE_E_CONTINUADA", "Educação Permanente e Continuada"),
    ("PESQUISA_EM_ENFERMAGEM_E_SAUDE", "Pesquisa em enfermagem e saúde"),
    ("DEV_DE_PROJETO_E_PESQUISA", "Desenvolvimento de projetos e pesquisas"),
)

# criar o filme



class Filme(models.Model):
     thumb = models.ImageField(upload_to='thumb_filmes')
     titulo = models.CharField(max_length=100)
     descricao = models.TextField(max_length=1000)
     categoria = models.CharField(max_length=150, choices=LISTA_CATEGORIAS)
     visualizacoes= models.IntegerField(default=0)
     data_criacao = models.DateTimeField(default=timezone.now)


     def __str__(self):
         return self.titulo

#criar os episodios

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo

class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")



# criar o usuário
