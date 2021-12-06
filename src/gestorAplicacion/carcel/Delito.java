package gestorAplicacion.carcel;

import java.util.Hashtable;

public class Delito {
	private static Hashtable<Integer,Delito> delitos= new Hashtable<Integer,Delito>();
    private int codigo;
    private String nombre;
    private String descripcion;
    private int nivel;
    private long tiempoCondena; /*meses*/
    
    public Delito(int codigo, String nombre, String descripcion, int nivel, long tiempoCondena) {
    	this.codigo = codigo;
    	this.nombre = nombre;
    	this.descripcion = descripcion;
    	this.nivel = nivel;
    	this.tiempoCondena = tiempoCondena;
    	delitos.put(this.codigo, this);
    }
}
