from gestorAplicacion.prisionero import Prisionero

class Celda:
    _celdas = {}
    _celdasMASCULINAS = []
    _celdasFEMENINAS = []

    def __init__(self, numero: int, genero, largo: float, ancho: float, capMax: int):
        self._numero = numero
        self._genero = genero
        self._LARGO = largo
        self._ANCHO = ancho
        self._CAPMAX = capMax
        self._prisioneros = {}

        Celda._celdas[self._numero] = self

        if self._genero.value == "MASCULINO":
            Celda._celdasMASCULINAS.append(self._numero)
        elif self._genero.value == "FEMENINO":
            Celda._celdasFEMENINAS.append(self._numero)

    def extraerPrisionero(self, prisionero: Prisionero):
        prisionero.setCelda(None)
        self._prisioneros.pop(prisionero.getIdentificacion())

    def ingresarPrisionero(self, prisionero: Prisionero):
        prisionero.setCelda(self)
        self._prisioneros[prisionero.getIdentificacion()] = prisionero

    def __str__(self) -> str: #Decidir implementacion
        prisioneros = ""
        for key in self._prisioneros:
            prisioneros += str(key) + " "

        return ("CELDA: " + str(self._numero) + "\n"
        + "Género: " +  self._genero.value + "\n"
        + "Largo: " + str(self._LARGO) + "\n"
        + "Ancho: " + str(self._ANCHO) + "\n"
        + "Capacidad Máxima: " + str(self._CAPMAX) + "\n"
        + "Prisioneros en la Celda: " + prisioneros)

    def infoTraslados(self): #Decidir implementacion
        pass

    def getPrisioneros(self):
        return self._prisioneros

    def getNumero(self):
        return self._numero
    def setNumero(self, numero: int):
        self._numero = numero

    def getGenero(self):
        return self._genero    

    def getLargo(self):
        return self._LARGO
    def getAncho(self):
        return self._ANCHO
    def getCapMax(self):
        return self._CAPMAX

    @classmethod
    def getCeldas(cls):
        return cls._celdas

    @classmethod
    def setCeldas(cls, celdas):
        cls._celdas = celdas
    
    @classmethod
    def getCeldasMASCULINAS(cls):
        return cls._celdasMASCULINAS
    @classmethod
    def setCeldasMASCULINAS(cls, celdasMASCULINAS):
        cls._celdasMASCULINAS = celdasMASCULINAS

    @classmethod
    def getCeldasFEMENINAS(cls):
        return cls._celdasFEMENINAS
    @classmethod
    def setCeldasMASCULINAS(cls, celdasFEMENINAS):
        cls._celdasFEMENINAS = celdasFEMENINAS