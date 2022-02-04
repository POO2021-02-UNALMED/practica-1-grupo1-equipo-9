from tkinter import messagebox
from .errorInconsistencias import ErrorInconsistencias

class ErrorInconsistenciaGeneros(ErrorInconsistencias):

    def __init__(self, mensaje, gen1, gen2):
        mssg = "ErrorInconsistenciaGeneros: " + mensaje
        super().__init__(mssg)
        self.checkValue(gen1, gen2)

    def checkValue(self, gen1, gen2):
        if gen1 is not gen2:
            raise self
    
    def messbox(self):
        messagebox.showwarning("ERROR!", self.error)