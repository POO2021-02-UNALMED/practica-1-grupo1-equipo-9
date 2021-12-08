package uiMain;

import java.time.LocalDate;
import java.util.Hashtable;

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
		
	}

    public static void main(String[] args) {
        // TODO code application logic here
		
    }
}
