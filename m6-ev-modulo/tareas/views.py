from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'tareas/home.html'   )

@login_required
def lista_tareas(request):
    # Aquí iría la lógica para obtener las tareas desde la base de datos
    tareas = []  # Esto debería ser reemplazado por una consulta real
    return render(request, 'tareas/lista_tareas.html', {'tareas': tareas})  

@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        # Aquí iría la lógica para agregar una nueva tarea
        pass
    return render(request, 'tareas/agregar_tarea.html')

@login_required
def eliminar_tarea(request, tarea_id): 
    # Aquí iría la lógica para eliminar una tarea por su ID
    pass
    return render(request, 'tareas/eliminar_tarea.html', {'tarea_id': tarea_id})

@login_required
def detalles_tarea(request, tarea_id):
    # Aquí iría la lógica para obtener los detalles de una tarea por su ID
    tarea = None  # Esto debería ser reemplazado por una consulta real
    return render(request, 'tareas/detalles_tarea.html', {'tarea': tarea})

def login_view(request):
    return render(request, 'tareas/login.html')

def registrarse_view(request):
    return render(request, 'tareas/registrarse.html')

def cerrar_sesion_view(request):
    return render(request, 'tareas/cerrar_sesion.html')