package uiMain;

import java.io.IOException;
import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.apuestas.Apostador;
import gestorAplicacion.apuestas.Apuesta;
import gestorAplicacion.apuestas.Pelea;
import gestorAplicacion.carcel.Guardian;
import gestorAplicacion.carcel.Prisionero;

public class UIApuesta extends UI{
	static Scanner input = new Scanner(System.in);
	
	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar apostador");
		lista_menu.put(2, "Resultados de apuestas");
		lista_menu.put(3, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) throws IOException {
		switch(op) {
			case 1: ingresarApostador(); break;
			case 2: resultadosApuestas(); break;
		}
	}

	public void 
	ingresarApostador() {
		
		System.out.print("\nIngrese la identificaci�n del apostador: ");
		int id = input.nextInt();
		Apostador ap;
		if (Prisionero.getPrisioneros().containsKey(id)) {
			ap = Prisionero.getPrisioneros().get(id);
		} else if (Guardian.getGuardianes().containsKey(id)) {
			ap = Guardian.getGuardianes().get(id);
		} else {
			System.out.println("En el sistema no se encuentran registrados apostadores con tal ID");
			return;
		}
		
		Hashtable<Integer, Pelea> peleas = Pelea.getPeleas();
		System.out.println("\nEn las siguientes peleas a�n se puede apostar: \n");

		for (Integer k : peleas.keySet()) {
			if (peleas.get(k).getGanador() == null) {
				System.out.println(peleas.get(k));
			}
		}
		
		int cod;
		do {
			System.out.print("\nIngrese el c�digo de la pelea: ");
			cod = input.nextInt();
		} while (!peleas.containsKey(cod) || peleas.get(cod).getGanador() != null);
		
		Pelea pelea = peleas.get(cod);
		
		System.out.println(
				"\nEscoja al peleador por el que va a apostar: \n" + "1. " + pelea.getLuchadores()[0].infoApostador()
						+ "\n" + "2. " + pelea.getLuchadores()[1].infoApostador());
		int ganador = input.nextInt();
		Prisionero prisionero;
		if (ganador == 1) {
			prisionero = pelea.getLuchadores()[0];
		} else if (ganador == 2) {
			prisionero = pelea.getLuchadores()[1];
		} else {
			System.out.println("Numero invalido");
			return;
		}
		
		System.out.println("\nIngrese el dinero que desea apostar: ");
		int apuesta = input.nextInt();
		
		
		pelea.getApuesta().agregarApostador(ap, prisionero, apuesta);
		System.out.println("\nApostador registrado con �xito\n");

		
	}
	
	public void 
	resultadosApuestas() {
		System.out.println("\nLos siguientes son los resultados actuales de cada apuesta registrada en el sistema: \n");
		
		Hashtable<Integer, Apuesta> apuestas = Apuesta.getApuestas();
		for (Integer k : apuestas.keySet()) {
			System.out.println(apuestas.get(k).resultadoApuesta());
			System.out.println("\n---------------\n");
		}
		
	}

}
