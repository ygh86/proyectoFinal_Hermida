from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView,DetailView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from .models import Evento, Ubicacion
from .forms import EventoFormulario, UbicacionFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
'''
## Vistas para el Blog de Eventos
'''
## home
def index(request):
    context = {
        'titulo': 'Blog de Eventos',
        'mensaje': 'Esta es la entrega final del curso de Python y Django de CoderHouse',
    }
    return render(request, 'blogeventos/index.html',context)

## sobre mi
def about(request):
    context = {
        'titulo': 'Sobre Mi',
        'mensaje': 'Página creada por Yasmin Hermida para la entrega final del curso de Python y Django de CoderHouse. En este blog podrás encontrar información sobre diversos eventos, sus detalles y ubicaciones.',
    }
    return render(request, 'blogeventos/about.html',context)

'''
## Vistas para Eventos
- Listas, Detalles, Crear, Editar, Eliminar
'''
## lista de eventos con buscador
class EventosListView(ListView):
    model = Evento
    template_name = 'blogeventos/evento_list.html'
    context_object_name = 'eventos'
    context = {
        'titulo': 'Eventos'
 }

    def get_queryset(self):
        busqueda = self.request.GET.get('busqueda', '')
        queryset = Evento.objects.all()
        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)
        return queryset.order_by('-fecha_inicio')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busqueda'] = self.request.GET.get('busqueda', '')
        return context

## detalle del evento
class EventoDetailView(DetailView):
    model = Evento
    template_name = 'blogeventos/evento_detail.html'
    context_object_name = 'evento'

## crear eventos
class EventoCreateView(LoginRequiredMixin, CreateView,SuccessMessageMixin):
    model = Evento
    form_class = EventoFormulario
    template_name = 'blogeventos/evento_create.html'
    success_url = reverse_lazy('blogeventos:evento_list')
    context_object_name = 'evento'
    login_url = '/accounts/login/'
    success_message = "El evento '%(nombre)s' fue creado exitosamente."
    def form_valid(self, form):
        form.instance.organizador = self.request.user
        return super().form_valid(form)

## Editar evento
class EventoUpdateView(LoginRequiredMixin,UpdateView,SuccessMessageMixin):
    model = Evento
    form_class = EventoFormulario
    template_name = 'blogeventos/evento_edit.html'
    context_object_name = 'evento'
    login_url = '/accounts/login/'
    success_message = "El evento '%(nombre)s' fue editado exitosamente."
    def get_success_url(self):
        return reverse('blogeventos:evento_detail', kwargs={'pk': self.object.pk})

## Eliminar evento
class EventoDeleteView(LoginRequiredMixin,DeleteView):
    model = Evento
    template_name = 'blogeventos/evento_confirm_delete.html'
    success_url = reverse_lazy('blogeventos:evento_list')
    context_object_name = 'evento'
    login_url = '/accounts/login/'
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(request, f"El evento '{self.object.nombre}' fue eliminado exitosamente.")
        return super().delete(request, *args, **kwargs)

"""
## Vistas para Ubicaciones
- Listas, Crear, Editar, Eliminar
"""
## lista de ubicaciones
class UbicacionListView(ListView):
    model = Ubicacion
    template_name = 'blogeventos/ubicacion_list.html'
    context_object_name = 'ubicaciones'
    queryset = Ubicacion.objects.all()

## crear ubicacion
class UbicacionCreateView(LoginRequiredMixin, CreateView,SuccessMessageMixin):
    model = Ubicacion
    form_class = UbicacionFormulario
    template_name = 'blogeventos/ubicacion_create.html'
    success_url = reverse_lazy('blogeventos:ubicacion_list')
    context_object_name = 'ubicacion'
    login_url = '/accounts/login/'
    success_message = "La ubicación '%(nombre)s' fue creada exitosamente."

## editar ubicacion
class UbicacionUpdateView(LoginRequiredMixin,UpdateView,SuccessMessageMixin):
    model = Ubicacion
    form_class = UbicacionFormulario
    template_name = 'blogeventos/ubicacion_edit.html'
    context_object_name = 'ubicacion'
    login_url = '/accounts/login/'
    success_message = "La ubicación '%(nombre)s' fue editada exitosamente."
    def get_success_url(self):
        return reverse('blogeventos:ubicacion_list')

## eliminar ubicacion
class UbicacionDeleteView(LoginRequiredMixin,DeleteView):
    model = Ubicacion
    template_name = 'blogeventos/ubicacion_confirm_delete.html'
    success_url = reverse_lazy('blogeventos:ubicacion_list')
    context_object_name = 'ubicacion'
    login_url = '/accounts/login/'
    ## evitar eliminar ubicacion si tiene eventos asociados
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Verificar si hay eventos asociados a esta ubicación
        if Evento.objects.filter(ubicacion=self.object).exists():
            messages.error(request, f"No se puede eliminar la ubicación '{self.object.nombre}' porque tiene eventos asociados.")
            return redirect('blogeventos:ubicacion_list')
        
        messages.success(request, f"La ubicación '{self.object.nombre}' se eliminó correctamente.")
        return super().delete(request, *args, **kwargs)

"""
## formulario para crear ubicaciones
@login_required
def ubicacionesFormulario(request):
    if request.method == 'POST':
        form = UbicacionFormulario(request.POST)
        if form.is_valid():
            form.save()
            ubicaciones = Ubicacion.objects.all()
            context = {
                'ubicaciones': ubicaciones,
                'mensaje': 'Ubicación creada exitosamente.'
            }
            return render(request, 'blogeventos/ubicacion_list.html', context)
        else:
            form.add_error(None, "Por favor corrija los errores en el formulario.")
            context = {
                'form': form,
                'mensaje': 'Por favor corrija los errores en el formulario.'
            }
            return render(request, 'blogeventos/ubicacion_crear.html', context)
    else:
        form = UbicacionFormulario()
        context = {
            'form': form
        }
    return render(request, 'blogeventos/ubicacion_crear.html',context)

## Editar ubicacion
def ubicacion_editar(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    if request.method == 'POST':
        form = UbicacionFormulario(request.POST, instance=ubicacion)
        if form.is_valid():
            form.save()
            return render(request, 'blogeventos/ubicacion_list.html', {'ubicaciones': Ubicacion.objects.all(), 'mensaje': 'Ubicación actualizada exitosamente.'})
        else:
            form.add_error(None, "Hay datos que no son correctos.")
            return render(request, 'blogeventos/ubicacion_editar.html', {'form': form, 'ubicacion': ubicacion, 'mensaje': 'Por favor corrija los errores en el formulario.'})
    else:
        form = UbicacionFormulario(instance=ubicacion)
        return render(request, 'blogeventos/ubicacion_editar.html', {'form': form, 'ubicacion': ubicacion})

"""