from django.urls import path
from . import views
from .views import EventosListView, EventoDetailView, EventoCreateView, EventoUpdateView, EventoDeleteView,UbicacionListView,UbicacionCreateView,UbicacionUpdateView,UbicacionDeleteView

app_name = "blogeventos"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('pages/', EventosListView.as_view(), name='evento_list'),   
    path('pages/crear/', EventoCreateView.as_view(), name='evento_create'),
    path('pages/<int:pk>/', EventoDetailView.as_view(), name='evento_detail'),
    path('pages/<int:pk>/editar/', EventoUpdateView.as_view(), name='evento_edit'),
    path('pages/<int:pk>/eliminar/', EventoDeleteView.as_view(), name='evento_delete'),
    path('ubicacion/', UbicacionListView.as_view(), name='ubicacion_list'),
    path('ubicacion/crear/', UbicacionCreateView.as_view(), name='ubicacion_create'),
    path('ubicacion/<int:pk>/editar/', UbicacionUpdateView.as_view(), name='ubicacion_edit'),
    path('ubicacion/<int:pk>/eliminar/', UbicacionDeleteView.as_view(), name='ubicacion_delete'),

]