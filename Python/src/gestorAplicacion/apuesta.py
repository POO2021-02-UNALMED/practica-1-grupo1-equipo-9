from pelea import Pelea
from prisionero import Prisionero
from apostador import Apostador

class Apuesta:
    _apuestas = {}

    def __init__(self, codigo: int, pelea: Pelea):
        self._codigo = codigo
        self._pelea = pelea
        Apuesta._apuestas[codigo] = self

    def resultadoApuesta(self):
        if self._pelea.getGanador() is None :
            return "La pelea con codigo " + str(self.getCodigo()) + " aun no tiene ganador"

    def resolverApuesta(self):
        pass

    def agregarApostador(self, apostador: Apostador, prisionero: Prisionero, apuesta: int):
        pass
