from apostador import Apostador
from datetime import datetime, timedelta, date

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
        _celda.ingresarPrisionero(self)
        self._delitos = _delitos

        if self._genero=="MASCULINO":
            Prisionero.prisionerosMASCULINOS.append(self.identificacion)

        elif self._genero=="FEMENINO":
            Prisionero.prisionerosFEMENINOS.append(self.identificacion) 
        
        meses = 0
        for i in _delitos:
            meses += _delitos[i].getTiempoCondena()

        self._finCondena = self._inicioCondena
        self.incrementarCondena(meses)

        Prisionero._prisioneros[self.identificacion] = self

    def agregarDelito(self, delito):
        Prisionero._delitos[delito.getCodigo()] = delito
        self.incrementarCondena(delito.getTiempoCondena())

    def agregarAntidelito(self, antidelito):
        Prisionero._antidelitos[antidelito.getCodigo()] = antidelito
        self.disminuirCondena(antidelito.getRebajaCondena())

    def incrementarCondena(self,meses):
        self._finCondena = self._finCondena + timedelta(weeks=meses*4)

    def disminuirCondena(self,meses):  
        self._finCondena = self._finCondena - 4*timedelta(weeks=meses*4)      

    '''#override
    def __str__(self):'''

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

    def getAntidelitos(self):
        return self._antidelitos 

    @classmethod
    def getPrisioneros(cls):
        return cls._prisioneros
    def setPrisioneros(cls, _prisioneros):
        cls._prisioneros = _prisioneros

    def __str__(self) -> str:
        return ("PRISIONERO: " + self._codigo + "\n" + "Genero: " + self._genero.value + "\n" 
                + "Inicio condena: " + self._inicioCondena + "\n" 
                + "Fin condena " + self._finCondena + "\n" )
