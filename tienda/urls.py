from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    # --- Ruta de Home ---
    path('', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    
    # --- Ruta - Catálogo ---
        # IA: [inexistencia del método as_index()] → Solución manual: [Cambiar por as_view()].
    path('catalogo/', views.ProductoListView.as_view(), name='catalogo'),

    path('producto/nuevo/', views.registrar_producto, name='registrar_producto'),
]   