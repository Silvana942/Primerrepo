from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect

from apps.post.forms import CategoriaForm
from .models import Categoria

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def ver_categorias(request):
    lista_categorias = Categoria.objects.all()
    template = 'post/ver_categorias.html'
    contexto = {
        'categorias':lista_categorias
    }
    return render(request, template, contexto)

def crear_categorias(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST or None)
        if formulario.is_valid():
            formulario.save()
            return redirect('ver_categorias')
    else:
        formulario = CategoriaForm()
    template = 'post/crear_categorias.html'
    contexto = {
        'formulario':formulario
    }
    return render(request, template, contexto)
