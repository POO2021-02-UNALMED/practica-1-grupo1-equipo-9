from gestorAplicacion.antidelito import Antidelito
from gestorAplicacion.celda import Celda
from gestorAplicacion.delito import Delito
from gestorAplicacion.genero import genero
from gestorAplicacion.pelea import Pelea
from gestorAplicacion.prisionero import Prisionero
from gestorAplicacion.guardian import Guardian


delito1 = Delito(1, "Robo", "Apropiarse de un bien ajeno de manera fraudulenta, empleando la fuera, violencia o intimidacion ", 2, 10)
delito2 = Delito(2, "Pelea callejera", "Enfrentarse fisicamente con otra persona o animal en lugares publicos", 1, 12)
delito3 = Delito(3, "3", "3", 6, 48)
delito4 = Delito(4, "4", "4", 8, 200)
delito5 = Delito(5, "5", "5", 9, 360)
delito6 = Delito(6, "6", "6", 3, 24)
delito7 = Delito(7, "Batalla", "Participar en la batalla del Departamento de Misterios como mortifago", 5, 360)
delito8 = Delito(8, "Batalla", "Participar en la batalla del Departamento de Misterios", 5, 50)
delito9 = Delito(9, "9", "9", 7, 500)
delito10 = Delito(10, "10", "10", 4, 10)
		
delitos1 = {}
delitos1[delito1.getCodigo()] =  delito1
delitos1[delito5.getCodigo()] = delito5
delitos1[delito9.getCodigo()] = delito9
		
delitos2 = {}
delitos2[delito9.getCodigo()] = delito9
		
delitos3 = {}
delitos3[delito7.getCodigo()] = delito7
delitos3[delito3.getCodigo()] = delito3
	
delitos4 = {}
delitos4[delito10.getCodigo()] = delito10
		
delitos5 = {}
delitos5[delito2.getCodigo()] = delito2
delitos5[delito4.getCodigo()] = delito4
delitos5[delito6.getCodigo()] = delito6
delitos5[delito8.getCodigo()] = delito8
		
#		crearCeldas
celda0 = Celda(0, genero.M, 1.5, 4, 2)
celda1 = Celda(1, genero.M, 1.5, 4, 3)
celda2 = Celda(2, genero.M, 1.5, 4, 4)
celda3 = Celda(3, genero.M, 1.5, 4, 2)
celda4 = Celda(4, genero.M, 1.5, 4, 3)
celda5 = Celda(5, genero.F, 1.5, 4, 4)
celda6 = Celda(6, genero.F, 1.5, 4, 5)
celda7 = Celda(7, genero.F, 1.5, 4, 6)
celda8 = Celda(8, genero.F, 1.5, 4, 2)
celda9 = Celda(9, genero.F, 1.5, 4, 3)
		
#		crearPrisioneros 
delitos00 = {}; delitos00[delito1.getCodigo()] = delito1
delitos11 = {}; delitos11[delito1.getCodigo()] = delito1; delitos11[delito2.getCodigo()] = delito2
delitos22 = {}; delitos22[delito1.getCodigo()] = delito1; delitos22[delito3.getCodigo()] = delito3; delitos22[delito4.getCodigo()] = delito4
delitos33 = {}; delitos33[delito4.getCodigo()] = delito4; delitos33[delito2.getCodigo()] = delito2; delitos33[delito5.getCodigo()] = delito5; delitos3[delito9.getCodigo()] = delito9
delitos44 = {}; delitos44[delito6.getCodigo()] = delito6; delitos44[delito2.getCodigo()] = delito2; delitos44[delito10.getCodigo()] = delito10
delitos55 = {}; delitos55[delito6.getCodigo()] = delito6; delitos55[delito5.getCodigo()] = delito5
delitos66 = {}; delitos66[delito7.getCodigo()] = delito7; delitos66[delito8.getCodigo()] = delito8; delitos66[delito9.getCodigo()] = delito9
delitos77 = {}; delitos77[delito8.getCodigo()] = delito8; delitos77[delito5.getCodigo()] = delito5; delitos77[delito10.getCodigo()] = delito10
		
