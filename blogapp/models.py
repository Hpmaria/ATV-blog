from django.db import models

# Create your models here.


class CursoRealizado(models.Model):
    nome = models.CharField(max_length=200)  # Nome do curso
    descricao = models.TextField()  # Descrição do curso

    def __str__(self):
        return self.nome

class Gosto(models.Model):
    nome = models.CharField(max_length=200)  # Nome do gosto

    def __str__(self):
        return self.nome


class Postagem(models.Model):
    titulo = models.CharField(max_length=200)  # Título da postagem
    conteudo = models.TextField()  # Conteúdo da postagem
    imagem = models.ImageField(upload_to='postagens/')  # Imagem da postagem

    def __str__(self):
        return self.titulo
