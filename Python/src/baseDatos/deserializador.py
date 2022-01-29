import pickle
import os
import settings
from gestorAplicacion.antidelito import Antidelito
from gestorAplicacion.apuesta import Apuesta
from gestorAplicacion.celda import Celda
from gestorAplicacion.delito import Delito
from gestorAplicacion.guardian import Guardian
from gestorAplicacion.pelea import Pelea
from gestorAplicacion.prisionero import Prisionero

def deserializar():
    datos = {"antidelitos": lambda x: Antidelito.setAntidelitos(x),
            "apuestas": lambda x: Apuesta.setApuestas(x),
            "celdas": lambda x: Celda.setCeldas(x),
            "celdasFEMENINAS": lambda x: Celda.setCeldasFEMENINAS(x),
            "celdasMASCULINAS": lambda x: Celda.setCeldasMASCULINAS(x),
            "delitos": lambda x: Delito.setDelitos(x),
            "guardianes": lambda x: Guardian.setGuardianes(x),
            "peleas": lambda x: Pelea.setPeleas(x),
            "prisioneros": lambda x: Prisionero.setPrisioneros(x),
            "prisionerosFEMENINO": lambda x: Prisionero.setPrisionerosFEMENINOS(x),
            "prisionerosMASCULINO": lambda x: Prisionero.setPrisionerosMASCULINOS(x)}

    direccAux = os.path.join(settings.BASE_DIR, "src", "baseDatos")

    for k, v in datos.items():
        picklefile = open( os.path.join(direccAux, k) , 'rb')
        pc = pickle.load(picklefile)
        v(pc)
        picklefile.close()
        print(pc)

        