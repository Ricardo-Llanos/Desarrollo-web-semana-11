from django.db import models

# Create your models here.
class Producto(models.Model):
    """
        Modelo de la tabla Producto
    """

    # El "id" no se define manualmente ya que Django lo manejará

    nombre = models.CharField(
        max_length=150, 
        verbose_name="Nombre del Producto"
    )
    
    descripcion = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Descripción"
    )
    
    # IA: [inexistencia del campo max_index] → Solución manual: [Cambiar por max_digits].
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Precio"
    )
    
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Fecha de Registro"
    )

    def __str__(self):
        # Devolvemos el valor para identificar el producto
        return self.nombre