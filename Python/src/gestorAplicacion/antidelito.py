class Antidelito:
    _antidelitos = {}

    def __init__(self, codigo: int, nombre: str, descripcion: str, rebajaCondena: int):
        self._codigo = codigo
        self._nombre = nombre
        self._descripcion = descripcion
        self._rebajaCondena = rebajaCondena
        Antidelito._antidelitos[self._codigo] = self

    def getCodigo(self):
        return self._codigo
    def setCodigo(self, codigo: int):
        self._codigo = codigo

    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getDescripcion(self):
        return self._descripcion
    def setDescripcion(self, descripcion: str):
        self._descripcion = descripcion

    def getRebajaCondena(self):
        return self._rebajaCondena
    def setRebajaCondena(self, rebajaCondena: int):
        self._rebajaCondena = rebajaCondena

    @classmethod
    def getAntidelitos(cls):
        return cls._antidelitos
    @classmethod
    def setAntidelitos(cls, antidelitos):
        cls._antidelitos = antidelitos

    def __str__(self) -> str: #Decidir implementacion
        pass