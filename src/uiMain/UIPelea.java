package uiMain;

import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.apuestas.Pelea;
import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Prisionero;
import gestorAplicacion.carcel.genero;

public class UIPelea extends UI {
	static Scanner input = new Scanner(System.in);

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
		switch (op) {
		case 1:
			registrarPelea();
			break;
		case 2:
			definirPelea();
			break;
		case 3:
			listarPeleas();
			break;
		case 4:
			battleRoyal();
			break;
		}
	}

	public void registrarPelea() {
		System.out.print("Ingrese el codigo de la pelea a registrar: ");
		int codigo = input.nextInt();

		if (Pelea.getPeleas().containsKey(codigo)) {
			System.out.print("Ya existe una pelea registrada con este codigo.\n");
			return;
		}
		System.out.print("Ingrese el genero de la pelea:\n" + "1. MASCULINA. \n" + "2. FEMENINA.");
		int gen = input.nextInt();
		genero gene;
		if (gen == 1) {
			gene = genero.MASCULINO;
		} else {
			gene = genero.FEMENINO;
		}

		if (Prisionero.prisionerosFEMENINOS.size() < 2 || Prisionero.prisionerosMASCULINOS.size() < 2) {
			System.out.println("\nNo existen suficientes peleadores :( \n");
			return;
		}

		ArrayList<Integer> idprisioneros = null;
		switch (gene) {
		case FEMENINO:
			idprisioneros = Prisionero.prisionerosFEMENINOS;
			break;
		case MASCULINO:
			idprisioneros = Prisionero.prisionerosMASCULINOS;
			break;
		}

		System.out.println("\nEstos son los peleadores disponibles con este genero:");
		for (Integer id : idprisioneros) {
			System.out.println("ID: " + id + ". Nombre : " + Prisionero.getPrisioneros().get(id).getNombre());
		}

		int luch1;
		do {
			System.out.print("Ingrese el ID del luchador 1: ");
			luch1 = input.nextInt();
		} while (!idprisioneros.contains(luch1));

		int luch2;
		do {
			System.out.print("Ingrese el ID del luchador 2: ");
			luch2 = input.nextInt();
		} while (!idprisioneros.contains(luch2) || luch1 == luch2);

		System.out.print("ingrese el arma del luchador 1: ");
		input.nextLine();
		String arma1 = input.nextLine();
		System.out.print("ingrese el arma del luchador 2: ");
		String arma2 = input.nextLine();

		System.out.println("\nSe registro la siguiente pelea exitosamente\n");
		System.out.println(new Pelea(codigo, gene, Prisionero.getPrisioneros().get(luch1),
				Prisionero.getPrisioneros().get(luch2), arma1, arma2));
	}

	public void definirPelea() {
		Hashtable<Integer, Pelea> peleas = Pelea.getPeleas();

		System.out.println("\nLas siguientes peleas aún no tienen ganador: \n");

		for (Integer k : peleas.keySet()) {
			if (peleas.get(k).getGanador() == null) {
				System.out.println(peleas.get(k));
			}
		}

		int cod;
		do {
			System.out.print("\nIngrese el código de la pelea: ");
			cod = input.nextInt();
		} while (!peleas.containsKey(cod) || peleas.get(cod).getGanador() != null);

		System.out.println(
				"\nEscoja al ganador de esta pelea: \n" + "1. " + peleas.get(cod).getLuchadores()[0].infoApostador()
						+ "\n" + "2. " + peleas.get(cod).getLuchadores()[1].infoApostador());
		int ganador = input.nextInt();

		if (ganador == 1) {
			peleas.get(cod).setGanador(peleas.get(cod).getLuchadores()[0]);
			System.out.println("\nSe registro al ganador con exito\n");
		} else if (ganador == 2) {
			peleas.get(cod).setGanador(peleas.get(cod).getLuchadores()[1]);
			System.out.println("\nSe registro al ganador con exito\n");
		} else {
			System.out.println("Numero invalido");
		}

	}

	public void listarPeleas() {
		System.out.println("\nA continuacion se listan todas las peleas que han" + "sido registradas en el sistema:\n");

		Hashtable<Integer, Pelea> peleas = Pelea.getPeleas();
		for (Integer k : peleas.keySet()) {
			System.out.println(peleas.get(k));
		}

	}

	public void battleRoyal() {
		System.out.println("Seleccione el género de este Battle Royal: \n" + "1. MASCULINA. \n" + "2. FEMENINA.");
		int gen = input.nextInt();
		genero gene;
		if (gen == 1) {
			gene = genero.MASCULINO;
		} else {
			gene = genero.FEMENINO;
		}
		
		ArrayList<Integer> idceldas = null;
		switch (gene) {
		case FEMENINO:
			idceldas = Celda.getCeldasFEMENINAS();
			break;
		case MASCULINO:
			idceldas = Celda.getCeldasMASCULINAS();
			break;
		}
		
		System.out.println("Las siguientes celdas están disponibles: ");
		for (Integer id : idceldas) {
			System.out.println(id);
		}
		
		ArrayList<Integer> celdasParticipantes = new ArrayList<>();
		
		System.out.println("\nSeleccione las celdas que participaran en el Battle Royal. \n"
				+ "Cuando termine de seleccionar todas celdas que desee, ingrese por pantalla -1: ");
		int opc;
		do {
			opc = input.nextInt();
			if (opc == -1) {break;}
			if (idceldas.contains(opc)) {
				if (!celdasParticipantes.contains(opc)) {
					celdasParticipantes.add(opc);
				}
			}
		} while (true);
		
		System.out.println("Las celdas participantes son:");
		for (Integer integer : celdasParticipantes) {
			System.out.print(integer + " ");
		}
		
		ArrayList<Celda> celdasParticipantes2 = new ArrayList<>();
		for (Integer integer : celdasParticipantes) {
			celdasParticipantes2.add(Celda.getCeldas().get(integer));
		}
		
		Object[] BY = Pelea.battleRoyale(celdasParticipantes2);
		ArrayList<String> combates = (ArrayList<String>) BY[0];
		
		System.out.println("\n El Battle Royal transcurrio de la siguiente manera...");
		for (String string : combates) {
			System.out.println(string);
		}
		
		
	}

}
