from tkinter import messagebox
from .errorInconsistencias import ErrorInconsistencias

class ExceptionSalarioInsuficiente(ErrorInconsistencias):

    def __init__(self, saldo, apuesta):
        mssg = "ExceptionSalarioInsuficiente: Este apostador no tiene el saldo suficiente para realizar esta apuesta"
        super().__init__(mssg)
        self.checkValue(saldo, apuesta)


    def checkValue(self, saldo, apuesta):
        if saldo < apuesta:
            raise self
    
    def messbox(self):
        messagebox.showwarning("ERROR!", self.error)
