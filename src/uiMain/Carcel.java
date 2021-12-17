
package uiMain;

import java.io.IOException;
import java.time.LocalDate;
import java.util.Hashtable;
import java.util.Scanner;
import java.util.ArrayList;

import baseDatos.Deserializador;
import baseDatos.Serializador;
import gestorAplicacion.apuestas.Pelea;
import gestorAplicacion.carcel.Antidelito;
import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Guardian;
import gestorAplicacion.carcel.Prisionero;
import gestorAplicacion.carcel.genero;
import gestorAplicacion.carcel.Delito; 

public class Carcel {
	static Scanner input = new Scanner(System.in);
	static long readLong() {
		return input.nextLong();
	}
	
    public static void main(String[] args) throws IOException {
    	

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
		Prisionero prisionero12 = new Prisionero(12, "nombre12", 200, genero.FEMENINO, celda8, delitos66);
		Prisionero prisionero13 = new Prisionero(13, "nombre13", 120, genero.MASCULINO, celda2, delitos66);
		Prisionero prisionero14 = new Prisionero(14, "nombre14", 50, genero.FEMENINO, celda6, delitos77);
		Prisionero prisionero15 = new Prisionero(15, "nombre15", 0, genero.FEMENINO, celda7, delitos44);
		
		
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
		
		ArrayList<Celda> battleRoyal1 = new ArrayList<>();
		battleRoyal1.add(celda1);
		battleRoyal1.add(celda2);
		battleRoyal1.add(celda3);
		Object br = pelea1.battleRoyale(battleRoyal1);
		
		System.out.print(br);
		
//		---------------------------------------------------------------------------------------------------
		
		System.out.println(delito1);
		System.out.println(celda5);
		System.out.println(guardian3);
		System.out.println(prisionero11);
		System.out.println(prisionero1);
		System.out.println(prisionero0);
		System.out.println(pelea0);
		
		pelea0.getApuesta().agregarApostador(guardian5, prisionero0, 30);
		pelea0.getApuesta().agregarApostador(guardian4, prisionero0, 10);
		pelea0.getApuesta().agregarApostador(prisionero10, prisionero1, 20);
		pelea0.getApuesta().agregarApostador(prisionero14, prisionero1, 10);
		
		pelea0.setGanador(prisionero0);
		System.out.println(pelea0.getApuesta().resultadoApuesta());
		
		System.out.println("\n---------------------------------------------------------------\n");
		
		ArrayList<Object[]> temp1 =  guardian1.getTraslados();
		Object[] trasnaldo0 = {celda0, prisionero0, celda0};
		temp1.add(trasnaldo0);
		Object[] trasnaldo1 = {celda1, prisionero1, celda1};
		temp1.add(trasnaldo1);
		Object[] trasnaldo2 = {celda2, prisionero2, celda2};
		temp1.add(trasnaldo2);
		Object[] trasnaldo3 = {celda3, prisionero3, celda3};
		temp1.add(trasnaldo3);
		
		guardian1.listaTraslados().forEach(x -> System.out.println(x));
		
    	// Inicicializador de Menu principal
		Hashtable<Integer, String> menu_actual = new Hashtable<>();
		menu_actual.put(1, "Gestionar Guardianes");
		menu_actual.put(2, "Gestionar Prisioneros");
		menu_actual.put(3, "Gestionar Delitos");
		menu_actual.put(4, "Gestionar Antidelitos");
		menu_actual.put(5, "Gestionar Peleas");
		menu_actual.put(6, "Gestionar Apuestas");
		menu_actual.put(7, "Salir");
		
		Menu m = new Menu();
		Menu menu = new Menu(menu_actual, m);
		menu.leerOpcion();
		
		Serializador.serializar();
		Deserializador.deserializar();

			int opcion;
			
			do {
				System.out.println("Escoga la opcion que desea realizar: ");
				System.out.println("1. Ingresar nueva informacion");
				System.out.println("2. Modificar informacion");
				System.out.println("3. Eliminar informacion");
				System.out.println("4. Consultar informacion");
				System.out.println("5. Peleas y apuestas");
				System.out.println("0. Salir");
				opcion = input.nextInt();
				switch(opcion) {
					case 1: ingresarInfo(); break;
					case 2: modificarInfo(); break;
					case 3: eliminarInfo(); break;
					case 4: consultarInfo(); break;
					case 5: peleasApuestas(); break;
					case 0: Serializador.serializar();
				}
			}while(opcion!=0);	
    }

