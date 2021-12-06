package gestorAplicacion.carcel;

import java.util.Hashtable;

public class Delito {
	private static Hashtable<Integer,Delito> delitos= new Hashtable<Integer,Delito>();
    private int codigo;
    private String categoria;
    private String nivel;
    private long tiempoCondena; /*meses*/
}
