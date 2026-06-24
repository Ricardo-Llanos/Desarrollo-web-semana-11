import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import escape
from .models import Producto

class ProductoForm(forms.ModelForm):
    """
        Formulario de Productos.
            - Aplica validaciones sobre los campos
            - Limpia la información antes de su ingreso
    """
    class Meta:

        model = Producto
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Ej. Laptop Pro 15'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-lg rows-3', 'placeholder': 'Detalles...'}),
            'precio': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg', 'step': '0.01'}),
        }

    """
        Limpia el campo de nombre
            - Permite eliminar los espacios dentro del campo
            - Permite eliminar toda clase de caracter no permitido
            - Permite escapar la información HTML ( < > )
    """
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        # Remover espacios / Escapar HTML
        nombre_sanitizado = escape(nombre.strip())
        
        # Eliminar caracteres especiales
        if not re.match(r'^[a-zA-Z0-9\sñÑáéíóúÁÉÍÓÚ\-\.]+$', nombre_sanitizado):
            raise ValidationError("El nombre contiene caracteres especiales no permitidos.")
        
        return nombre_sanitizado

    """
        Limpia el campo de descripción
            - Permite eliminar los espacios dentro del campo
            - Permite escapar el contenido HTML
            - Establece que la descripción no pueda ser del mismo nombre que el nombre del producto
    """
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')

        # Escapar HTML
        if descripcion:
            cleaned_data['descripcion'] = escape(descripcion.strip())

        # nombre != descripcion
        if nombre and descripcion and nombre.lower() == descripcion.lower():
            self.add_error('descripcion', "La descripción no puede ser idéntica al nombre del producto.")
            
        return cleaned_data