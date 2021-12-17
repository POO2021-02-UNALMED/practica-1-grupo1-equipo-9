package uiMain;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Hashtable;
import java.util.Scanner;

import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Guardian;
import gestorAplicacion.carcel.Prisionero;

public class UIGuardian extends UI {
	static Scanner input = new Scanner(System.in);
	static InputStreamReader inputStrObj = new InputStreamReader(System.in);
	static BufferedReader bufrObj = new BufferedReader(inputStrObj);
	
	private void listarCeldas() {
		System.out.println("**Listado de celdas**");

		Enumeration<Integer> e = Celda.getCeldas().keys();
		
		System.out.println("Numero  | Genero  | Largo  | Ancho   | Capacidad maxima");

        while (e.hasMoreElements()) {
            int key = e.nextElement();
            
            Celda celda = Celda.getCeldas().get(key);
            
            System.out.println(
            		key + " | "
            + celda.getNumero() + " | "
            + celda.getGenero() + " | "
            + celda.getLargo() + " | "
            + celda.getAncho() + " | "
            + celda.getCapMax());
        }
        System.out.println("");
	}
	
	public void ingresarGuardian() throws IOException {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();

		// Verificacion de codigo de guardian existente
		Guardian guardian = Guardian.getGuardianes().get(codigo);
		if (guardian!=null) {
			System.out.println("El guardían ya exíste!\n");
		} else {
			System.out.print("Ingrese Nombre: ");
			String nombre = bufrObj.readLine();
			
			System.out.print("Ingrese saldo: ");
			int saldo = input.nextInt();
			
			System.out.print("Ingrese salario: ");
			int salario = input.nextInt();
			
			System.out.print("Ingresar celda? [y/n]: ");
			String nueva_celda = bufrObj.readLine();
			
			
			if(nueva_celda.equals("y")) {
				
				listarCeldas();
				System.out.println("");
				
				Hashtable<Integer, Celda> celdas1 = new Hashtable<>();
				
				do {
					System.out.print("Ingrese identificador de celda: ");
					int celda_input = input.nextInt();
					Celda celda = Celda.getCeldas().get(celda_input);
					if(celda==null) {
						System.out.println("La celda no existe");
					} else {
						celdas1.put(celda_input, celda);
						System.out.println("Celda agregada");
					}
					
					System.out.print("Ingresar otra celda? [y/n]: ");
					nueva_celda = bufrObj.readLine();
					
				} while(nueva_celda.equals("y"));
				
				
				Guardian guardian1 = new Guardian(codigo, nombre, saldo, salario, celdas1);
			} else {
				Guardian guardian1 = new Guardian(codigo, nombre, saldo, salario);
			}
		}
		
	}
	
	public void borrarGuardian() {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();
		
		Guardian guardian = Guardian.getGuardianes().remove(codigo);
		if (guardian==null) {
			System.out.println("El guardían no exíste!\n");
		} else {
			System.out.println("El guardían fue borrado exitosamente!\n");
		}
	}
	
	public void editarGuardian() throws IOException {
		System.out.print("Ingrese codigo: ");
		int codigo = input.nextInt();
		
		Guardian guardian = Guardian.getGuardianes().get(codigo);
		if (guardian!=null) {
			System.out.println("Deje en blanco(Srings) o ponga -1(integer) en los campos que no desea editar");
			String nombre = guardian.getNombre();
			int salario = guardian.getSalario(); 
			int saldo = guardian.getSaldo();
			// TODO: editar celdas
			
			System.out.print("Nombre ["+nombre+"]: ");
			String nombre_input = bufrObj.readLine();
			if (!nombre_input.equals("")) {
				guardian.setNombre(nombre_input);
			}
			
			System.out.print("Salario ["+salario+"]: ");
			int salario_input = input.nextInt();
			if (!(salario_input == -1) ) {
				guardian.setSalario(salario_input);
			}
			
			System.out.print("Saldo ["+saldo+"]: ");
			int saldo_input = input.nextInt();
			if (!(saldo_input  == -1) ) {
				guardian.setSalario(saldo_input );
			}
			
			
			
		} else {
			System.out.println("El guardían no exitosamente!\n");
		}
	}
	
	public void listarGuardianes() {
		System.out.println("**Listado guardianes**");

		Enumeration<Integer> e = Guardian.getGuardianes().keys();
		System.out.println("Identificacion  | Nombre   | Salario  | Saldo");

        while (e.hasMoreElements()) {
            int key = e.nextElement();
            
            Guardian guardian = Guardian.getGuardianes().get(key);
            
            System.out.println(
            		key + " | "
            + guardian.getNombre() + " | "
            + guardian.getSalario() + " | "
            + guardian.getSaldo());
        }
        System.out.println("");
	}
	
	public void transladarPrisionero() {
		System.out.print("Elija un guardian ingresando el identificador: ");
		int codigo = input.nextInt();
		Guardian guardian = Guardian.getGuardianes().get(codigo);
		
		if (guardian!=null) {
			System.out.print("Ingresa el identificador del prisionero: ");
			int codigo_prisionero = input.nextInt();
			Prisionero prisionero = Prisionero.getPrisioneros().get(codigo_prisionero);
			
			if (prisionero!=null) {
				System.out.print("Ingresa el numero de celda: ");
				int numero_celda = input.nextInt();
				Celda celda = Celda.getCeldas().get(numero_celda);
				
				if (celda!=null) {
					guardian.trasladarPrisionero(prisionero, celda);
					System.out.println("Prisionero transladado exitosamente");
				} else {
					System.out.println("Lo sentimos la celda no existe.");
				}
				
			} else {
				System.out.println("Lo sentimos el prisionero no existe.");
			}
			
			
		} else {
			System.out.println("El guardían no exitosamente!\n");
		}
		

	}
	
	public void listarTraslados() {
		System.out.print("Ingrese identificador de guardian: ");
		int codigo = input.nextInt();
		Guardian guardian = Guardian.getGuardianes().get(codigo);

		if (guardian!=null) {
			ArrayList<String> translados = guardian.listaTraslados();
			for(String s: translados) {
				System.out.println(s);
			}
		} else {
			System.out.println("El guardían no exitosamente!\n");
		}
	}

	@Override
	public Hashtable<Integer, String> getMenu() {
		Hashtable<Integer, String> lista_menu = new Hashtable<>();
		lista_menu.put(1, "Ingresar guardian");
		lista_menu.put(2, "Borrar guardian");
		lista_menu.put(3, "Editar guardian");
		lista_menu.put(4, "Listar guardian");
		lista_menu.put(5, "Transladar prisionero");
		lista_menu.put(6, "Listar transladados");
		lista_menu.put(7, "Salir");
		return lista_menu;
	}

	@Override
	public void ejecutarOpcion(int op) throws IOException {
		switch(op) {
			case 1: ingresarGuardian(); break;
			case 2: borrarGuardian(); break;
			case 3: editarGuardian(); break;
			case 4: listarGuardianes(); break;
			case 5: transladarPrisionero(); break;
			case 6: listarTraslados(); break;
		}
	}

}
