from django.shortcuts import render
from django.views.generic import ListView

from .models import Producto

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductoForm
from .models import Producto

# --- Login ---
def login_usuario(request):
    if request.method == 'POST':
        # Credenciales
        usuario_txt = request.POST.get('username')
        clave_txt = request.POST.get('password')
        
        user = authenticate(request, username=usuario_txt, password=clave_txt)
        if user is not None:
            login(request, user)

            # Session
            request.session['rol_usuario'] = 'Administrador' if user.is_staff else 'Operador'
            return redirect('tienda:catalogo')
        else:
            messages.error(request, "Credenciales de acceso incorrectas.")
            
    return render(request, 'tienda/login.html')

# --- Logout ---
def logout_usuario(request):
    logout(request)
    return redirect('tienda:login')

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

# --- CRUD PRODUCTOS ---
@login_required(login_url='tienda:login')
def registrar_producto(request):
    """
        Encargado del manejo del formulario de registro
    """
    if request.method == 'POST':
        # ModelForm con datos de la petición HTTP
        form = ProductoForm(request.POST)
        
        # Validaciones
        if form.is_valid():
            form.save()
            messages.success(request, "¡Producto registrado de forma segura y auditada!") # Respuesta
            return redirect('tienda:catalogo')
    else:
        # GET
        form = ProductoForm()
        
    return render(request, 'tienda/registro_producto.html', {'form': form})
