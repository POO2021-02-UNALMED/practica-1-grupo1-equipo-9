import pickle
import os
from gestorAplicacion.antidelito import Antidelito
from gestorAplicacion.apuesta import Apuesta
from gestorAplicacion.celda import Celda
from gestorAplicacion.delito import Delito
from gestorAplicacion.guardian import Guardian
from gestorAplicacion.pelea import Pelea
from gestorAplicacion.prisionero import Prisionero

def serializar():
    datos = {"antidelitos": Antidelito.getAntidelitos(),
            "apuestas": Apuesta.getApuestas(),
            "celdas": Celda.getCeldas(),
            "celdasFEMENINAS": Celda.getCeldasFEMENINAS(),
            "celdasMASCULINAS": Celda.getCeldasMASCULINAS(),
            "delitos": Delito.getDelitos(),
            "guardianes": Guardian.getGuardianes(),
            "peleas": Pelea.getPeleas(),
            "prisioneros": Prisionero.getPrisioneros(),
            "prisionerosFEMENINO": Prisionero.getPrisionerosFEMENINOS(),
            "prisionerosMASCULINO": Prisionero.getPrisionerosMASCULINOS()}

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    direccAux = os.path.join(BASE_DIR, "baseDatos")

    for k, v in datos.items():
        picklefile = open( os.path.join(direccAux, k) , 'wb')
        pickle.dump(v, picklefile)
        picklefile.close()



