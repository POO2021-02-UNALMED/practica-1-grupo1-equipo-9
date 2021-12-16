/*
 * La clase Antidelito representa las posibles acciones o trabajos que prisionero puede realizar para
 * disminuir su tiempo de condena. Se relaciona directamente con la clase Prisionero.
 * 
 * Posee los siguientes atributos:
 * - codigo (int): Permite la identificacion del Antidelito por medio de un entero.
 * - nombre (String): Permite la identificacion del Antidelito por medio de un String.
 * - descripcion (String): Contiene la descripcion de la accion o trabajo que el Prisionero puede realizar.
 * - antidelitos (Hashtable<Integer,Antidelito>): Permite llevar un registro de los Antidelitos creados, donde
 *   la clave de la Hashtable es el codigo del Antidelito y Antidelito es this.Antidelito.
 * - rebajaCondena (long): Representa el tiempo en meses que disminuye el Antidelito al tiempo de condena del 
 *   Prisionero que la realiza.
 */

package gestorAplicacion.carcel;
import java.io.Serializable;
import java.util.Hashtable;

public class Antidelito implements Serializable{
   
	private static final long serialVersionUID = 1L;
	
	private static Hashtable<Integer,Antidelito> antidelitos= new Hashtable<Integer,Antidelito>();
	private int codigo;
    private String nombre;
    private String descripcion;
    private long rebajaCondena; /*meses*/
    
    /*
     * Cuando se crea un Antidelito, se agrega a una lista general de antidelitos.
     */
    public Antidelito(int codigo, String nombre, String descripcion, long rebajaCondena) {
    	this.codigo = codigo;
    	this.nombre = nombre;
    	this.descripcion = descripcion;
    	this.rebajaCondena = rebajaCondena;
    	antidelitos.put(this.codigo, this);
    }

	public static Hashtable<Integer, Antidelito> getAntidelitos() {return antidelitos;}
	public static void setAntidelitos(Hashtable<Integer, Antidelito> antidelitos) {Antidelito.antidelitos = antidelitos;}
	
	public int getCodigo() {return codigo;}
	public void setCodigo(int codigo) {this.codigo = codigo;}

	public String getNombre() {return nombre;}
	public void setNombre(String nombre) {this.nombre = nombre;}

	public long getRebajaCondena() {return rebajaCondena;}
	public void setRebajaCondena(long rebajaCondena) {this.rebajaCondena = rebajaCondena;}
    
	@Override
	public String toString() {
		
		return "Codigo: " + this.getCodigo() + "\n" 
				+ "Nombre: " + this.getNombre() + "\n"
				+ "Rebaja condena: " + this.getRebajaCondena() + " meses" + "\n" + "\n";
	}

	public String getDescripcion() {return descripcion;}
	public void setDescripcion(String descripcion) {this.descripcion = descripcion;}
}
