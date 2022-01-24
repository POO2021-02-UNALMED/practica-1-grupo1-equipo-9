class Apostador:
    def __init__(self, identificacion, nombre, saldo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.saldo = saldo

    def aumentarSaldo(self, dinero):
        self.saldo += dinero

    def reducirSaldo(self, dinero):
        self.saldo -= dinero

    def getIdentificacion(self):
        return self.identificacion
    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion

    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    def getSaldo(self):
        return self.saldo
    def setSaldo(self, saldo):
        self.saldo = saldo