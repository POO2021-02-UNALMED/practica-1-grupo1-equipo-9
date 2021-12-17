package uiMain;
import java.io.IOException;
import java.util.*;

import baseDatos.Serializador;
import gestorAplicacion.apuestas.*;
import gestorAplicacion.carcel.*;

public class Menu {
	static Scanner input = new Scanner(System.in);
	static int option_out = 6;
	
	public static ArrayList<Hashtable> pila_menu = new ArrayList<>();
	public static Hashtable<Integer, String> menu_actual = new Hashtable<Integer, String>();
	public static ArrayList<Object> pila_objecto_actual = new ArrayList<>();
	public static Object objecto_actual;
	
	public Menu() {}

	Menu(Hashtable<Integer, String> lista_menu, Object objecto_actual){
		System.out.println("-------Carcel apuestera-------");
		setMenuActual(lista_menu, objecto_actual);
	}
	
	public static void setMenuActual(Hashtable<Integer, String> menu_actual, Object objecto_actual) {
		Menu.menu_actual = menu_actual;
		pila_menu.add(menu_actual);
		
		Menu.objecto_actual = objecto_actual;
		pila_objecto_actual.add(objecto_actual);
	}
	
	private static void setMenuAnterior() {
		pila_menu.remove(pila_menu.size()-1);
		pila_objecto_actual.remove(pila_objecto_actual.size()-1);
		
		if(pila_menu.size() > 0) {
			Menu.menu_actual = pila_menu.get(pila_menu.size()-1);			
			Menu.objecto_actual = pila_objecto_actual.get(pila_objecto_actual.size()-1);
		}
		
	}
	
	public void leerOpcion() throws IOException {
		int op;
		
		do {
			option_out = pintarMenu();
			op = input.nextInt();
			
			if (Menu.objecto_actual instanceof Menu) {
				((Menu)Menu.objecto_actual).ejecutarOpcion(op);
			} else if (Menu.objecto_actual instanceof UIGuardian) {
				((UIGuardian)Menu.objecto_actual).ejecutarOpcion(op);
			} else if (Menu.objecto_actual instanceof UIPrisionero) {
				((UIPrisionero)Menu.objecto_actual).ejecutarOpcion(op);
			} else if (Menu.objecto_actual instanceof UIDelito) {
				((UIDelito)Menu.objecto_actual).ejecutarOpcion(op);
			} else if (Menu.objecto_actual instanceof UIAntidelito) {
				((UIAntidelito)Menu.objecto_actual).ejecutarOpcion(op);
			} else if (Menu.objecto_actual instanceof UIPelea) {
				((UIPelea)Menu.objecto_actual).ejecutarOpcion(op);
			}
			
		} while(op < option_out);

		setMenuAnterior();
		
	}
	
	public static int pintarMenu(){
		int item = 1;
		
		while (true) {
			String valor = Menu.menu_actual.get(item);
			if(valor==null) {
				break;
			}
			System.out.println(item +". " + valor);
			item += 1;
		}
		System.out.print(": ");
		
		// Es la ultima opción del menu
		return item - 1;
	}
	
	/*
	 *  Opciones de menu
	 */
	public void gestionarGuardianes() throws IOException {
		UIGuardian g = new UIGuardian();
		Hashtable <Integer,String> ht1 = g.getMenu();
		Menu menu = new Menu(ht1, g);
		menu.leerOpcion();
		
		
	}
		
	public void gestionarPrisioneros() throws IOException {
		UIPrisionero p = new UIPrisionero();
		Hashtable<Integer, String> ht1 = p.getMenu();
		Menu menu = new Menu(ht1, p);
		menu.leerOpcion();
	}
	
	public void gestionarDelitos() throws IOException {
		UIDelito d = new UIDelito();
		Hashtable<Integer, String> ht1 = d.getMenu();
		Menu menu = new Menu(ht1, d);
		menu.leerOpcion();
	}
	
	public void gestionarAntidelitos() throws IOException {
		UIAntidelito d = new UIAntidelito();
		Hashtable<Integer, String> ht1 = d.getMenu();
		Menu menu = new Menu(ht1, d);
		menu.leerOpcion();
	}
	
	public void gestionarPeleas() throws IOException {
		UIPelea pl = new UIPelea();
		Hashtable<Integer, String> ht1 = pl.getMenu();
		Menu menu = new Menu(ht1, pl);
		menu.leerOpcion();
	}
	
	
	/*
	 * Debe implementarse en todos las clases
	 */
	public void ejecutarOpcion(int op) throws IOException {
		switch(op) {
			case 1: gestionarGuardianes(); break;
			case 2: gestionarPrisioneros(); break;
			case 3: gestionarDelitos(); break;
			case 4: gestionarAntidelitos(); break;
			case 5: gestionarPeleas(); break;
		}
	}
	

}
