from gestorAplicacion.apostador import Apostador
from gestorAplicacion.celda import Celda
from gestorAplicacion.prisionero import Prisionero

class Guardian(Apostador):
    _guardianes = {}

    def __init__(self, nombre: str, saldo: float, salario: float, celdas = None):
        super().__init__(nombre, saldo)
        self.identificacion = list(Guardian._guardianes.keys())[len(Guardian._guardianes)-1]+1
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
        trasladosString = []

        for i in self._traslados:
            mensaje = "Se trasladó al prisionero: " + str(i[1].getIdentificacion()) + "\n" + "Desde la celda: " + str(i[0].getNumero()) + "\n" + "A la celda: " + str(i[2].getNumero())
            trasladosString.append(mensaje)

        return trasladosString

    def __str__(self) -> str: #Decidir implementacion
        celdas = ""
        for key in self._celdas:
            celdas += str(key) + " "

        return ("GUARDIAN: " + str(self.identificacion) + "\n"
        + "Nombre: " + self.nombre + "\n"
        + "Saldo: " + str(round(self.saldo,2)) + "\n"
        + "Salario: " + str(round(self._salario,2)) + "\n"
        + "Celdas a Cargo: " + celdas)

    def infoApostador(self): #Decidir implementacion
        pass

    def getCeldas(self):
        return self._celdas
    def setCeldas(self, celdas):
        self._celdas = celdas

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