from django.db import models
from django.contrib.auth.models import User
import os

# Función para almacenar imágenes sin subcarpetas
def upload_to_media(instance, filename):
    return filename

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de categoría")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        
    def __str__(self):
        return self.nombre

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    titulo = models.CharField(max_length=200, verbose_name="Título")
    contenido = models.TextField(verbose_name="Contenido")
    imagen_portada = models.ImageField(
        upload_to=upload_to_media,  # Guarda las imágenes sin subcarpetas
        verbose_name="Imagen de Portada",
        null=True,
        blank=True,
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoría"
    )
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    etiquetas = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Etiquetas",
        help_text="Separadas por comas"
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo

    @property
    def imagen_url(self):
        """Devuelve la URL de la imagen de portada o una imagen por defecto si no tiene."""
        if self.imagen_portada and hasattr(self.imagen_portada, 'url'):
            return self.imagen_portada.url
        return "/static/images/default-post.jpg"  # Imagen por defecto para posts sin imagen

class Comentario(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comentarios',
        verbose_name="Artículo relacionado"
    )
    autor = models.CharField(max_length=100, verbose_name="Autor")
    texto = models.TextField(verbose_name="Contenido del comentario")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Comentario de {self.autor} en {self.post.titulo}"
