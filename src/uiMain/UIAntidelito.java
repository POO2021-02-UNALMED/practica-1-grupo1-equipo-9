package uiMain;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.carcel.Antidelito;

public class UIAntidelito extends UI{
	static Scanner input = new Scanner(System.in);
	static InputStreamReader inputStrObj = new InputStreamReader(System.in);
	static BufferedReader bufrObj = new BufferedReader(inputStrObj);
	
	public void ingresarAntidelito() throws IOException {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();

		// Verificacion de codigo de delito existente
		Antidelito antidelito = Antidelito.getAntidelitos().get(codigo);
		if (antidelito!=null) {
			System.out.println("El antidelito ya existe!\n");
		} else {
			System.out.print("Ingrese Nombre: ");
			String nombre = bufrObj.readLine();
			
			System.out.print("Ingrese Descripcion: ");
			String descripcion = bufrObj.readLine();
			
			System.out.print("Ingrese tiempo condena: ");
			long rebajaCondena = input.nextInt();
			
			new Antidelito(codigo, nombre, descripcion, rebajaCondena);			
			
		}
	}
	
	public void borrarAntidelito() {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();
		
		Antidelito antidelito = Antidelito.getAntidelitos().remove(codigo);
		if (antidelito==null) {
			System.out.println("El antidelito no existe!\n");
		} else {
			System.out.println("El antidelito fue borrado exitosamente!\n");
		}		
	}
	
	public void editarAntidelito() throws IOException {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();
		
		Antidelito antidelito = Antidelito.getAntidelitos().get(codigo);
		if (antidelito!=null) {
			System.out.println("Deje en blanco(Srings) o ponga -1(integer) en los campos que no desea editar");
			String nombre = antidelito.getNombre();
			String descripcion = antidelito.getDescripcion();
			long rebajaCondena = antidelito.getRebajaCondena();
			
			System.out.print("Nombre ["+nombre+"]: ");
			String nombre_input = bufrObj.readLine();
			if (!nombre_input.equals("")) {
				antidelito.setNombre(nombre_input);
			}
			
			System.out.print("Descripcion ["+descripcion+"]: ");
			String descripcion_input = bufrObj.readLine();
			if (!descripcion_input.equals("")) {
				antidelito.setDescripcion(descripcion_input);
			}
			
			System.out.print("Rebaja de condena ["+rebajaCondena+"]: ");
			long rebaja_condena_input = input.nextLong();
			if (!(rebaja_condena_input  == -1) ) {
				antidelito.setRebajaCondena(rebajaCondena);
			}
			
			
			
		} else {
			System.out.println("El antidelito no exitosamente!\n");
		}		
	}
	
	public void listarAntidelito() {
		System.out.println("**Listado Antidelitos**");

		Enumeration<Integer> e = Antidelito.getAntidelitos().keys();

        while (e.hasMoreElements()) {
            int key = e.nextElement();
            
            Antidelito antidelito = Antidelito.getAntidelitos().get(key);
            
            System.out.println(antidelito.toString());
        }
        System.out.println("");
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
	public void ejecutarOpcion(int op) throws IOException {
		switch(op) {
	    		case 1: ingresarAntidelito(); break;
				case 2: borrarAntidelito(); break;
				case 3: editarAntidelito(); break;
				case 4: listarAntidelito(); break;
		}
	}

}
