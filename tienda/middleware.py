import logging

logger = logging.getLogger(__name__)

class AuditoriaAccesoMiddleware:
    """
        Middleware personalizado para interceptar las llamadas a la API
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Interceptación del Request
        usuario = request.user if request.user.is_authenticated else "Anónimo"
        path = request.path
        metodo = request.method
        
        # Verificación
        print(f"[AUDITORÍA BACKEND] Usuario: {usuario} | Ruta: {path} | Método: {metodo}")

        # Flujo de la apps
        response = self.get_response(request)

        # (AI)[Retornar respuesta intacta] => [Retornar la respuesta directamente]
        return response