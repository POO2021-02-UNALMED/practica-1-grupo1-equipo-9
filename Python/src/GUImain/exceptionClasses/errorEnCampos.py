from .errorAplicacion import ErrorAplicacion

class ErrorEnCampos(ErrorAplicacion):
    def __init__(self, mensaje):
        super().__init__("ErrorEnCampos: " + mensaje)
