from .errorAplicacion import ErrorAplicacion

class ErrorInconsistencias(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__("ErrorInconsistencias: " + mensaje)
