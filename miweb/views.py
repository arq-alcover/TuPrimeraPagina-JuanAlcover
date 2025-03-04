from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categoria, Comentario
from .forms import PostForm, CategoriaForm, ComentarioForm, BusquedaForm

# Página de inicio con lista de posts
def home(request):
    posts = Post.objects.all()
    return render(request, 'miweb/home.html', {'posts': posts})

# Vista para crear un post asegurando que la imagen se guarda en media/
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Permite manejar archivos
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user  # Asigna el autor al usuario autenticado
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'miweb/crear_post.html', {'form': form})

# Búsqueda de posts
def buscar(request):
    form = BusquedaForm(request.GET or None)
    resultados = None
    if form.is_valid():
        query = form.cleaned_data['query']
        resultados = Post.objects.filter(titulo__icontains=query)
    return render(request, 'miweb/resultados_busqueda.html', {'form': form, 'resultados': resultados})

# Creación de categoría
def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'miweb/crear_categoria.html', {'form': form})

# Creación de comentario
def crear_comentario(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'miweb/crear_comentario.html', {'form': form})

# Vista detallada de un post asegurando que la imagen se maneje correctamente
def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'miweb/detalle_post.html', {'post': post})

# Página "Acerca de"
def about(request):
    return render(request, "miweb/about.html")

# CRUD con Django Class-Based Views

class PostListView(ListView):
    model = Post
    template_name = "miweb/post_list.html"
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = "miweb/post_detail.html"
    context_object_name = "post"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "miweb/post_form.html"
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asigna el autor del post automáticamente
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "miweb/post_form.html"
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "miweb/post_confirm_delete.html"
    success_url = reverse_lazy('post_list')
