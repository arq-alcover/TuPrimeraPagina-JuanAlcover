from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear-comentario/', views.crear_comentario, name='crear_comentario'),
    path('buscar/', views.buscar, name='buscar'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
]