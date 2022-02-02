from .errorAplicacion import ErrorAplicacion

class ExceptionC2(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__("ExceptionC2: " + mensaje)
