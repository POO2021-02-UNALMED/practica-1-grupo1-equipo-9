class Apostador:
    def __init__(self, identificacion: int, nombre: str, saldo: int):
        self.identificacion = identificacion
        self.nombre = nombre
        self.saldo = saldo

    def aumentarSaldo(self, dinero: int):
        self.saldo += dinero

    def reducirSaldo(self, dinero: int):
        self.saldo -= dinero

    def getIdentificacion(self):
        return self.identificacion
    def setIdentificacion(self, identificacion: int):
        self.identificacion = identificacion

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre: str):
        self.nombre = nombre

    def getSaldo(self):
        return self.saldo
    def setSaldo(self, saldo: int):
        self.saldo = saldo