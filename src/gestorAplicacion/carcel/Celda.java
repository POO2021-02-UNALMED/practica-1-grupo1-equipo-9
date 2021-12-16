/*
 * La clase Celda representa la unidad de espacio en donde se encierra a varios Prisioneros.
 * Esta clase se relaciona con las clases Guardian y Prisionero.
 * 
 * Posee los siguientes atributos:
 * - numero (int): Identificacion unica de la celda con un entero.
 * - genero (genero): Representa si los prisioneros que se encuentran en ella son hombre o mujeres.
 * - largo (double): Dimension largo de la Celda.
 * - ancho (double): Dimension ancho de la Celda.
 * - capMax (int): Representa el numero maximo de prisioneros que puede albergar la Celda.
 * - Prisioneros (Hashtable<Integer, Prisionero>): Permite llevar un registro de los Prisioneros que 
 *   se encuentran en la Celda, donde la clave de la Hashtable es la identificacion del Prisionero 
 *   y su valor es el Prisionero con dicha identificacion.
 */

package gestorAplicacion.carcel;
import java.io.Serializable;
import java.util.Enumeration;
import java.util.Hashtable;

public class Celda implements Serializable{

	private static final long serialVersionUID = 1L;
	
	private int numero;
    private gestorAplicacion.carcel.genero genero;
    private final double largo;
    private final double ancho;
    private final int capMax;
    private Hashtable<Integer, Prisionero> prisioneros = new Hashtable<Integer, Prisionero>();
    
    private static Hashtable<Integer, Celda> celdas = new Hashtable<>();
    
    /*
     * Cada vez que se crea un objeto Celda, se agrega a una lista general de Celdas creadas.
     * Al inicio del programa, todas las celdas disponibles ya se encontraran creadas, no se 
     * podra crear nuevas celdas.
     */
    public Celda(int numero, gestorAplicacion.carcel.genero genero, double largo, double ancho,int capMax) {
    	this.numero=numero;
    	this.genero=genero;
    	this.largo=largo;
    	this.ancho=ancho;
    	this.capMax=capMax;
    	
    	celdas.put(numero, this);
    }
    
    /*
     * Extrae de la lista de prisioneros que posee la Celda a un Prisionero.
     */
    public void extraerPrisionero(Prisionero prisionero) {
    	prisionero.setCelda(null);
    	prisioneros.remove(prisionero.getIdentificacion());
    }
    
    /*
     * Ingresa un Prisionero a la lista de prisioneros que posee la Celda.
     */
    public void ingresarPrisionero(Prisionero prisionero) {
    	prisionero.setCelda(this);
    	prisioneros.put(prisionero.getIdentificacion(), prisionero);
    }
    
	public Hashtable<Integer, Prisionero> getPrisioneros() {return prisioneros;}
	public static Hashtable<Integer, Celda> getCeldas() {return celdas;}

	public int getNumero() {return numero;}
	public void setNumero(int numero) {this.numero = numero;}

	public gestorAplicacion.carcel.genero getGenero() {return genero;}

	public double getLargo() {return largo;}

	public double getAncho() {return ancho;}

	public int getCapMax() {return capMax;}
	
	public static void setCeldas(Hashtable<Integer, Celda> celdas) {
		Celda.celdas = celdas;
	}

	@Override
	public String toString() {
		String claves = "";
		Enumeration<Integer> keys = prisioneros.keys();
		while (keys.hasMoreElements()) {
			claves += keys.nextElement() + " ";
		}
		
		return "Numero: " + this.getNumero() + "\n" 
				+ "Genero: " + this.getGenero() + "\n"
				+ "Medidas: " + this.getLargo() + "x" + this.getAncho() + "\n"
				+ "Capacidad maxima: " + this.getCapMax() + "\n"
				+ "Prisioneros: " + claves + "\n" + "\n";
	}

	
	
	
}