#################################################################################################3

prisionero0 = Prisionero(0, "nombre0", 100, genero.M, celda0, delitos00)
prisionero1 = Prisionero(1, "nombre1", 200, genero.M, celda0, delitos11)
prisionero2 = Prisionero(2, "nombre2", 300, genero.M, celda1, delitos22)
prisionero3 = Prisionero(3, "nombre3", 100, genero.M, celda1, delitos33)
prisionero4 = Prisionero(4, "nombre4", 200, genero.F, celda5, delitos44)
prisionero5 = Prisionero(5, "nombre5", 300, genero.F, celda6, delitos55)
prisionero6 = Prisionero(6, "nombre6", 400, genero.F, celda7, delitos66)
prisionero7 = Prisionero(7, "nombre7", 500, genero.F, celda5, delitos77)
prisionero8 = Prisionero(8, "nombre8", 400, genero.M, celda4, delitos00)
prisionero9 = Prisionero(9, "nombre9", 700, genero.M, celda4, delitos55)
prisionero10 = Prisionero(10, "nombre10", 1000, genero.M, celda3, delitos33)
prisionero11 = Prisionero(11, "nombre11", 1200, genero.F, celda9, delitos77)
prisionero12 = Prisionero(12, "nombre12", 200, genero.F, celda8, delitos66)
prisionero13 = Prisionero(13, "nombre13", 120, genero.M, celda2, delitos66)
prisionero14 = Prisionero(14, "nombre14", 50, genero.F, celda6, delitos77)
prisionero15 = Prisionero(15, "nombre15", 0, genero.F, celda7, delitos44)
		
		
#		crearGuardianes
celdas1 = {}
celdas1[celda0.getNumero()] = celda0
celdas1[celda9.getNumero()] = celda9
celdas1[celda5.getNumero()] = celda5
		
celdas2 = {}
celdas2[celda1.getNumero()] = celda1
celdas2[celda8.getNumero()] = celda8
celdas2[celda4.getNumero()] = celda4
		
celdas3 = {}
celdas3[celda3.getNumero()] = celda3
celdas3[celda7.getNumero()] = celda7
celdas3[celda2.getNumero()] = celda2
		
celdas4 = {}
celdas4[celda2.getNumero()] = celda2
celdas4[celda6.getNumero()] = celda6
celdas4[celda9.getNumero()] = celda9
		
celdas5 = {}
celdas5[celda5.getNumero()] = celda5
celdas5[celda8.getNumero()] = celda8
celdas5[celda7.getNumero()] = celda7
		
guardian1 = Guardian("Chuck Norris",4500,5430,celdas1)
guardian2 = Guardian("Jhon Wick",10000,6360,celdas2)
guardian3 = Guardian("Arnold Schwarzenegger",2035,5700,celdas3)
guardian4 = Guardian("Sylvester Stallone",8600,6100,celdas4)
guardian5 = Guardian("Jean_Claude Van Damme",6700,7480,celdas5)
		
#		crearAntidelitos
antidelito0 = Antidelito(0, "nombre0", "descripcion0",1)
antidelito1 = Antidelito(1, "nombre1", "descripcion1",2)
antidelito2 = Antidelito(2, "nombre2", "descripcion2",3)
antidelito3 = Antidelito(3, "nombre3", "descripcion3",4)
antidelito4 = Antidelito(4, "nombre4", "descripcion4",5)
antidelito5 = Antidelito(5, "nombre5", "descripcion5",6)
antidelito6 = Antidelito(6, "nombre6", "descripcion6",7)
		
#		crearPeleas
pelea0 = Pelea(0, genero.M, prisionero0, prisionero1, "arma10", "arma20")
pelea1 = Pelea(1, genero.M, prisionero2, prisionero3, "arma11", "arma21")
pelea2 = Pelea(2, genero.F, prisionero4, prisionero5, "arma12", "arma22")
pelea3 = Pelea(3, genero.F, prisionero6, prisionero7, "arma13", "arma23")


from baseDatos.serializador import serializar
from baseDatos.deserializador import deserializar

serializar()
deserializar()