from django.db import models
from django.contrib.auth.models import User
'''
Modelo para representar un chat entre dos usuarios y los mensajes dentro de ese chat.
'''
class Chat(models.Model):
    usuario_emisor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chats_iniciados"
    )
    usuario_receptor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="chats_recibidos"
    )
    fecha_creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario_emisor', 'usuario_receptor')
        ordering = ['-fecha_creado']

    def __str__(self):
        return f"Chat entre {self.usuario_emisor.username} y {self.usuario_receptor.username}"

'''
Modelo para representar un mensaje dentro de un chat.
'''
class Mensaje(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="mensajes")
    usuario_remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_enviado = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['fecha_enviado']

    def __str__(self):
        return f"{self.usuario_remitente.username}: {self.contenido[:20]}"
