# Ejemplo del Patrón Chain of Responsibility en Python

El patrón de diseño **Chain of Responsibility** permite que varios objetos tengan la oportunidad de manejar una solicitud, sin que el remitente necesite saber cuál de los objetos la manejará. Este patrón encadena los objetos receptores y pasa la solicitud a lo largo de la cadena hasta que uno de los objetos la maneje.

Este patrón es útil cuando:
- **Se requiere flexibilidad** para manejar solicitudes sin que el remitente deba conocer el tipo de objeto que procesará la solicitud.
- Se quiere **evitar que un único objeto** tenga que encargarse de todas las solicitudes, distribuyendo el trabajo entre varios objetos.
- Se necesita **un enfoque desacoplado** para manejar solicitudes, de modo que no se necesite modificar el código cada vez que se agrega un nuevo manejador.

### Beneficios
- **Desacoplamiento:** Los objetos que envían solicitudes no están atados a un manejador específico.
- **Flexibilidad:** Se pueden agregar, eliminar o modificar los manejadores sin afectar a otros objetos en la cadena.
- **Mejor mantenimiento:** Permite un manejo modular y escalable de las solicitudes.

## 1. Crear la clase base `Handler`

```python
class Handler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class LowSeverityHandler(Handler):
    def handle(self, request):
        if request["severity"] == "low":
            return f"LowSeverityHandler: Handling {request['severity']} severity request."
        elif self._next_handler:
            return self._next_handler.handle(request)

class MediumSeverityHandler(Handler):
    def handle(self, request):
        if request["severity"] == "medium":
            return f"MediumSeverityHandler: Handling {request['severity']} severity request."
        elif self._next_handler:
            return self._next_handler.handle(request)

class HighSeverityHandler(Handler):
    def handle(self, request):
        if request["severity"] == "high":
            return f"HighSeverityHandler: Handling {request['severity']} severity request."
        elif self._next_handler:
            return self._next_handler.handle(request)

# Crear los objetos manejadores
low_handler = LowSeverityHandler()
medium_handler = MediumSeverityHandler()
high_handler = HighSeverityHandler()

# Configurar la cadena de responsabilidad
low_handler.set_next(medium_handler).set_next(high_handler)

# Solicitudes con diferentes niveles de severidad
requests = [
    {"severity": "low"},
    {"severity": "medium"},
    {"severity": "high"},
    {"severity": "unknown"},
]

# Procesar las solicitudes
for request in requests:
    result = low_handler.handle(request)
    if result:
        print(result)
    else:
        print(f"No handler for {request['severity']} severity request.")
```