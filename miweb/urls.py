from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home, 
    buscar, 
    detalle_post, 
    crear_post, 
    crear_categoria, 
    crear_comentario,
    about,
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    path('', home, name='home'),  # Página principal
    path('buscar/', buscar, name='buscar'),  # Buscar posts
    path('pages/<int:post_id>/', detalle_post, name='detalle_post'),  # Vista de un post
    path('pages/new/', crear_post, name='crear_post'),  # Crear un nuevo post
    path('pages/category/', crear_categoria, name='crear_categoria'),  # Crear categoría
    path('pages/comment/', crear_comentario, name='crear_comentario'),  # Agregar comentario
    path('about/', about, name='about'),  # Página "Acerca de"

    # CRUD con Django Class-Based Views
    path('pages/', PostListView.as_view(), name='post_list'),  # Listar posts
    path('pages/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ver post
    path('pages/new/', PostCreateView.as_view(), name='post_create'),  # Crear post
    path('pages/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),  # Editar post
    path('pages/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Eliminar post
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)