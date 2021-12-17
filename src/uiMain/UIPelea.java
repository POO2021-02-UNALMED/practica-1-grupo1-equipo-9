package uiMain;

import java.util.Hashtable;

public class UIPelea extends UI{

	// Función de prueba
	public void imprimirAlgo() {
		System.out.println("Se ejecuto na acción");
	}
	
	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar pelea");
		lista_menu.put(2, "Borrar pelea");
		lista_menu.put(3, "Editar pelea");
		lista_menu.put(4, "Listar pelea");
		lista_menu.put(5, "Imprimir algo");
		lista_menu.put(6, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) {
		switch(op) {
	    //		case 1: ingresarPrisionero(); break;
		//		case 2: borrarPrisionero(); break;
		//		case 3: editarPrisionero(); break;
		//		case 4: listarPrisionero(); break;
				case 5: imprimirAlgo(); break;
		}
	}

}
