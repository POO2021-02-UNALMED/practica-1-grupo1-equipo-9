from gestorAplicacion.prisionero import Prisionero
from gestorAplicacion.apostador import Apostador

class Apuesta:
    _apuestas = {}

    def __init__(self, codigo: int, pelea):
        self._codigo = codigo
        self._pelea = pelea
        self._apostadores = []
        self._estadisticas = []
        self._montoTotal = 0
        self._montoTotalGanadores = 0
        Apuesta._apuestas[codigo] = self

    def resultadoApuesta(self):
        if self._pelea.getGanador() is None :
            return "La pelea con codigo " + str(self.getCodigo()) + " aun no tiene ganador"
        if not self.getApostadores(): 
            return "La pelea con codigo " + str(self.getCodigo()) + " no tuvo apuestas"

        resultadoMonto1 = "Pelea: " + str(self.getCodigo()) + "\nEl monto total recogido en la apuesta fue: " + str(self._montoTotal) + "\n"
        resultadoMonto2 = "El dinero total apostado por los ganadores de esta apuesta fue: " + str(self._montoTotalGanadores) + "\n\n"

        resulta3 = "Las estadisticas de esta apuesta son las siguientes: \n"
        resulta4 = ""

        for string in self._estadisticas:
            resulta4 += string + "\n"

        return resultadoMonto1 + resultadoMonto2 + resulta3 + resulta4

    def _resolverApuesta(self):
        if not self.getApostadores(): return

        montoTotal = 0
        totalGanadores = 0

        for tupla in self.getApostadores():
            prisionero: Prisionero = tupla[1]
            apuesta = tupla[2]
            montoTotal += apuesta
            if self._pelea.getGanador() is prisionero: totalGanadores += apuesta

        for tupla in self.getApostadores():
            apostador: Apostador= tupla[0]
            prisionero: Prisionero = tupla[1]
            apuesta = tupla[2]

            if self._pelea.getGanador() is prisionero:
                k = apuesta/totalGanadores
                ganancia = k*montoTotal
                apostador.aumentarSaldo(ganancia)

                self._estadisticas.append(
                    "Apostador con ID: " + str(apostador.getIdentificacion()) + "\t"*3 + "+" 
                    + str(round(ganancia - apuesta, 2)) + "\t"*3 + "Saldo actual: " + str(round(apostador.getSaldo(),2))
                    )
            else:
                self._estadisticas.append(
                    "Apostador con ID: " + str(apostador.getIdentificacion()) + "\t"*3 + "-" 
                    + str(apuesta) + "\t"*3 + "Saldo actual: " + str(round(apostador.getSaldo(),2))
                    )

        self._montoTotal = montoTotal
        self._montoTotalGanadores = totalGanadores
        


    def agregarApostador(self, apostador: Apostador, prisionero: Prisionero, apuesta: int):
        apostador.reducirSaldo(apuesta)
        agregando = (apostador, prisionero, apuesta)
        self._apostadores.append(agregando)

    
    def getCodigo(self): return self._codigo
    def setCodigo(self, codigo: int): self._codigo = codigo
    
    def getPelea(self): return self._pelea
    def setPelea(self, pelea): self._pelea = pelea

    def getApostadores(self): return self._apostadores
    
    @classmethod
    def getApuestas(clc): return clc._apuestas
    @classmethod
    def setApuestas(clc, apuestas: dict): clc._apuestas = apuestas