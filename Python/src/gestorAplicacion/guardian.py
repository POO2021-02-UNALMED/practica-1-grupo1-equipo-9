from gestorAplicacion.apostador import Apostador
from gestorAplicacion.celda import Celda
from gestorAplicacion.prisionero import Prisionero

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
        + "Saldo: " + str(self.saldo) + "\n"
        + "Salario: " + str(self._salario) + "\n"
        + "Celdas a Cargo: " + celdas)

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