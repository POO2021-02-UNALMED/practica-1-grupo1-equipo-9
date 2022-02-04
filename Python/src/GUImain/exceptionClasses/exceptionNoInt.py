from tkinter import messagebox
from .errorEnCampos import ErrorEnCampos

class ExceptionNoInt(ErrorEnCampos):

    def __init__(self, mensaje, dato):
        mssg = "ExceptionNoInt: " + mensaje
        super().__init__(mssg)
        self.checkValue(dato)


    def checkValue(self, dato):
        try:
            float(dato) 
        except:
            raise self
    
    def messbox(self):
        messagebox.showwarning("ERROR!", self.error)
