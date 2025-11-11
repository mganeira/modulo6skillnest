from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    EditarProducto, ListaProductos, MisProductos, 
    RegistroView, CustomLoginView
)

urlpatterns = [
    path('', ListaProductos.as_view(), name='lista_Productos'),
    path('Productos/', MisProductos.as_view(), name='mis_Productos'),
    path('editar/', EditarProducto.as_view(), name='editar_Producto'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', RegistroView.as_view(), name='registro'),
]