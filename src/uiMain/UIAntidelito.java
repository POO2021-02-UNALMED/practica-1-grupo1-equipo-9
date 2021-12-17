package uiMain;

import java.util.Hashtable;

public class UIAntidelito extends UI{
	
	public void ingresarAntidelito() {
		
	}
	
	public void borrarAntidelito() {
		
	}
	
	public void editarAntidelito() {
		
	}
	
	public void listarAntidelito() {
		
	}

	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar antidelito");
		lista_menu.put(2, "Borrar antidelito");
		lista_menu.put(3, "Editar antidelito");
		lista_menu.put(4, "Listar antidelito");
		lista_menu.put(5, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) {
		switch(op) {
	    		case 1: ingresarAntidelito(); break;
				case 2: borrarAntidelito(); break;
				case 3: editarAntidelito(); break;
				case 4: listarAntidelito(); break;
		}
	}

}
