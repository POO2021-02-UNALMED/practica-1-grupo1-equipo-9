package uiMain;

import java.util.Hashtable;

public class UIDelito extends UI {

	public void ingresarDelito() {
		
	}
	
	public void borrarDelito() {
		
	}
	
	public void editarDelito() {
		
	}
	
	public void listarDelito() {
		
	}

	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar delito");
		lista_menu.put(2, "Borrar delito");
		lista_menu.put(3, "Editar delito");
		lista_menu.put(4, "Listar delito");
		lista_menu.put(5, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) {
		switch(op) {
    		case 1: ingresarDelito(); break;
			case 2: borrarDelito(); break;
			case 3: editarDelito(); break;
			case 4: listarDelito(); break;
		}
	}

}
