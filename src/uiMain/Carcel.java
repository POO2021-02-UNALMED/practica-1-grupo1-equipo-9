package uiMain;

import java.time.LocalDate;
import java.util.Hashtable;

import gestorAplicacion.apuestas.Pelea;
import gestorAplicacion.carcel.Antidelito;
import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Guardian;
import gestorAplicacion.carcel.Prisionero;
import gestorAplicacion.carcel.genero;
import gestorAplicacion.carcel.Delito; 

public class Carcel {
	
	static {
//		crearDelitos
		Delito delito1 = new Delito(1, "Robo", "Apropiarse de un bien ajeno de manera fraudulenta, empleando la fuera, violencia o intimidacion ", 2, 10);
		Delito delito2 = new Delito(2, "Pelea callejera", "Enfrentarse fisicamente con otra persona o animal en lugares publicos", 1, 12);
		Delito delito3 = new Delito(3, "3", "3", 6, 48);
		Delito delito4 = new Delito(4, "4", "4", 8, 200);
		Delito delito5 = new Delito(5, "5", "5", 9, 360);
		Delito delito6 = new Delito(6, "6", "6", 3, 24);
		Delito delito7 = new Delito(7, "Batalla", "Participar en la batalla del Departamento de Misterios como mortifago", 5, 360);
		Delito delito8 = new Delito(8, "Batalla", "Participar en la batalla del Departamento de Misterios", 5, 50);
		Delito delito9 = new Delito(9, "9", "9", 7, 500);
		Delito delito10 = new Delito(10, "10", "10", 4, 10);
		
		Hashtable<Integer, Delito> delitos1 = new Hashtable<>();
		delitos1.put(delito1.getCodigo(), delito1);
		delitos1.put(delito5.getCodigo(), delito5);
		delitos1.put(delito9.getCodigo(), delito9);
		
		Hashtable<Integer, Delito> delitos2 = new Hashtable<>();
		delitos2.put(delito9.getCodigo(), delito9);
		
		Hashtable<Integer, Delito> delitos3 = new Hashtable<>();
		delitos3.put(delito7.getCodigo(), delito7);
		delitos3.put(delito3.getCodigo(), delito3);
		
		Hashtable<Integer, Delito> delitos4 = new Hashtable<>();
		delitos4.put(delito10.getCodigo(), delito10);
		
		Hashtable<Integer, Delito> delitos5 = new Hashtable<>();
		delitos5.put(delito2.getCodigo(), delito2);
		delitos5.put(delito4.getCodigo(), delito4);
		delitos5.put(delito6.getCodigo(), delito6);
		delitos5.put(delito8.getCodigo(), delito8);
		
//		crearCeldas
		Celda celda0 = new Celda(0, genero.MASCULINO, 1.5, 4, 2);
		Celda celda1 = new Celda(1, genero.MASCULINO, 1.5, 4, 3);
		Celda celda2 = new Celda(2, genero.MASCULINO, 1.5, 4, 4);
		Celda celda3 = new Celda(3, genero.MASCULINO, 1.5, 4, 2);
		Celda celda4 = new Celda(4, genero.MASCULINO, 1.5, 4, 3);
		Celda celda5 = new Celda(5, genero.FEMENINO, 1.5, 4, 4);
		Celda celda6 = new Celda(6, genero.FEMENINO, 1.5, 4, 5);
		Celda celda7 = new Celda(7, genero.FEMENINO, 1.5, 4, 6);
		Celda celda8 = new Celda(8, genero.FEMENINO, 1.5, 4, 2);
		Celda celda9 = new Celda(9, genero.FEMENINO, 1.5, 4, 3);
		
//		crearPrisioneros 
		Hashtable<Integer, Delito>  delitos00 = new Hashtable<>(); delitos00.put(delito1.getCodigo(), delito1);
		Hashtable<Integer, Delito>  delitos11 = new Hashtable<>(); delitos11.put(delito1.getCodigo(), delito1); delitos11.put(delito2.getCodigo(), delito2);
		Hashtable<Integer, Delito>  delitos22 = new Hashtable<>(); delitos22.put(delito1.getCodigo(), delito1); delitos22.put(delito3.getCodigo(), delito3); delitos22.put(delito4.getCodigo(), delito4);
		Hashtable<Integer, Delito>  delitos33 = new Hashtable<>(); delitos33.put(delito4.getCodigo(), delito4); delitos33.put(delito2.getCodigo(), delito2); delitos33.put(delito5.getCodigo(), delito5); delitos3.put(delito9.getCodigo(), delito9);
		Hashtable<Integer, Delito>  delitos44 = new Hashtable<>(); delitos44.put(delito6.getCodigo(), delito6); delitos44.put(delito2.getCodigo(), delito2); delitos44.put(delito10.getCodigo(), delito10);
		Hashtable<Integer, Delito>  delitos55 = new Hashtable<>(); delitos55.put(delito6.getCodigo(), delito6); delitos55.put(delito5.getCodigo(), delito5);
		Hashtable<Integer, Delito>  delitos66 = new Hashtable<>(); delitos66.put(delito7.getCodigo(), delito7); delitos66.put(delito8.getCodigo(), delito8); delitos66.put(delito9.getCodigo(), delito9);
		Hashtable<Integer, Delito>  delitos77 = new Hashtable<>(); delitos77.put(delito8.getCodigo(), delito8); delitos77.put(delito5.getCodigo(), delito5); delitos77.put(delito10.getCodigo(), delito10);
		
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
		Prisionero prisionero12 = new Prisionero(12, "nombre12", 200, genero.FEMENINO, celda9, delitos66);
		
//		crearGuardianes
		Hashtable<Integer, Celda> celdas1 = new Hashtable<>();
		celdas1.put(celda0.getNumero(), celda0);
		celdas1.put(celda9.getNumero(), celda9);
		celdas1.put(celda5.getNumero(), celda5);
		
		Hashtable<Integer, Celda> celdas2 = new Hashtable<>();
		celdas2.put(celda1.getNumero(), celda1);
		celdas2.put(celda8.getNumero(), celda8);
		celdas2.put(celda4.getNumero(), celda4);
		
		Hashtable<Integer, Celda> celdas3 = new Hashtable<>();
		celdas3.put(celda3.getNumero(), celda3);
		celdas3.put(celda7.getNumero(), celda7);
		celdas3.put(celda2.getNumero(), celda2);
		
		Hashtable<Integer, Celda> celdas4 = new Hashtable<>();
		celdas4.put(celda2.getNumero(), celda2);
		celdas4.put(celda6.getNumero(), celda6);
		celdas4.put(celda9.getNumero(), celda9);
		
		Hashtable<Integer, Celda> celdas5 = new Hashtable<>();
		celdas5.put(celda5.getNumero(), celda5);
		celdas5.put(celda8.getNumero(), celda8);
		celdas5.put(celda7.getNumero(), celda7);
		
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
		Pelea pelea3 = new Pelea(3, genero.FEMENINO, prisionero6, prisionero7, "arma13", "arma23");
		
	}

    public static void main(String[] args) {
        // TODO code application logic here
		
    }
}
