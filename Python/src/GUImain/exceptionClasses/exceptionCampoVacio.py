from tkinter import messagebox
from .errorEnCampos import ErrorEnCampos

class ExceptionCampoVacio(ErrorEnCampos):

    def __init__(self, *values):
        super().__init__("ExceptionCampoVacio: Existe algún campo vacío")
        self.checkValues(values)


    def checkValues(self, values):
        for v in values:
            if str(v).strip() == "":
                raise self
    
    def messbox(self):
        messagebox.showwarning("ERROR!", self.error)

