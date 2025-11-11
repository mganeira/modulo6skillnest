from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock']
    list_filter = ['precio']
    search_fields = ['nombre', 'descripcion']
    
    # Controla quién puede ver productos
    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('gestion_prod.can_view_producto')
    
    # Controla quién puede editar productos
    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('gestion_prod.can_edit_producto')
    
    # Controla quién puede eliminar productos
    def has_delete_permission(self, request, obj=None):
        return request.user.has_perm('gestion_prod.can_delete_producto')
    
    # Controla quién puede agregar productos
    def has_add_permission(self, request):
        return request.user.has_perm('gestion_prod.can_edit_producto')
