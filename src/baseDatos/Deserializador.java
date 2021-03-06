package baseDatos;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.apuestas.Apuesta;
import gestorAplicacion.apuestas.Pelea;
import gestorAplicacion.carcel.Antidelito;
import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Delito;
import gestorAplicacion.carcel.Guardian;
import gestorAplicacion.carcel.Prisionero;

public class Deserializador {
	private static String rutaTemp = System.getProperty("user.dir") + "\\src\\baseDatos\\temp";
	private static FileInputStream fileIn;

	public static void deserializar() {
		deserializarAntidelitos();
		deserializarPeleas();
		deserializarApuestas();
		deserializarPrisioneros();
		deserializarGuardianes();
		deserializarDelitos();
		deserializarCeldas();
		/* 
		 * Por la forma en que se dise�o el programa, cada que se crea un objeto este se agrega
		 * a la Hashtable de esa clase, entonces no se deserializa cada objeto individualmente 
		 * sino que se guardan en una Hashtable todos los objetos que fueron creados, se deserializa
		 * esta Hashtable y se le asigna a la Hashtable de la clase.
		 */
	}

	private static 
	void deserializarApuestas() {
		try {
			fileIn = new FileInputStream(rutaTemp + "\\apuestas.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			Hashtable<Integer, Apuesta> hashtable = (Hashtable<Integer, Apuesta>) in.readObject();
			
			Apuesta.setApuestas(hashtable);
			
			in.close();
			fileIn.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void deserializarPeleas() {
		try {
			fileIn = new FileInputStream(rutaTemp + "\\peleas.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			Hashtable<Integer, Pelea> hashtable = (Hashtable<Integer, Pelea>) in.readObject();
			
			Pelea.setPeleas(hashtable);
			
			in.close();
			fileIn.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void deserializarPrisioneros() {
		try {
			fileIn = new FileInputStream(rutaTemp + "\\prisioneros.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			Hashtable<Integer, Prisionero> hashtable = (Hashtable<Integer, Prisionero>) in.readObject();
			
			Prisionero.setPrisioneros(hashtable);
			
			in.close();
			fileIn.close();
			
			
			fileIn = new FileInputStream(rutaTemp + "\\prisionerosMASCULINOS.txt");
			
			ObjectInputStream in2 = new ObjectInputStream(fileIn);
			
			ArrayList<Integer> tabla2 = (ArrayList<Integer>) in2.readObject();
			
			Prisionero.prisionerosMASCULINOS = tabla2;
			
			in2.close();
			fileIn.close();
			
			
			fileIn = new FileInputStream(rutaTemp + "\\prisionerosFEMENINOS.txt");
			
			ObjectInputStream in3 = new ObjectInputStream(fileIn);
			
			ArrayList<Integer> tabla3 = (ArrayList<Integer>) in3.readObject();
			
			Prisionero.prisionerosFEMENINOS = tabla3;
			
			in3.close();
			fileIn.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void deserializarGuardianes() {
		try {
			fileIn = new FileInputStream(rutaTemp + "\\guardianes.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			Hashtable<Integer, Guardian> hashtable = (Hashtable<Integer, Guardian>) in.readObject();
			
			Guardian.setGuardianes(hashtable);
			
			in.close();
			fileIn.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void deserializarDelitos() {
		try {
			fileIn = new FileInputStream(rutaTemp + "\\delitos.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			Hashtable<Integer, Delito> hashtable = (Hashtable<Integer, Delito>) in.readObject();
			
			Delito.setDelitos(hashtable);
			
			in.close();
			fileIn.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void deserializarAntidelitos() {
		try {
			fileIn = new FileInputStream(rutaTemp + "\\antidelitos.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			Hashtable<Integer, Antidelito> hashtable = (Hashtable<Integer, Antidelito>) in.readObject();
			
			Antidelito.setAntidelitos(hashtable);
			
			in.close();
			fileIn.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void deserializarCeldas() {
		try {
			fileIn = new FileInputStream(rutaTemp + "\\celdas.txt");
			
			ObjectInputStream in = new ObjectInputStream(fileIn);
			
			Hashtable<Integer, Celda> hashtable = (Hashtable<Integer, Celda>) in.readObject();
			
			Celda.setCeldas(hashtable);
			
			in.close();
			fileIn.close();
			
			fileIn = new FileInputStream(rutaTemp + "\\celdasMASCULINAS.txt");
			
			ObjectInputStream in2 = new ObjectInputStream(fileIn);
			
			ArrayList<Integer> tabla2 = (ArrayList<Integer>) in2.readObject();
			
			Celda.setCeldasMASCULINAS(tabla2);
			
			in2.close();
			fileIn.close();
			
			
			fileIn = new FileInputStream(rutaTemp + "\\celdasFEMENINAS.txt");
			
			ObjectInputStream in3 = new ObjectInputStream(fileIn);
			
			ArrayList<Integer> tabla3 = (ArrayList<Integer>) in3.readObject();
			
			Celda.setCeldasFEMENINAS(tabla3);
			
			in3.close();
			fileIn.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
