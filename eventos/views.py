from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView
from .models import Evento

# Vista pública
class ListaEventos(ListView):
    model = Evento
    template_name = 'Eventos/lista_eventos.html'
    context_object_name = 'eventos'

# Vista privada (solo usuarios autenticados)
class MisEventos(LoginRequiredMixin, ListView):
    model = Evento
    template_name = 'Eventos/mis_eventos.html'
    context_object_name = 'eventos'
    
    def get_queryset(self):
        # Solo muestra posts del usuario logueado
        return Evento.objects.filter(autor=self.request.user)

# Vista con permiso (editar eventos)
class EditarEvento(PermissionRequiredMixin, TemplateView):
    template_name = 'Eventos/editar_evento.html'
    permission_required = 'eventos.change_evento'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(autor=self.request.user)#Eventos.objects.all()
        context['usuario'] = self.request.user
        return context