from apostador import Apostador
from datetime import date

class Prisionero(Apostador):
    _delitos = {}
    _antidelitos = {}
    _prisioneros = {}
    prisionerosMASCULINOS = []
    prisionerosFEMENINOS = []


    def __init__(self, identificacion, nombre, saldo, _genero, _celda, _delitos):
        Apostador.__init__(self, identificacion, nombre, saldo)
        self._genero = _genero
        self._inicioCondena = date.today()
        self._celda = _celda
        self._delitos = _delitos

        if self._genero=="MASCULINO":
            Prisionero.prisionerosMASCULINOS.append(self.identificacion)

        elif self._genero=="FEMENINO":
            Prisionero.prisionerosFEMENINOS.append(self.identificacion) 

    def getGenero(self):
        return self._genero
    def setGenero(self, _genero):
        self._genero = _genero

    def getCelda(self):
        return self._celda
    def setCelda(self, _celda):
        self._celda = _celda

    def getInicioCondena(self):
        return self._inicioCondena
    def setInicioCondena(self, _inicioCondena):
        self._inicioCondena = _inicioCondena 

    def getFinCondena(self):
        return self._finCondena
    def setFinCondena(self, _finCondena):
        self._finCondena = _finCondena      

    def getDelitos(self):
        return self._delitos
    def setDelitos(self, _delitos):
        self._delitos = _delitos    

    def getAntidelitos(self):
        return self.antidelitos
    def setAntiDelitos(self, antidelitos):
        self.antidelitos = antidelitos  

    def getPrisioneros(self):
        return self._prisioneros
    def setPrisioneros(self, _prisioneros):
        self._prisioneros = _prisioneros          