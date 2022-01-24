from apostador import Apostador

class Guardian(Apostador):
    _guardianes = {}

    def __init__(self, identificacion, nombre, saldo, salario, celdas):
        super().__init__(identificacion, nombre, saldo)
        self.salario = salario
        self.celdas = celdas
        Guardian._guardianes[self.identificacion] = self

    

    