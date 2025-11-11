
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from gestion_prod import views as gestion_prod_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gestion_prod.urls')),
]