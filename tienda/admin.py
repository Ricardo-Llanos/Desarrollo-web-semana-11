from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # IA: [Restricciones de visibilidad] → Solución manual: [Control de visibilidad por medio de exclusión de visibilidad del campo].
        # --- Campos visibles ---
    list_display = ('id', 'nombre_en_mayuscula', 'precio', 'fecha_creacion')
    
        # --- Filtros laterales y barras de búsqueda ---
    list_filter = ('fecha_creacion', 'precio')
    search_fields = ('nombre', 'descripcion')
    
        # --- Campos de solo lectura ---
    readonly_fields = ('fecha_creacion',)
    
        # --- Control de visibilidad ---
    exclude = ('costo_proveedor',) 

        # Acciones masivas personalizadas de gestión operativa
    actions = ['aplicar_descuento_diez']
    
    # Decorador
    @admin.display(description='Producto (Mayúsculas)')
    def nombre_en_mayuscula(self, obj):
        return obj.nombre.upper()


    # Acción (dsct)
    @admin.action(description='Aplicar 10% de descuento masivo')
    def aplicar_descuento_diez(self, request, queryset):
        for producto in queryset:
            producto.precio = producto.precio * 0.90
            producto.save()

        self.message_user(request, f"Se redujo con éxito el precio a {queryset.count()} productos.")