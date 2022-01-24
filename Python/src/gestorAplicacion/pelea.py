from prisionero import Prisionero
from apuesta import Apuesta
from random import randint

class Pelea:
    _peleas = {}

    def __init__(self, codigo:int, genero, luchador1: Prisionero, luchador2: Prisionero,
                armaLuchador1: str, armaLuchador2: str) -> None:
        self._ganador = None
        self._codigo = codigo
        self._genero = genero
        self._luchador1 = luchador1
        self._luchador2 = luchador2
        self._armaLuchador1 = armaLuchador1
        self._armaLuchador2 = armaLuchador2

        self._apuesta = Apuesta(codigo, self)

        Pelea._peleas[codigo] = self

    def setGanador(self, prisionero: Prisionero):
        self._ganador = prisionero
        self._apuesta.resolverApuesta()

    def getGanador(self): return self._ganador

    def getLuchadores(self):
        return (self._luchador1, self._luchador2)

    @classmethod
    def battleRoyale(clc, celdas: list):
        luchadores = []
        combates = []

        for c in celdas:
            for k in c.getPrisioneros().keys(): luchadores.append(k)

        if len(luchadores) < 3:
            combates.append("No hay suficientes luchadores")
            return combates

        while len(luchadores) > 1:
            rN1 = randint(0, len(luchadores)-1)
            l1 = luchadores.pop(rN1)

            rN2 = randint(0, len(luchadores)-1)
            l2 = luchadores.pop(rN2)

            g = randint(0,1)

            if g:
                luchadores.append(l2)
                combates.append("El prisionero "+ str(l2) +" ha derrotado al prisionero "+ str(l1))
            else:
                luchadores.append(l1)
                combates.append("El prisionero "+ str(l1) +" ha derrotado al prisionero "+ str(l2))

        ganador: Prisionero = Prisionero.getPrisioneros()[luchadores[0]]
        ganador.aumentarSaldo(1000)
        combates.append("El prisionero "+ luchadores[0] + " es el ganador y recibio 1000 dolares")

        return combates


    def getCodigo(self): return self._codigo
    def setCodigo(self, codigo: int): self._codigo = codigo
    
    def getGenero(self): return self._genero
    def setGenero(self, genero): self._genero = genero

    def getArmaLuchador1(self): return self._armaLuchador1
    def setArmaLuchador1(self, armaLuchador1: str): self._armaLuchador1 = armaLuchador1

    def getArmaLuchador2(self): return self._armaLuchador2
    def setArmaLuchador2(self, armaLuchador2: str): self._armaLuchador2 = armaLuchador2
	
    def getApuesta(self): return self._apuesta
    def setApuesta(self, apuesta: Apuesta): self._apuesta = apuesta
	
    @classmethod
    def getPeleas(clc): return clc._peleas
    @classmethod
    def setPeleas(clc, peleas: dict): clc._peleas = peleas

    def __str__(self) -> str:
        return ("PELEA: " + self._codigo + "\n" + "Genero: " + self._genero.value + "\n" 
                + "Luchador 1: " + self._luchador1.getNombre() +"\n"
                + "Luchador 2: " + self._luchador2.getNombre() + "\n" 
                + "Arma luchador 1: " + self._armaLuchador1 + "\n" 
                + "Arma luchador 2: " + self._armaLuchador2 + "\n" 
                + "Ganador: " + ("Aun no hay ganador" if self._ganador is None else self._ganador.getNombre()) + "\n")