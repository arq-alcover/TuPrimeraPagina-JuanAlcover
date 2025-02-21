from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Categoria, Comentario
from .forms import PostForm, CategoriaForm, ComentarioForm, BusquedaForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'miweb/home.html', {'posts': posts})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'miweb/crear_post.html', {'form': form})

# Repite lógica similar para crear_categoria y crear_comentario

def buscar(request):
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            resultados = Post.objects.filter(titulo__icontains=query)
            return render(request, 'miweb/resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'miweb/buscar.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'miweb/crear_categoria.html', {'form': form})

def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ComentarioForm()
    return render(request, 'miweb/crear_comentario.html', {'form': form})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'miweb/detalle_post.html', {'post': post})