from gestorAplicacion.apostador import Apostador
from datetime import date
from dateutil.relativedelta import relativedelta

class Prisionero(Apostador):
    _prisioneros = {}
    _prisionerosMASCULINOS = []
    _prisionerosFEMENINOS = []

    def __init__(self, nombre, saldo, _genero, _celda, _delitos: dict):
        from gestorAplicacion.celda import Celda
        super().__init__(nombre, saldo)
        self.identificacion = len(Prisionero._prisioneros) + 1
        self._antidelitos = {}
        self._genero = _genero
        self._inicioCondena = date.today()
        self._celda = _celda 
        Celda.getCeldas()[_celda].ingresarPrisionero(self)
        self._delitos = _delitos

        if self._genero.value == "MASCULINO":
            Prisionero._prisionerosMASCULINOS.append(self.identificacion)

        elif self._genero.value == "FEMENINO":
            Prisionero._prisionerosFEMENINOS.append(self.identificacion) 
        
        meses = 0
        for i in _delitos.keys():
            meses += _delitos[i].getTiempoCondena()

        self._finCondena = self._inicioCondena
        self.incrementarCondena(meses)

        Prisionero._prisioneros[self.identificacion] = self

    def agregarDelito(self, delito):
        self._delitos[delito.getCodigo()] = delito
        self.incrementarCondena(delito.getTiempoCondena())

    def agregarAntidelito(self, antidelito):
        self._antidelitos[antidelito.getCodigo()] = antidelito
        self.disminuirCondena(antidelito.getRebajaCondena())

    def incrementarCondena(self,meses):
        self._finCondena = self._finCondena + relativedelta(months=+meses)

    def disminuirCondena(self,meses):  
        self._finCondena = self._finCondena - relativedelta(months=+meses)      

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
    @classmethod
    def setPrisioneros(cls, _prisioneros):
        cls._prisioneros = _prisioneros

    @classmethod
    def getPrisionerosMASCULINOS(cls):
        return cls._prisionerosMASCULINOS
    @classmethod
    def setPrisionerosMASCULINOS(cls, _prisioneros):
        cls._prisionerosMASCULINOS = _prisioneros

    @classmethod
    def getPrisionerosFEMENINOS(cls):
        return cls._prisionerosFEMENINOS
    @classmethod
    def setPrisionerosFEMENINOS(cls, _prisioneros):
        cls._prisionerosFEMENINOS = _prisioneros

    def __str__(self) -> str:
        return ("Prisionero: "+ str(self.identificacion) + "\n" + "Genero: " + self._genero.value + "\n"
                +"Inicio condena: " + str(self.getInicioCondena()) +"\n"
                + "Fin condena: " + str(self.getFinCondena()) + "\n")
    
