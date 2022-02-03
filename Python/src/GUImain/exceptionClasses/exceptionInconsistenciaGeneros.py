from tkinter import messagebox
from .errorInconsistencias import ErrorInconsistencias

class ErrorInconsistenciaGeneros(ErrorInconsistencias):

    def __init__(self, mensaje):
        mssg = "ErrorInconsistenciaGeneros: " + mensaje
        super().__init__(mssg)

    def checkValue(self):
        pass
    
    def messbox(self):
        messagebox.showwarning("ERROR!", self.error)