from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView
from .models import producto
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render


# Vista pública
class ListaProductos(ListView):
    model = producto
    template_name = 'gestion_prod/lista_productos.html'
    context_object_name = 'productos'

# Vista privada (solo usuarios autenticados)
class MisProductos(LoginRequiredMixin, ListView):
    model = producto
    template_name = 'gestion_prod/mis_productos.html'
    context_object_name = 'productos'
    
    def get_queryset(self):
        # Solo muestra posts del usuario logueado
        return producto.objects.filter(autor=self.request.user)


# Vista con permiso (editar productos)
class EditarProducto(PermissionRequiredMixin, TemplateView):
    template_name = 'gestion_prod/editar_producto.html'
    permission_required = 'productos.change_producto'
    permission_denied_message = "No tienes permiso para editar productos."
    
    def handle_no_permission(self):
        # Si no está autenticado, redirige al login
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        
        # Si está autenticado pero no tiene permiso, muestra template personalizado
        return render(self.request, 'gestion_prod/sin_permiso.html', {
            'mensaje': self.get_permission_denied_message(),
            'usuario': self.request.user
        }, status=403)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = producto.objects.filter(autor=self.request.user)
        context['usuario'] = self.request.user
        return context