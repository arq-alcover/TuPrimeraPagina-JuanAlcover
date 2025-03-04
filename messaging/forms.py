from django import forms
from .models import Message
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all().exclude(is_superuser=True),  # Excluir superusuarios
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Destinatario"
    )

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Escribe tu mensaje aquí...'
        }),
        label="Mensaje"
    )

    class Meta:
        model = Message
        fields = ['receiver', 'content']
