from apostador import Apostador
from celda import Celda
from prisionero import Prisionero

class Guardian(Apostador):
    _guardianes = {}

    def __init__(self, identificacion: int, nombre: str, saldo: int, salario:int, celdas = None):
        super().__init__(identificacion, nombre, saldo)
        self._salario = salario
        self._celdas = celdas
        self._traslados = []
        Guardian._guardianes[self.identificacion] = self

    def trasladarPrisionero(self, prisionero: Prisionero, celda: Celda):
        celdaOrigen = prisionero.getCelda()
        celdaOrigen.extraerPrisionero(prisionero)
        celda.ingresarPrisionero(prisionero)

        traslado = (celdaOrigen, prisionero, celda)
        self.agregarTraslados(traslado)
        
    def agregarTraslados(self, objetos):
        self._traslados.append(objetos)

    def listaTraslados(self): #Decidir implementacion
        pass

    def __str__(self) -> str: #Decidir implementacion
        pass

    def infoApostador(self): #Decidir implementacion
        pass

    def getCeldas(self):
        return self._celdas
    def agregarCelda(self, celda: Celda):
        self._celdas[celda.getNumero()] = celda

    def getSalario(self):
        return self._salario
    def setSalario(self, salario):
        self._salario = salario

    @classmethod
    def getGuardianes(cls):
        return cls._guardianes
    @classmethod
    def setGuardianes(cls, guardianes):
        cls._guardianes = guardianes