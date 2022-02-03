from tkinter import messagebox
from .errorEnCampos import ErrorEnCampos

class ExceptionValorNegativo(ErrorEnCampos):

    def __init__(self, mensaje, dato):
        mssg = "ExceptionValorNegativo: " + mensaje
        super().__init__(mssg)
        self.checkValue(dato)


    def checkValue(self, dato):
        if dato < 0:
            raise self
    
    def messbox(self):
        messagebox.showwarning("ERROR!", self.error)
