package uiMain;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.carcel.Antidelito;
import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Delito;
import gestorAplicacion.carcel.Guardian;
import gestorAplicacion.carcel.Prisionero;
import gestorAplicacion.carcel.genero;

public class UIPrisionero extends UI{
	static Scanner input = new Scanner(System.in);
	static InputStreamReader inputStrObj = new InputStreamReader(System.in);
	static BufferedReader bufrObj = new BufferedReader(inputStrObj);
	
	public void ingresarPrisionero() throws IOException{
		System.out.println("Ingrese el codigo de identificacion del prisionero: ");
		int identificacion = input.nextInt();
		if (Prisionero.getPrisioneros().containsKey(identificacion) || Guardian.getGuardianes().containsKey(identificacion)) {
			System.out.println("Esta identificacion ya se encuentra registrada");
			return;
		}
		
		System.out.print("Ingrese el nombre del prisionero: ");
		String nombre = bufrObj.readLine();;
		
		System.out.print("Ingrese el saldo del prisionero: ");
		int saldo = input.nextInt();
		
		System.out.println("Ingrese el genero del prisionero:\n"
                + "1. MASCULINO \n"
                + "2. FEMENINA");
        int gen = input.nextInt();
        genero gene;
        if (gen == 1) { gene = genero.MASCULINO; }
        else { gene = genero.FEMENINO; }
        
        System.out.println("Ingrese el numero de celda del prisionero.\n"
        		+ "Las celdas disponibles se mostraran a continuacion:");
        Hashtable<Integer, Celda> celdas = Celda.getCeldas(); 
        if (gen == 1) {
        	ArrayList<Integer> celdashombres = Celda.getCeldasMASCULINAS();
        	for (int k: celdashombres) {
        		if (celdas.get(k).getCapMax() > celdas.get(k).getPrisioneros().size()) {
        			System.out.println("Numero: " + celdas.get(k).getNumero());
        		}
        	}
        }else {
        	ArrayList<Integer> celdasmujeres = Celda.getCeldasFEMENINAS();
        	for (int k: celdasmujeres) {
        		if (celdas.get(k).getCapMax() > celdas.get(k).getPrisioneros().size()) {
        			System.out.println("Numero: " + celdas.get(k).getNumero());
        		}
        	}
        }
        
        int num = input.nextInt();
        if(!celdas.containsKey(num)) {
        	System.out.println("No se ha encontrado la celda ingresada");
        	return;
        }
        
        Celda celda = Celda.getCeldas().get(num);
        
        System.out.println("Ingrese los codigos de los delitos del prisionero dando enter entre cada uno.\n"
        		+ "Ingrese -1 para terminar su entrada."
        		+ "Los delitos se encuentran listados a continuación:");
        for (Integer k: Delito.getDelitos().keySet()) {
        	System.out.println("Codigo: " + Delito.getDelitos().get(k).getCodigo()
        			+ " Nombre: " + Delito.getDelitos().get(k).getNombre());
        }
        int delito;
        Hashtable<Integer, Delito> delitos = new Hashtable<>();
        while(true) {
        	delito = input.nextInt();
        	if(delito == -1) {
        		break;
        	}else {
        		if (Delito.getDelitos().containsKey(delito)) {
        			delitos.put(delito, Delito.getDelitos().get(delito));
        		}else {
        			System.out.println("El delito ingresado no es valido");
        		}
        	}
        }
        
        new Prisionero(identificacion,nombre,saldo,gene,celda,delitos);
        System.out.println("Prisionero ingresado correctamente");
	}
	
	public void borrarPrisionero() throws IOException {
		System.out.print("Ingrese la identificacion del prisionero que desea eliminar: ");
		int identificacion = input.nextInt();
		if (Prisionero.getPrisioneros().containsKey(identificacion)) {
			Prisionero.getPrisioneros().get(identificacion).getCelda().extraerPrisionero(Prisionero.getPrisioneros().get(identificacion));
			Prisionero.getPrisioneros().remove(identificacion);
			System.out.println("Prisionero eliminado correctamente");
		}else {
			System.out.println("El prisionero ingresado no se encuentra en la base de datos");
			return;
		}
		
	}
	
	public void agregarDelito() throws IOException{
		System.out.println("Ingrese la identificacion del prisionero:");
		int identificacion = input.nextInt();
		Prisionero prisionero = Prisionero.getPrisioneros().get(identificacion);
		if(prisionero != null) {
			System.out.println("Ingrese el codigo del delito que desea agregar.\n"
					+ "Los delitos se listan a continuacion:");
			for(Integer k: Delito.getDelitos().keySet()) {
				System.out.println("Codigo: " + Delito.getDelitos().get(k).getCodigo()
						+ " Nombre: " + Delito.getDelitos().get(k).getNombre());
			}
			int codigo = input.nextInt();
			Delito delito = Delito.getDelitos().get(codigo);
			if(delito != null) {
				prisionero.agregarDelito(delito);
				System.out.println("Se ha ingresado correctamente el delito");
			}else {
				System.out.println("No se encuentra el delito ingresado");
			}
		}
		else {
			System.out.println("El prisionero ingresado no se encuentra en la base de datos");
		}
	}
	
	public void agregarAntidelito() throws IOException{
		System.out.println("Ingrese la identificacion del prisionero:");
		int identificacion = input.nextInt();
		Prisionero prisionero = Prisionero.getPrisioneros().get(identificacion);
		if(prisionero != null) {
			System.out.println("Ingrese el codigo del antidelito que desea agregar.\n"
					+ "Los antidelitos se listan a continuacion:");
			for(Integer k: Antidelito.getAntidelitos().keySet()) {
				System.out.println("Codigo: " + Antidelito.getAntidelitos().get(k).getCodigo()
						+ " Nombre: " + Antidelito.getAntidelitos().get(k).getNombre());
			}
			int codigo = input.nextInt();
			Antidelito antidelito = Antidelito.getAntidelitos().get(codigo);
			if(antidelito != null) {
				prisionero.agregarAntidelito(antidelito);
				System.out.println("Se ha ingresado correctamente el antidelito");
			}else {
				System.out.println("No se encuentra el antidelito ingresado");
			}
		}
		else {
			System.out.println("El prisionero ingresado no se encuentra en la base de datos");
		}
	}
	
	public void listarPrisionero() {
		System.out.println("**Listado Prisioneros**");

		Enumeration<Integer> e = Prisionero.getPrisioneros().keys();

        while (e.hasMoreElements()) {
            int key = e.nextElement();
            
            Prisionero prisionero = Prisionero.getPrisioneros().get(key);
            
            System.out.println(prisionero.toString());
        }
        System.out.println("");
	}
	
	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar prisionero");
		lista_menu.put(2, "Borrar prisionero");
		lista_menu.put(3, "Listar prisioneros");
		lista_menu.put(4, "Agregar delito");
		lista_menu.put(5, "Agregar antidelito");
	
		lista_menu.put(6, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) throws IOException{
		switch(op) {
    		case 1: ingresarPrisionero(); break;
			case 2: borrarPrisionero(); break;
			case 3: listarPrisionero(); break;
			case 4: agregarDelito(); break;
			case 5: agregarAntidelito(); break;
		}
	}

}
