
from django.urls import path
from .views import EditarEvento, ListaEventos, MisEventos

urlpatterns = [
    path('', ListaEventos.as_view(), name='lista_eventos'),
    path('eventos/', MisEventos.as_view(), name='mis_eventos'),
    path('editar/', EditarEvento.as_view(), name='editar_evento'),
]