package gestorAplicacion.carcel;
import java.util.Hashtable;

public class Antidelito {
    private static Hashtable<Integer,Antidelito> antidelitos= new Hashtable<Integer,Antidelito>();
	private int codigo;
    private String nombre;
    private long rebajaCondena; /*meses*/
}
