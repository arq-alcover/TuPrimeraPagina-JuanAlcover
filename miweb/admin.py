from django.contrib import admin
from .models import Post, Categoria, Comentario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_publicacion", "categoria")
    search_fields = ("titulo", "etiquetas")
    list_filter = ("categoria", "fecha_publicacion")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("autor", "post", "fecha_creacion")
    search_fields = ("autor", "texto")
    list_filter = ("fecha_creacion",)
