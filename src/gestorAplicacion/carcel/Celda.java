package gestorAplicacion.carcel;
import java.util.Hashtable;

public class Celda {
	private int numero;
    private gestorAplicacion.carcel.genero genero;
    private final int largo;
    private final int ancho;
    private final int capMax;
    private String tipo;
    private Hashtable<Integer, Prisionero> prisioneros;
    
    private static Hashtable<Integer, Celda> celdas;
    
    public Celda(int numero, gestorAplicacion.carcel.genero genero, int largo, int ancho,int capMax, String tipo) {
    	this.numero=numero;
    	this.genero=genero;
    	this.largo=largo;
    	this.ancho=ancho;
    	this.capMax=capMax;
    	this.tipo=tipo;
    	
    }
    
    public void extraerPrisionero(Prisionero prisionero) {
//    	Hace prisionero.celda = null y prisionero.celda.remove(prisionero)
    }
    public void ingresarPrisionero(Prisionero prisionero) {
//    	Hace prisionero.celda = this y this.add(prisionero)
    }
	public Hashtable<Integer, Prisionero> getPrisioneros() {
		return prisioneros;
	}
}
