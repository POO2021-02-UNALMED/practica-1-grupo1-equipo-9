from tkinter import messagebox
from .exceptionC1 import ExceptionC1

class ExceptionCampoVacio(ExceptionC1):

    def __init__(self, *values):
        super().__init__("ExceptionCampoVacio: Existe algún campo vacío")
        self.checkValues(values)


    def checkValues(self, values):
        for v in values:
            if str(v).strip() == "":
                raise self
    
    def messbox(self):
        messagebox.showwarning("ERROR!", self.error)



if __name__ == "__main__":
    try:
        ExceptionCampoVacio(1,3,"dad","")
    except ExceptionCampoVacio as f:
        f.messbox()
