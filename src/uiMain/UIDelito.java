package uiMain;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Delito;
import gestorAplicacion.carcel.Guardian;

public class UIDelito extends UI {
	static Scanner input = new Scanner(System.in);
	static InputStreamReader inputStrObj = new InputStreamReader(System.in);
	static BufferedReader bufrObj = new BufferedReader(inputStrObj);
	
	public void ingresarDelito() throws IOException {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();

		// Verificacion de codigo de delito existente
		Delito delito = Delito.getDelitos().get(codigo);
		if (delito!=null) {
			System.out.println("El delito ya exíste!\n");
		} else {
			System.out.print("Ingrese Nombre: ");
			String nombre = bufrObj.readLine();
			
			System.out.print("Ingrese Descripción: ");
			String descripcion = bufrObj.readLine();
			
			System.out.print("Ingrese Nivel: ");
			int nivel = input.nextInt();
			
			System.out.print("Ingrese tiempo condena: ");
			long tiempoCondena = input.nextInt();
			
			Delito delito1 = new Delito(codigo, nombre, descripcion, nivel, tiempoCondena);			
			
		}
	}
	
	public void borrarDelito() {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();
		
		Delito delito = Delito.getDelitos().remove(codigo);
		if (delito==null) {
			System.out.println("El delito no exíste!\n");
		} else {
			System.out.println("El delito fue borrado exitosamente!\n");
		}
	}
	
	public void editarDelito() throws IOException {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();
		
		Delito delito = Delito.getDelitos().get(codigo);
		if (delito!=null) {
			System.out.println("Deje en blanco(Srings) o ponga -1(integer) en los campos que no desea editar");
			String nombre = delito.getNombre();
			String descripcion = delito.getDescripcion(); 
			int nivel = delito.getNivel();
			long tiempoCondena = delito.getTiempoCondena();
			
			System.out.print("Nombre ["+nombre+"]: ");
			String nombre_input = bufrObj.readLine();
			if (!nombre_input.equals("")) {
				delito.setNombre(nombre_input);
			}
			
			System.out.print("Descripcion ["+descripcion+"]: ");
			String descripcion_input = bufrObj.readLine();
			if (!descripcion_input.equals("")) {
				delito.setDescripcion(descripcion_input);
			}
			
			System.out.print("Nivel ["+nivel+"]: ");
			int nivel_input = input.nextInt();
			if (!(nivel_input == -1) ) {
				delito.setNivel(nivel_input);
			}
			
			System.out.print("Tiempo de condena ["+tiempoCondena+"]: ");
			long tiempo_condena_input = input.nextLong();
			if (!(tiempo_condena_input  == -1) ) {
				delito.setTiempoCondena(tiempoCondena);
			}
			
			
			
		} else {
			System.out.println("El delito no exitosamente!\n");
		}
	}
	
	public void listarDelito() {
		System.out.println("**Listado Delitos**");

		Enumeration<Integer> e = Delito.getDelitos().keys();

        while (e.hasMoreElements()) {
            int key = e.nextElement();
            
            Delito delito = Delito.getDelitos().get(key);
            
            System.out.println(delito.toString());
        }
        System.out.println("");
	}

	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar delito");
		lista_menu.put(2, "Borrar delito");
		lista_menu.put(3, "Editar delito");
		lista_menu.put(4, "Listar delito");
		lista_menu.put(5, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) throws IOException {
		switch(op) {
    		case 1: ingresarDelito(); break;
			case 2: borrarDelito(); break;
			case 3: editarDelito(); break;
			case 4: listarDelito(); break;
		}
	}

}
