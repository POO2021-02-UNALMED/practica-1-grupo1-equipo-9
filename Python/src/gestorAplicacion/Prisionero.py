from apostador import Apostador;

class Prisionero(Apostador):
    prisionerosMASCULINOS = []
    prisionerosFEMENINOS = []


    def __init__(self, identificacion, nombre, saldo, genero, celda, delitos):
        Apostador.__init__(self, identificacion, nombre, saldo)
        self.genero = genero
        self.celda = celda
        self.delitos = delitos

        if self.genero=="MASCULINO":
            Prisionero.prisionerosMASCULINOS.append(self.identificacion)

        elif self.genero=="FEMENINO":
            Prisionero.prisionerosFEMENINOS.append(self.identificacion) 

    def getGenero(self):
        return self.genero
    def setGenero(self, genero):
        self.genero = genero

    def getCelda(self):
        return self.celda
    def setCelda(self, celda):
        self.celda = celda

    '''def getInicioCondena(self):
        return self.inicioCondena
    def setInicioCondena(self, inicioCondena):
        self.inicioCondena = inicioCondena 

    def getFinCondena(self):
        return self.FinCondena
    def setFinCondena(self, finCondena):
        self.finCondena = finCondena  '''      

    def getDelitos(self):
        return self.delitos
    def setDelitos(self, delitos):
        self.delitos = delitos    

    def getAntidelitos(self):
        return self.antidelitos
    def setAntiDelitos(self, antidelitos):
        self.antidelitos = antidelitos  

    def getPrisioneros(self):
        return self.prisioneros
    def setPrisioneros(self, prisioneros):
        self.prisioneros = prisioneros          