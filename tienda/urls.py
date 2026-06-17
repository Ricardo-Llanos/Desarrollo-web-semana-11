from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    # --- Ruta de Home ---
    path('', views.home, name='home'),
    
    # --- Ruta - Catálogo ---
        # IA: [inexistencia del método as_index()] → Solución manual: [Cambiar por as_view()].
    path('catalogo/', views.ProductoListView.as_view(), name='catalogo'),

]