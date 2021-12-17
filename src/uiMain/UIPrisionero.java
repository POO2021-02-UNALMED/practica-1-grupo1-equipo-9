package uiMain;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.carcel.Antidelito;
import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Delito;
import gestorAplicacion.carcel.Prisionero;
import gestorAplicacion.carcel.genero;

public class UIPrisionero extends UI{
	static Scanner input = new Scanner(System.in);
	static InputStreamReader inputStrObj = new InputStreamReader(System.in);
	static BufferedReader bufrObj = new BufferedReader(inputStrObj);
	
	public void ingresarPrisionero() throws IOException{
		System.out.println("Ingrese el código de identificación del prisionero: ");
		int identificacion = input.nextInt();
		if (Prisionero.getPrisioneros().containsKey(identificacion)) {
			System.out.println("Este prisionero ya se encuentra en la base de datos");
			return;
		}
		
		System.out.print("Ingrese el nombre del prisionero: ");
		String nombre = bufrObj.readLine();;
		
		System.out.print("Ingrese el saldo del prisionero: ");
		int saldo = input.nextInt();
		
		System.out.println("Ingrese el género del prisionero:\n"
                + "1. MASCULINO \n"
                + "2. FEMENINA");
        int gen = input.nextInt();
        genero gene;
        if (gen == 1) { gene = genero.MASCULINO; }
        else { gene = genero.FEMENINO; }
        
        System.out.println("Ingrese el numero de celda del prisionero.\n"
        		+ "Las celdas disponibles se mostraran a continuación:");
        if (gen == 1) {
        	for (Integer numeroa: Celda.getCeldasMASCULINAS()) {
        		for (Integer numerob: Celda.getCeldas().keySet()) {
        			if (numeroa == numerob && Celda.getCeldas().get(numeroa).getCapMax() < Celda.getCeldas().get(numeroa).getPrisioneros().size()) {
        				System.out.println(numeroa);
        			}
        		}
        	}
        }else {
        	for (Integer numeroa: Celda.getCeldasFEMENINAS()) {
        		for (Integer numerob: Celda.getCeldas().keySet()) {
        			if (numeroa == numerob && Celda.getCeldas().get(numeroa).getCapMax() < Celda.getCeldas().get(numeroa).getPrisioneros().size()) {
        				System.out.println(numeroa);
        			}
        		}
        	}
        }
        
        int numero = input.nextInt();
        if (gen==1 && !Celda.getCeldasMASCULINAS().contains(numero)) {
        	System.out.println("La celda seleccionada no es valida");
        	return;
        } else if (!Celda.getCeldasFEMENINAS().contains(numero)) {
        	System.out.println("La celda seleccionada no es valida");
        	return;
        }
        Celda celda = Celda.getCeldas().get(numero);  
        
        System.out.println("Ingrese los codigos de los delitos del prisionero dando enter entre cada uno.\n"
        		+ "Ingrese -1 para terminar su entrada."
        		+ "Los delitos se encuentran listados a continuación:");
        for (Integer k: Delito.getDelitos().keySet()) {
        	System.out.println("Código: " + Delito.getDelitos().get(k).getCodigo()
        			+ "Nombre: " + Delito.getDelitos().get(k).getNombre());
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
        
        Prisionero prisionero1 = new Prisionero(identificacion,nombre,saldo,gene,celda,delitos);
        System.out.println("Prisionero ingresado correctamente");
	}
	
	public void borrarPrisionero() throws IOException {
		System.out.print("Ingrese la identificación del prisionero que desea eliminar: ");
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
			System.out.println("Ingrese el código del delito que desea agregar.\n"
					+ "Los delitos se listan a continuación:");
			for(Integer k: Delito.getDelitos().keySet()) {
				System.out.println("Código: " + Delito.getDelitos().get(k).getCodigo()
						+ "nombre: " + Delito.getDelitos().get(k).getNombre());
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
			System.out.println("Ingrese el código del antidelito que desea agregar.\n"
					+ "Los antidelitos se listan a continuación:");
			for(Integer k: Antidelito.getAntidelitos().keySet()) {
				System.out.println("Código: " + Antidelito.getAntidelitos().get(k).getCodigo()
						+ "nombre: " + Antidelito.getAntidelitos().get(k).getNombre());
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
