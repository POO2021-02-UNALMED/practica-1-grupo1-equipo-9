class Delito:
    _delitos = {}

    def __init__(self, _nombre, _descripcion, _nivel, _tiempoCondena):
        self._codigo = list(Delito._delitos.keys())[len(Delito._delitos)-1]+1
        self._nombre = _nombre
        self._descripcion = _descripcion 
        self._nivel = _nivel
        self._tiempoCondena = _tiempoCondena

        Delito._delitos[self._codigo] = self

    def getCodigo(self):
        return self._codigo
    def setCodigo(self, _codigo):
        self._codigo = _codigo

    def getNombre(self):
        return self._nombre
    def setNombre(self, _nombre):
        self._nombre = _nombre   

    def getDescripcion(self):
        return self._descripcion
    def setDescripcion(self, _descripcion):
        self._descripcion = _descripcion

    def getNivel(self):
        return self._nivel
    def setNivel(self, _nivel):
        self._nivel = _nivel      

    def getTiempoCondena(self):
        return self._tiempoCondena
    def setTiempoCondena(self, _tiempoCondena):
        self._tiempoCondena = _tiempoCondena

    @classmethod
    def getDelitos(cls):
        return cls._delitos
    @classmethod
    def setDelitos(cls, _delitos):
        cls._delitos = _delitos       

    def __str__(self) -> str:
        return ("Delito: "+ str(self.getCodigo()) + "\n" + "Nombre: " + self.getNombre()+ "\n"
                +"Descripción: " + self.getDescripcion() +"\n"
                +"Nivel: " + str(self.getNivel()) + "\n"
                + "Tiempo condena: " + str(self.getTiempoCondena()) + "\n")    