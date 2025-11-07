
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from eventos import views as eventos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eventos.urls')),
]