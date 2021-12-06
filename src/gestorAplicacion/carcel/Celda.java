package gestorAplicacion.carcel;
import java.util.Hashtable;

public class Celda {
	private int numero;
    private gestorAplicacion.carcel.genero genero;
    private final int largo;
    private final int ancho;
    private final int capMax;
    private Hashtable<Integer, Prisionero> prisioneros;
    
    private static Hashtable<Integer, Celda> celdas;
    
    public Celda(int numero, gestorAplicacion.carcel.genero genero, int largo, int ancho,int capMax) {
    	this.numero=numero;
    	this.genero=genero;
    	this.largo=largo;
    	this.ancho=ancho;
    	this.capMax=capMax;

    }
    
    public void extraerPrisionero(Prisionero prisionero) {
//    	Hace prisionero.celda = null y prisionero.celda.remove(prisionero)
    }
    public void ingresarPrisionero(Prisionero prisionero) {
//    	Hace prisionero.celda = this y this.add(prisionero)
    }
	public Hashtable<Integer, Prisionero> getPrisioneros() {return prisioneros;}
	public static Hashtable<Integer, Celda> getCeldas() {return celdas;}

	public int getNumero() {return numero;}
	public void setNumero(int numero) {this.numero = numero;}

	public gestorAplicacion.carcel.genero getGenero() {return genero;}

	public int getLargo() {return largo;}

	public int getAncho() {return ancho;}

	public int getCapMax() {return capMax;}


	
	
	
}
