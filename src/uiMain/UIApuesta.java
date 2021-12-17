package uiMain;

import java.io.IOException;
import java.util.Hashtable;

public class UIApuesta extends UI{
	public void ingresarApuesta() {
		System.out.println("Funciona");
	}

	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar apuesta");
		lista_menu.put(2, "Borrar apuesta");
		lista_menu.put(3, "Editar apuesta");
		lista_menu.put(4, "Listar apuesta");
		lista_menu.put(5, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) throws IOException {
		switch(op) {
			case 1: ingresarApuesta(); break;
//			case 2: borrarApuesta(); break;
//			case 3: editarApuesta(); break;
//			case 4: listarApuesta(); break;
		}
	}

}
