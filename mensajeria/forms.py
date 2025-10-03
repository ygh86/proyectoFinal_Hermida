from django import forms
from .models import Mensaje

'''
clase para el formulario de envío de mensajes
'''
class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ["contenido"]
        widgets = {
            "contenido": forms.Textarea(attrs={"rows": 2, "placeholder": "Escribe un mensaje..."})
        }