package gestorAplicacion.carcel;
import java.io.Serializable;
import java.util.Enumeration;
import java.util.Hashtable;

public class Celda implements Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private int numero;
    private gestorAplicacion.carcel.genero genero;
    private final double largo;
    private final double ancho;
    private final int capMax;
    private Hashtable<Integer, Prisionero> prisioneros = new Hashtable<Integer, Prisionero>();
    
    private static Hashtable<Integer, Celda> celdas = new Hashtable<>();
    
    public Celda(int numero, gestorAplicacion.carcel.genero genero, double largo, double ancho,int capMax) {
    	this.numero=numero;
    	this.genero=genero;
    	this.largo=largo;
    	this.ancho=ancho;
    	this.capMax=capMax;
    	
    	celdas.put(numero, this);

    }
    
    public void extraerPrisionero(Prisionero prisionero) {
//    	Hace prisionero.celda = null y prisionero.celda.remove(prisionero)
    	prisionero.setCelda(null);
    	prisioneros.remove(prisionero.getIdentificacion());
    }
    
    public void ingresarPrisionero(Prisionero prisionero) {
//    	Hace prisionero.celda = this y this.add(prisionero)
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
