package gestorAplicacion.carcel;
import java.io.Serializable;
import java.util.Hashtable;

public class Antidelito implements Serializable{
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private static Hashtable<Integer,Antidelito> antidelitos= new Hashtable<Integer,Antidelito>();
	private int codigo;
    private String nombre;
    private String descripcion;
    private long rebajaCondena; /*meses*/
    
    public Antidelito(int codigo, String nombre, String descripcion, long rebajaCondena) {
    	this.codigo = codigo;
    	this.nombre = nombre;
    	this.descripcion = descripcion;
    	this.rebajaCondena = rebajaCondena;
    	antidelitos.put(this.codigo, this);
    }

	public static Hashtable<Integer, Antidelito> getAntidelitos() {return antidelitos;}

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
}
