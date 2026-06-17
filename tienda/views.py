from django.shortcuts import render
from django.views.generic import ListView

from .models import Producto

# Create your views here.

# --- Home ---
def home(request):
    """
        Vista encargado de mostrar la página de bienvenida.
    """
    
    contexto = {
        'message': 'Bienvenido al entorno de desarrollo Django 5.2'
    }

    return render(request, 'tienda/base.html', contexto)

# --- Catálogo ---
class ProductoListView(ListView):
    """
        Vista encargada de mostrar el catálogo de productos del sistema.
    """

    model = Producto
    template_name = 'tienda/catalogo.html'
    
    context_object_name = 'productos' 

    def get_context_data(self, **kwargs):
        # Establecemos "**kwargs" para permitir establecer nuevos parámetros adicionales al método original
        context = super().get_context_data(**kwargs) 

        context['titulo_pagina'] = 'Catálogo Oficial de Productos'
        
        return context