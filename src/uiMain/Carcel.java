
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
    	
		
    	
		Deserializador.deserializar();
		
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

    }

}
