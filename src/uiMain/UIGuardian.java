package uiMain;

import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Guardian;

public class UIGuardian extends UI {
	static Scanner input = new Scanner(System.in);
	
	public void ingresarGuardian() {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();
		// TODO: Verificar codigo existente
		
		System.out.print("Ingrese Nombre: ");
		String nombre = input.nextLine();
		input.nextLine();
		
		System.out.print("Ingrese saldo: ");
		int saldo = input.nextInt();
		
		System.out.print("Ingrese salario: ");
		int salario = input.nextInt();
		
		System.out.print("Ingresar celda? [y/n]: ");
		String nueva_celda = input.nextLine();
		input.nextLine();
		
		if(nueva_celda.equals("y")) {
			// TODO: Listar celdas
			
			Hashtable<Integer, Celda> celdas1 = new Hashtable<>();
			celdas1.put(1, null);
			
//			System.out.print("Ingresar identificador de celda: ");
//			int celda = input.nextInt();
			
			
			Guardian guardian1 = new Guardian(codigo, nombre, saldo, salario, celdas1);
		} else {
			Guardian guardian1 = new Guardian(codigo, nombre, saldo, salario);
		}
		
	}
	
	public void listarGuardian() {
		System.out.println("Listado guardianes");
		System.out.println(Guardian.getGuardianes().toString());
	}
	

	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar guardian");
		lista_menu.put(2, "Borrar guardian");
		lista_menu.put(3, "Editar guardian");
		lista_menu.put(4, "Listar guardian");
		lista_menu.put(5, "guardia.trasladarPrisionero(prisionero, celda)");
		lista_menu.put(6, "listaTraslados()");
		
		lista_menu.put(8, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) {
		switch(op) {
			case 1: ingresarGuardian(); break;
	//		case 2: gestionarPrisioneros(); break;
	//		case 3: gestionarDelitos(); break;
			case 4: listarGuardian(); break;
	//		case 5: gestionarPeleas(); break;
		}
	}

}
