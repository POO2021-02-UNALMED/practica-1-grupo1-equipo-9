package gestorAplicacion.carcel;
import java.util.Hashtable;

public class Celda {
	private int numero;
    private gestorAplicacion.carcel.genero genero;
    private int largo;
    private int ancho;
    private int capMax;
    private String tipo;
    private Hashtable<Integer, Prisionero> prisioneros;
    
    private static Hashtable<Integer, Celda> celdas;
    
    public void extraerPrisionero(Prisionero prisionero) {
    	
    }
    public void ingresarPrisionero(Prisionero prisionero) {
    	
    }
}
