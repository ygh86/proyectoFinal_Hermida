from django import forms
from .models import Evento, Ubicacion
from django_ckeditor_5.widgets import CKEditor5Widget
'''
Formulario para crear y editar eventos y ubicaciones.
'''
class EventoFormulario(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion','resumen', 'fecha_inicio', 'fecha_fin', 'ubicacion', 'imagen']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'fecha_fin': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }
        labels = {
            'nombre': 'Nombre del Evento',
            'descripcion': 'Descripción',
            'fecha_inicio': 'Fecha y Hora de Inicio',
            'fecha_fin': 'Fecha y Hora de Fin',
            'ubicacion': 'Ubicación',
            'imagen': 'Imagen del Evento',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre del evento (máximo 100 caracteres).',
            'descripcion': 'Ingrese una breve descripción del evento.',
            'fecha_inicio': 'Seleccione la fecha y hora de inicio del evento.',
            'fecha_fin': 'Seleccione la fecha y hora de fin del evento.',
            'ubicacion': 'Seleccione la ubicación del evento.',
        }
        error_messages = {
            'nombre': {
                'max_length': 'El nombre del evento no puede exceder los 100 caracteres.',
                'required': 'El nombre del evento es obligatorio.',
            },
            'fecha_inicio': {
                'invalid': 'Ingrese una fecha y hora de inicio válida.',
                'required': 'La fecha y hora de inicio es obligatoria.',
            },
            'fecha_fin': {
                'invalid': 'Ingrese una fecha y hora de fin válida.',
                'required': 'La fecha y hora de fin es obligatoria.',
            },
            'ubicacion': {
                'required': 'La ubicación es obligatoria.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            raise forms.ValidationError("La fecha y hora de inicio debe ser anterior a la fecha y hora de fin.")    
        return cleaned_data

'''
Formulario para crear y editar ubicaciones.
'''
class UbicacionFormulario(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre', 'direccion', 'ciudad', 'pais']
        labels = {
            'nombre': 'Nombre de la Ubicación',
            'direccion': 'Dirección',
            'ciudad': 'Ciudad',
            'pais': 'País',
        }
        help_texts = {
            'nombre': 'Ingrese el nombre de la ubicación (máximo 100 caracteres).',
            'direccion': 'Ingrese la dirección (máximo 200 caracteres).',
            'ciudad': 'Ingrese la ciudad (máximo 100 caracteres).',
            'pais': 'Ingrese el país (máximo 100 caracteres).',
        }
        error_messages = {
            'nombre': {
                'max_length': 'El nombre de la ubicación no puede exceder los 100 caracteres.',
                'required': 'El nombre de la ubicación es obligatorio.',
            },
            'direccion': {
                'max_length': 'La dirección no puede exceder los 200 caracteres.',
                'required': 'La dirección es obligatoria.',
            },
            'ciudad': {
                'max_length': 'La ciudad no puede exceder los 100 caracteres.',
                'required': 'La ciudad es obligatoria.',
            },
            'pais': {
                'max_length': 'El país no puede exceder los 100 caracteres.',
                'required': 'El país es obligatorio.',
            },
        }