package baseDatos;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import gestorAplicacion.apuestas.Apuesta;
import gestorAplicacion.apuestas.Pelea;
import gestorAplicacion.carcel.Antidelito;
import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Delito;
import gestorAplicacion.carcel.Guardian;
import gestorAplicacion.carcel.Prisionero;

public class Serializador {
	private static String rutaTemp = System.getProperty("user.dir") + "\\src\\baseDatos\\temp";
	private static FileOutputStream fileOut;

	public static void serializar() {
		serializarAntidelitos();
		serializarPeleas();
		serializarApuestas();
		serializarPrisioneros();
		serializarGuardianes();
		serializarDelitos();
		serializarCeldas();
		/* 
		 * Por la forma en que se diseño el programa, cada que se crea un objeto este se agrega
		 * a la Hashtable de esa clase, entonces no se serializa cada objeto individualmente 
		 * sino que se guardan en una Hashtable todos los objetos que fueron creados y se serializa
		 * esta Hashtable.
		 */
	}

	private static 
	void serializarApuestas() {
		try {
			fileOut = new FileOutputStream(rutaTemp + "\\apuestas.txt");
			
			ObjectOutputStream out = new ObjectOutputStream(fileOut);
			
			out.writeObject(Apuesta.getApuestas());
			out.close();
			fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void serializarPeleas() {
		try {
		fileOut = new FileOutputStream(rutaTemp + "\\peleas.txt");
		
		ObjectOutputStream out = new ObjectOutputStream(fileOut);
		
		out.writeObject(Pelea.getPeleas());
		out.close();
		fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void serializarPrisioneros() {
		try {
		fileOut = new FileOutputStream(rutaTemp + "\\prisioneros.txt");
		
		ObjectOutputStream out = new ObjectOutputStream(fileOut);
		
		out.writeObject(Prisionero.getPrisioneros());
		out.close();
		fileOut.close();
		
		fileOut = new FileOutputStream(rutaTemp + "\\prisionerosMASCULINOS.txt");
		
		ObjectOutputStream out2 = new ObjectOutputStream(fileOut);
		
		out2.writeObject(Prisionero.prisionerosMASCULINOS);
		out2.close();
		fileOut.close();
		
		fileOut = new FileOutputStream(rutaTemp + "\\prisionerosFEMENINOS.txt");
		
		ObjectOutputStream out3 = new ObjectOutputStream(fileOut);
		
		out3.writeObject(Prisionero.prisionerosFEMENINOS);
		out3.close();
		fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void serializarGuardianes() {
		try {
		fileOut = new FileOutputStream(rutaTemp + "\\guardianes.txt");
		
		ObjectOutputStream out = new ObjectOutputStream(fileOut);
		
		out.writeObject(Guardian.getGuardianes());
		out.close();
		fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void serializarDelitos() {
		try {
		fileOut = new FileOutputStream(rutaTemp + "\\delitos.txt");
		
		ObjectOutputStream out = new ObjectOutputStream(fileOut);
		
		out.writeObject(Delito.getDelitos());
		out.close();
		fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void serializarAntidelitos() {
		try {
		fileOut = new FileOutputStream(rutaTemp + "\\antidelitos.txt");
		
		ObjectOutputStream out = new ObjectOutputStream(fileOut);
		
		out.writeObject(Antidelito.getAntidelitos());
		out.close();
		fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private static 
	void serializarCeldas() {
		try {
		fileOut = new FileOutputStream(rutaTemp + "\\celdas.txt");
		
		ObjectOutputStream out = new ObjectOutputStream(fileOut);
		
		out.writeObject(Celda.getCeldas());
		out.close();
		fileOut.close();
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
