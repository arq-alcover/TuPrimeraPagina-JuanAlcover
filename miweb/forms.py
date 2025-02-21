from django import forms
from .models import Post, Categoria, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen_portada', 'categoria', 'etiquetas']
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'imagen_portada': 'Imagen Principal (Recomendado 1200x630px)',
            'categoria': 'Categoría',
            'etiquetas': 'Etiquetas (separadas por comas)'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Mi primer post'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control editor-textarea',
                'rows': 5,
                'placeholder': 'Escribe el contenido del post...'
            }),
            'imagen_portada': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'etiquetas': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Tecnología, Viajes...'
            })
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre de la categoría'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Tecnología, Viajes...'
            })
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['post', 'autor', 'texto']
        labels = {
            'post': 'Seleccionar Post',
            'autor': 'Autor',
            'texto': 'Comentario'
        }
        widgets = {
            'post': forms.Select(attrs={
                'class': 'form-select'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tu nombre o alias'
            }),
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escribe tu comentario aquí...'
            })
        }

class BusquedaForm(forms.Form):
    query = forms.CharField(
        label='Buscar posts',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: Django, Programación...'
        })
    )