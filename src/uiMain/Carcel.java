package uiMain;

import java.time.LocalDate;

import gestorAplicacion.carcel.Antidelito;
import gestorAplicacion.carcel.Celda;
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
		Delito delito7 = new Delito(7, "Batalla", "Participar en la batalla del Departamento de Misterios como mortífago", 5, 360);
		Delito delito8 = new Delito(8, "Batalla", "Participar en la batalla del Departamento de Misterios", 5, 50);
		Delito delito9 = new Delito(9, "9", "9", 7, 500);
		Delito delito10 = new Delito(10, "10", "10", 4, 10);
		
		
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
