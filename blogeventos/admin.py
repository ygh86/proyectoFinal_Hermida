from django.contrib import admin
from .models import Evento, Ubicacion

# Register your models here.
admin.site.register(Evento)
admin.site.register(Ubicacion)