	static void ingresarInfo() {
		int opcion;
		do {
			System.out.println("1. Ingresar nuevo prisionero");
			System.out.println("2. Ingresar nuevo guardia");
			System.out.println("3. Registrar delito");
			System.out.println("4. Registrar antidelito");
			System.out.println("5. Regresar");
			opcion=input.nextInt();
			switch(opcion) {
				case 1: ingresarPrisionero(); break;
				case 2: ingresarGuardia(); break;
				case 3: registrarDelito(); break;
				case 4: registrarAntidelito(); break;
				case 5: break;
			}
		}while(opcion!=5);	
	}
	
	static void modificarInfo() {	
		int opcion;
		do {
			System.out.println("1. Modificar prisionero"); 
			System.out.println("2. Modificar guardia");
			System.out.println("3. Modificar delito");
			System.out.println("4. Modificar antidelito");
			System.out.println("5. Regresar");
			opcion=input.nextInt();
			switch(opcion) {
				case 1: modificarPrisionero(); break;
				case 2: modificarGuardia(); break;
				case 3: modificarDelito(); break;
				case 4: modificarAntidelito(); break;
				case 5: break;
			}
		}while(opcion!=5);	
	}

	static void consultarInfo() {
	
		int opcion;
		do {
			System.out.println("1. Consultar prisionero");
			System.out.println("2. Consultar guardia");
			System.out.println("3. Consultar delito");
			System.out.println("4. Consultar antidelito");
			System.out.println("5. Regresar");
			opcion=input.nextInt();
			switch(opcion) {
				case 1: consultarPrisionero(); break;
				case 2: consultarGuardia(); break;
				case 3: consultarDelito(); break;
				case 4: consultarAntidelito(); break;
				case 5: break;
			}
		}while(opcion!=5);	
	}
	
	static void eliminarInfo() {
		
		int opcion;
		do {
			System.out.println("1. Eliminar prisionero");
			System.out.println("2. Eliminar guardia");
			System.out.println("3. Eliminar delito");
			System.out.println("4. Eliminar antidelito");
			System.out.println("5. Regresar");
			opcion=input.nextInt();
			switch(opcion) {
				case 1: eliminarPrisionero(); break;
				case 2: eliminarGuardia(); break;
				case 3: eliminarDelito(); break;
				case 4: eliminarAntidelito(); break;
				case 5: break;
			}
		}while(opcion!=5);	
	}
	
	static void ingresarPrisionero() {
		
	}
	static void ingresarGuardia() {
		
	}
	static void registrarDelito() {
		
	}
	static void registrarAntidelito() {
		
	}
    static void peleasApuestas() {
    	int opcion;
		do {
			System.out.println("1. Resolver pelea"); //se ingresas los ganadores y se llama al m�todo serGanador()
			System.out.println("2. Consultar pelea");//se imprimen las peleas
			System.out.println("3. Consultar apuesta");
			System.out.println("4. Agregar apostador"); //se llama al metodo agregarApostador de apuesta de la pelea agregada
			System.out.println("5. Regresar");
			opcion=input.nextInt();
			switch(opcion) {
				case 1: resolverPelea(); break;
				case 2: consultarPelea(); break;
				case 3: consultarApuesta(); break;
				case 4: agregarApostador(); break;
				case 5: break;
			}
		}while(opcion!=5);	
	}
	static void modificarPrisionero() {
		/*Desde este metodo se da la opcion de trasladar prisionero primero se pide
		 * numero de celda, se debe comprobar que sea el mismo genero, despues se muestran
		 * todos los guardias que tienen a cargo esa celda,se llama al metodo trasladar 
		 * prisionero del guardia que se decidio que iba a trasladar al prisionero*/
		
		// Tambien esta la opcion de agregarDelito y agregarAntidelitos
	}
	static void modificarGuardia() {
		
	}
	static void modificarDelito() {
		
	}
	static void modificarAntidelito() {
		
	}
	
	static void eliminarPrisionero() {
		
	}
	static void eliminarGuardia() {
		
	}
	static void eliminarDelito() {
		
	}
	static void eliminarAntidelito() {
		
	}
	
	static void consultarPrisionero() {
		
	}
	static void consultarGuardia() {
		
	}
	static void consultarDelito() {
		
	}
	static void consultarAntidelito() {
		
	}
	static void resolverPelea() {

	}
	static void consultarPelea() {

	}
	static void consultarApuesta(){

	}
	static void agregarApostador(){

	}
}
