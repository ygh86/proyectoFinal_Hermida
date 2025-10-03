from django.db import models
#from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User

# Create your models here.
'''
Modelos para la app blogeventos
    Modelo Principal: Evento
    Modelos secundarios: Ubicacion
'''
 # modelo Principal:
class Evento(models.Model): 
    nombre = models.CharField(max_length=100)
    descripcion = CKEditor5Field('Text', config_name='extends')
    resumen = models.CharField(max_length=200,null=True, blank=True)
    fecha_inicio = models.DateTimeField() 
    fecha_fin = models.DateTimeField()
    organizador = models.ForeignKey(User, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE) 
    imagen = models.ImageField(upload_to='media/')
    
    def __str__(self): 
        return f"{self.nombre} ( {self.fecha_inicio.date()} ) - {self.ubicacion.nombre}"

# Modelo 2:
class Ubicacion(models.Model): 
    nombre = models.CharField(max_length=100) 
    direccion = models.CharField(max_length=200) 
    ciudad = models.CharField(max_length=100) 
    pais = models.CharField(max_length=100) 
    
    def __str__(self): 
        return f"{self.nombre} - ( {self.ciudad}, {self.pais} )"
    
