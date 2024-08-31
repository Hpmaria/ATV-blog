

# Create your views here.

from django.shortcuts import render
from .models import *


def postagens(request):
    postagens = Postagem.objects.all()  # Buscando todas as postagens
    return render(request, 'blogapp/index.html', {'postagens': postagens})


def sobre(request):
    cursos = CursoRealizado.objects.all()  # Buscando todos os cursos realizados
    gostos = Gosto.objects.all()  # Buscando todos os gostos
    return render(request, 'blogapp/sobre.html', {'cursos': cursos, 'gostos': gostos})
