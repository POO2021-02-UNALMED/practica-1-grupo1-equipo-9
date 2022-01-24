from apostador import Apostador
from datetime import date, timedelta

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
        self._celda = _celda # _celda.ingresarPrisionero(self)
        self._delitos = _delitos

        if self._genero=="MASCULINO":
            Prisionero.prisionerosMASCULINOS.append(self.identificacion)

        elif self._genero=="FEMENINO":
            Prisionero.prisionerosFEMENINOS.append(self.identificacion) 
        
        '''meses=0
        for(Integer k: delitos.keySet())
            meses+=delitos.get(k).getTiempoCondena();   
        this.finCondena = this.inicioCondena;
        incrementarCondena(meses)

        prisioneros.put(this.identificacion, this)
'''
        self._finCondena = self._inicioCondena
        incrementarCondena(meses)

        _prisioneros[self.identificacion] = self

    def agregarDelito(self, delito):
        _delitos[delito.getCodigo()] = delito
        incrementarCondena(delito.getTiempoCondena())

    def agregarAntidelito(self, antidelito):
        _antidelitos[antidelito.getCodigo()] = antidelito
        disminuirCondena(antidelito.getTiempoCondena())

    def incrementarCondena(meses):
        self._finCondena = self._finCondena + timedelta(months=meses)

    def disminuirCondena(meses):  
        self._finCondena = self._finCondena - timedelta(months=meses)      

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

    def getPrisioneros(self):
        return self._prisioneros
    def setPrisioneros(self, _prisioneros):
        self._prisioneros = _prisioneros          
