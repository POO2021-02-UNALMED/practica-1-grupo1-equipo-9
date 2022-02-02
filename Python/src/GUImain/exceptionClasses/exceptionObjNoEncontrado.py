from tkinter import messagebox
from .exceptionC2 import ExceptionC2

class ExceptionObjNoEncontrado(ExceptionC2):

    def __init__(self, mensaje, dato, datos):
        mssg = "ExceptionObjNoEncontrado: " + mensaje
        super().__init__(mssg)
        self.checkValue(dato, datos)


    def checkValue(self, dato, datos):
        if dato not in datos:
            raise self
    
    def messbox(self):
        messagebox.showwarning("ERROR!", self.error)
