package uiMain;

import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.apuestas.Pelea;
import gestorAplicacion.carcel.Prisionero;
import gestorAplicacion.carcel.genero;

public class UIPelea extends UI{
	static Scanner input = new Scanner(System.in);

	// Funcion de prueba
	public void imprimirAlgo() {
		System.out.println("Se ejecuto una accion");
	}
	
	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Registrar pelea nueva");
		lista_menu.put(2, "Definir resultado de pelea");
		lista_menu.put(3, "Listar peleas");
		lista_menu.put(4, "Battle Royal");
		lista_menu.put(5, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) {
		switch(op) {
	    		case 1: registrarPelea(); break;
				case 2: definirPelea(); break;
				case 3: listarPeleas(); break;
				case 4: battleRoyal(); break;
		}
	}
	
	public void 
	registrarPelea() {
		System.out.print("Ingrese el código de la pelea a registrar: ");
		int codigo = input.nextInt();
		
		if (Pelea.getPeleas().containsKey(codigo)) {
			System.out.print("Ya existe una pelea registrada con este código.\n");
			return;
		}
		System.out.print("Ingrese el género de la pelea:\n"
				+ "1. MASCULINA. \n"
				+ "2. FEMENINA.");
		int gen = input.nextInt();
		genero gene;
		if (gen == 1) { gene = genero.MASCULINO; }
		else { gene = genero.FEMENINO; }
		
		if (Prisionero.prisionerosFEMENINOS.size() < 2 || Prisionero.prisionerosMASCULINOS.size() < 2) {
			System.out.println("\nNo existen suficientes peleadores :( \n");
			return;
		}
		
		System.out.println("\nEstos son los peleadores disponibles con este género:");
		
		switch (gene) {
		case FEMENINO: 
			for (String prisionerosFEMENINOS : Prisionero.prisionerosFEMENINOS) {
				System.out.println(prisionerosFEMENINOS);
			}
		case MASCULINO:
			for (String prisionerosMASCULINO : Prisionero.prisionerosMASCULINOS) {
				System.out.println(prisionerosMASCULINO);
			}
		}
		
		int luch1;
		do {
			System.out.print("Ingrese el ID del luchador 1: ");
			luch1 = input.nextInt();
		} while (!Prisionero.getPrisioneros().containsKey(luch1));
		
		int luch2;
		do {
			System.out.print("Ingrese el ID del luchador 2: ");
			luch2 = input.nextInt();
		} while (!Prisionero.getPrisioneros().containsKey(luch2) || luch1 == luch2);
		
		System.out.print("ingrese el arma del luchador 1: ");
		String arma1 = input.nextLine();
		System.out.print("ingrese el arma del luchador 2: ");
		String arma2 = input.nextLine();
		
		new Pelea(codigo, gene, Prisionero.getPrisioneros().get(luch1), Prisionero.getPrisioneros().get(luch2), arma1, arma2);
		System.out.println("\nSe registró la nueva pelea exitosamente\n");
	}
	
	public void
	definirPelea() {
		
	}
	
	public void
	listarPeleas() {
		
	}
	
	public void
	battleRoyal() {
		
	}

}
