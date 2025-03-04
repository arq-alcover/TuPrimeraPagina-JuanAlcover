from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sent_messages", on_delete=models.CASCADE, verbose_name="Remitente")
    receiver = models.ForeignKey(User, related_name="received_messages", on_delete=models.CASCADE, verbose_name="Destinatario")
    content = models.TextField(verbose_name="Contenido del mensaje")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y hora")

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return f"Mensaje de {self.sender} para {self.receiver} el {self.timestamp.strftime('%d-%m-%Y %H:%M')}"
