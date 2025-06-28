from django.shortcuts import render
from .models import Curso

def vista_principal(request):
    cursos = Curso.objects.all()
    return render(request, 'contenido/inicio.html', {'cursos': cursos})
