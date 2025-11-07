from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView
from .models import Evento
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm, LoginForm
from django.shortcuts import render

class RegistroView(CreateView):
    form_class = RegistroForm
    template_name = 'eventos/registro.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'eventos/login.html'
    redirect_authenticated_user = True


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
    template_name = 'eventos/editar_evento.html'
    permission_required = 'eventos.change_evento'
    permission_denied_message = "No tienes permiso para editar eventos."
    
    def handle_no_permission(self):
        # Si no está autenticado, redirige al login
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        
        # Si está autenticado pero no tiene permiso, muestra template personalizado
        return render(self.request, 'eventos/sin_permiso.html', {
            'mensaje': self.get_permission_denied_message(),
            'usuario': self.request.user
        }, status=403)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(autor=self.request.user)
        context['usuario'] = self.request.user
        return context