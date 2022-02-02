class ErrorAplicacion(Exception):
    def __init__(self, mensaje): 
        self.error = "Manejo de errores de la Aplicación: " + mensaje
        super().__init__(self.error)
