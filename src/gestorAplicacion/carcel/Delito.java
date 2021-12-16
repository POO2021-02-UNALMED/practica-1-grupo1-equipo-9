/*
 * La clase Delito representa cada delito por el cual se enjuicia a un Prisionero.
 * Se relaciona directamente con la clase Prisionero.
 * 
 * Posee los siguientes atributos:
 * - codigo (int): Permite la identificacion del Delito por medio de un entero.
 * - nombre (String): Permite la identificacion del Delito por medio de un String.
 * - descripcion (String): Contiene la descripcion del delito por el cual Prisionero es juzgado.
 * - delitos (Hashtable<Integer,Delito>): Permite llevar un registro de los Delitos creados, donde
 *   la clave de la Hashtable es el codigo del Delito y su valor es el Delito con dicho codigo.
 * - nivel (int): Representa el nivel de gravedad del Delito.
 * - tiempoCondena (long): Representa el tiempo en meses que el Prisionero debe pasar en la carcel para cumplir
 *   su condena. 
 */

package gestorAplicacion.carcel;
import java.io.Serializable;
import java.util.Hashtable;

public class Delito implements Serializable{
	
	private static final long serialVersionUID = 1L;
	
	private static Hashtable<Integer,Delito> delitos= new Hashtable<Integer,Delito>();
    private int codigo;
    private String nombre;
    private String descripcion;
    private int nivel;
    private long tiempoCondena; /*meses*/
    
    /*
     * Cada vez que se crea un Delito, se agrega a una lista general de Delitos.
     */
    public Delito(int codigo, String nombre, String descripcion, int nivel, long tiempoCondena) {
    	this.codigo = codigo;
    	this.nombre = nombre;
    	this.descripcion = descripcion;
    	this.nivel = nivel;
    	this.tiempoCondena = tiempoCondena;
    	delitos.put(this.codigo, this);
    }
	
    public int getCodigo() {return codigo;}
    public void setCodigo(int codigo) {this.codigo=codigo;}
    
	public String getNombre() {return nombre;}
	public void setNombre(String nombre) {this.nombre = nombre;}

	public String getDescripcion() {return descripcion;}
	public void setDescripcion(String descripcion) {this.descripcion = descripcion;}

	public int getNivel() {return nivel;}
	public void setNivel(int nivel) {this.nivel = nivel;}

	public long getTiempoCondena() {return tiempoCondena;}
	public void setTiempoCondena(long tiempoCondena) {this.tiempoCondena = tiempoCondena;}
	
	public static Hashtable<Integer, Delito> getDelitos() {return delitos;}
	public static void setDelitos(Hashtable<Integer, Delito> delitos) {Delito.delitos = delitos;}
	
	@Override
	public String toString() {
		
		return "Codigo: " + this.getCodigo() + "\n" 
				+ "Nombre: " + this.getNombre() + "\n"
				+ "Descripcion: " + this.getDescripcion() + "\n"
				+ "Nivel: " + this.getNivel() + "\n"
				+ "Aumento condena: " + this.getTiempoCondena() + " meses" + "\n" + "\n";
	}
}
