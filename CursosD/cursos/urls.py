from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_principal, name='Principal'),  # <-- El nombre 'Principal' es el que usas en el template
]
