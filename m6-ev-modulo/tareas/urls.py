from .views import home, agregar_tarea, eliminar_tarea, detalles_tarea, lista_tareas, login_view, registrarse_view, cerrar_sesion_view
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('tareas/', lista_tareas, name='lista_tareas'),
    path('tareas/agregar/', agregar_tarea, name='agregar_tarea'),
    path('tareas/eliminar/<int:tarea_id>/', eliminar_tarea, name='eliminar_tarea'),
    path('tareas/detalles/<int:tarea_id>/', detalles_tarea, name='detalles_tarea'),
    path('login/', login_view, name='login'),
    path('registrarse/', registrarse_view, name='registrarse'),
    path('cerrar_sesion/', cerrar_sesion_view, name='cerrar_sesion'),
]