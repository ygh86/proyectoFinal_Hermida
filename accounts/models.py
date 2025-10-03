from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

'''
Modelo Profile para extender el modelo User de Django.
Incluye campos adicionales como imagen, bio y website.
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"
    
    @property
    def imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        return settings.STATIC_URL + 'accounts/img/avatar_default.jpg'

'''
Señal para crear o actualizar el perfil del usuario automáticamente.
'''
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        # Solo guarda si el perfil ya existe
        if hasattr(instance, 'profile'):
            instance.profile.save()
