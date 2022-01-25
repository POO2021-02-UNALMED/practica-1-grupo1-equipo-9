from gestorAplicacion.antidelito import Antidelito
from gestorAplicacion.apostador import Apostador
from gestorAplicacion.apuesta import Apuesta
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


		Prisionero prisionero0 = new Prisionero(0, "nombre0", 100, genero.MASCULINO, celda0, delitos00);
		Prisionero prisionero1 = new Prisionero(1, "nombre1", 200, genero.MASCULINO, celda0, delitos11);
		Prisionero prisionero2 = new Prisionero(2, "nombre2", 300, genero.MASCULINO, celda1, delitos22);
		Prisionero prisionero3 = new Prisionero(3, "nombre3", 100, genero.MASCULINO, celda1, delitos33);
		Prisionero prisionero4 = new Prisionero(4, "nombre4", 200, genero.FEMENINO, celda5, delitos44);
		Prisionero prisionero5 = new Prisionero(5, "nombre5", 300, genero.FEMENINO, celda6, delitos55);
		Prisionero prisionero6 = new Prisionero(6, "nombre6", 400, genero.FEMENINO, celda7, delitos66);
		Prisionero prisionero7 = new Prisionero(7, "nombre7", 500, genero.FEMENINO, celda5, delitos77);
		Prisionero prisionero8 = new Prisionero(8, "nombre8", 400, genero.MASCULINO, celda4, delitos00);
		Prisionero prisionero9 = new Prisionero(9, "nombre9", 700, genero.MASCULINO, celda4, delitos55);
		Prisionero prisionero10 = new Prisionero(10, "nombre10", 1000, genero.MASCULINO, celda3, delitos33);
		Prisionero prisionero11 = new Prisionero(11, "nombre11", 1200, genero.FEMENINO, celda9, delitos77);
		Prisionero prisionero12 = new Prisionero(12, "nombre12", 200, genero.FEMENINO, celda8, delitos66);
		Prisionero prisionero13 = new Prisionero(13, "nombre13", 120, genero.MASCULINO, celda2, delitos66);
		Prisionero prisionero14 = new Prisionero(14, "nombre14", 50, genero.FEMENINO, celda6, delitos77);
		Prisionero prisionero15 = new Prisionero(15, "nombre15", 0, genero.FEMENINO, celda7, delitos44);
		
		
//		crearGuardianes
		Hashtable<Integer, Celda> celdas1 = new Hashtable<>();
		celdas1[celda0.getNumero(), celda0);
		celdas1[celda9.getNumero(), celda9);
		celdas1[celda5.getNumero(), celda5);
		
		Hashtable<Integer, Celda> celdas2 = new Hashtable<>();
		celdas2[celda1.getNumero(), celda1);
		celdas2[celda8.getNumero(), celda8);
		celdas2[celda4.getNumero(), celda4);
		
		Hashtable<Integer, Celda> celdas3 = new Hashtable<>();
		celdas3[celda3.getNumero(), celda3);
		celdas3[celda7.getNumero(), celda7);
		celdas3[celda2.getNumero(), celda2);
		
		Hashtable<Integer, Celda> celdas4 = new Hashtable<>();
		celdas4[celda2.getNumero(), celda2);
		celdas4[celda6.getNumero(), celda6);
		celdas4[celda9.getNumero(), celda9);
		
		Hashtable<Integer, Celda> celdas5 = new Hashtable<>();
		celdas5[celda5.getNumero(), celda5);
		celdas5[celda8.getNumero(), celda8);
		celdas5[celda7.getNumero(), celda7);
		
		Guardian guardian1 = new Guardian(1001,"Chuck Norris",4500,5430,celdas1);
		Guardian guardian2 = new Guardian(1002,"Jhon Wick",10000,6360,celdas2);
		Guardian guardian3 = new Guardian(1003,"Arnold Schwarzenegger",2035,5700,celdas3);
		Guardian guardian4 = new Guardian(1004,"Sylvester Stallone",8600,6100,celdas4);
		Guardian guardian5 = new Guardian(1005,"Jean_Claude Van Damme",6700,7480,celdas5);
		
//		crearAntidelitos
		Antidelito antidelito0 = new Antidelito(0, "nombre0", "descripcion0",1);
		Antidelito antidelito1 = new Antidelito(1, "nombre1", "descripcion1",2);
		Antidelito antidelito2 = new Antidelito(2, "nombre2", "descripcion2",3);
		Antidelito antidelito3 = new Antidelito(3, "nombre3", "descripcion3",4);
		Antidelito antidelito4 = new Antidelito(4, "nombre4", "descripcion4",5);
		Antidelito antidelito5 = new Antidelito(5, "nombre5", "descripcion5",6);
		Antidelito antidelito6 = new Antidelito(6, "nombre6", "descripcion6",7);
		
//		crearPeleas
		Pelea pelea0 = new Pelea(0, genero.MASCULINO, prisionero0, prisionero1, "arma10", "arma20");
		Pelea pelea1 = new Pelea(1, genero.MASCULINO, prisionero2, prisionero3, "arma11", "arma21");
		Pelea pelea2 = new Pelea(2, genero.FEMENINO, prisionero4, prisionero5, "arma12", "arma22");
		Pelea pelea3 = new Pelea(3, genero.FEMENINO, prisionero6, prisionero7, "arma13", "arma23")