package baseDatos;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;
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
