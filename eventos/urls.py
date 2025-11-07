from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    EditarEvento, ListaEventos, MisEventos, 
    RegistroView, CustomLoginView
)

urlpatterns = [
    path('', ListaEventos.as_view(), name='lista_eventos'),
    path('eventos/', MisEventos.as_view(), name='mis_eventos'),
    path('editar/', EditarEvento.as_view(), name='editar_evento'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', RegistroView.as_view(), name='registro'),
]