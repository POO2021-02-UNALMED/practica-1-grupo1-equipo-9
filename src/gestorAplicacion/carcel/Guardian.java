/*
 * La clase Guardian representa a los guardianes o celadores que una carcel posee.
 * A cada guardian se le asigna una o varias celdas de la cual esta encargado de cuidar.
 * Se hereda de la clase Apostador, es decir todo Guardian es un Apostador.
 * Esta clase se relaciona con la clase Celda e indirectamente con la clase Apuesta.
 * 
 * Posee los siguientes atributos:
 * - salario (int): Representa el salario que gana un Guardian mensualmente.
 * - celdas (Hashtable<Integer, Guardian>): Permite almacenar las celdas de las cuales un Guardian esta 
 *   encargado de cuidar. Este almacenamiento se hace en una HashTable donde cada clave es el numero de 
 *   la Celda y su respectivo valor es la Celda con mismo codigo. 
 * - traslados (ArrayList<Object[3]>): Cumple la funcion de almacenar los traslados que un Guardian
 *   ha realizado de un Prisionero de una celda a otra. La informacion se guarda en una lista de listas, donde
 *   cada lista interna esta conformada de la Celda de origen, el segundo el Prisionero trasladado y 
 *   la Celda destino.
 * - guardianes (Hashtable<Integer, Guardian>): Permite llevar un registro de los Guardianes creados, donde
 *   la clave de la Hashtable es la identificacion del Guardian y su valor es el Guardian con dicho codigo.
 */

package gestorAplicacion.carcel;

import java.util.ArrayList;
import java.util.Enumeration;
import java.util.Hashtable;

import gestorAplicacion.apuestas.Apostador;

public class Guardian extends Apostador{
   
	private static final long serialVersionUID = 1L;
	
	private int salario;
    private ArrayList<Object[]> traslados = new ArrayList<>();
    private Hashtable<Integer, Celda> celdas = new Hashtable<>();
    
    private static Hashtable<Integer, Guardian> guardianes = new Hashtable<>();
    
    /*
     * Constructor usado para guardianes que aun no se les asignan celdas para cuidar.
     */
    public Guardian(int identificacion, String nombre, int saldo, int salario) {
		super(identificacion, nombre, saldo);
		this.setSalario(salario);
		
		guardianes.put(identificacion, this);
	}
    
    /*
     * Cada vez que se crea un objeto Guardian, se agrega a una lista general de guardianes creados.
     */
	public Guardian(int identificacion, String nombre, int saldo, int salario, Hashtable<Integer, Celda> celdas) {
		super(identificacion, nombre, saldo);
		this.setSalario(salario);
		this.celdas = celdas;
		
		guardianes.put(identificacion, this);
	}

	/*
	 * Recibe como parametros el prisionero a trasladar y la celdad donde va a ser trasladado,
	 * se debe eliminar el prisionero de la lista de la celda original y agregarlo a la nueva
	 * celda. 
	 * Se agregan los traslados en la lista de traslados de los guardianes.
	 * Utiliza el metodo agregarTraslado y le pasa un Object[3] donde el primer
	 * elemento es la Celda de origen, el segundo elemento es el prisionero
	 * trasladado y la tercera es la celda destino. 
	 */
    public void trasladarPrisionero(Prisionero prisionero, Celda celda) {    	
		Celda celdaOrigen = prisionero.getCelda();
    	celdaOrigen.extraerPrisionero(prisionero);
		celda.ingresarPrisionero(prisionero);
		
		Object[] traslado = {celdaOrigen, prisionero, celda};
		
		this.agregarTraslado(traslado);
    }
    
    public ArrayList<Object[]> getTraslados() {return traslados;}
    
    /*
     * Agrega la informacion del traslado a los 'traslados'(atributo) que ha hecho this Apostador.
     */
    private void agregarTraslado(Object[] objetos) { 
    	traslados.add(objetos);
    }

	@Override
	public String toString() {
		String claves = "";
		Enumeration<Integer> keys = celdas.keys();
		while (keys.hasMoreElements()) {
			claves += keys.nextElement() + " ";
		}
		
		return "GUARDIAN: " + getIdentificacion() + "\n" 
				+ "Nombre: " + getNombre() + "\n"
				+ "Saldo: " + getSaldo() + "\n"
				+ "Salario: " + getSalario() + "\n"
				+ "Celdas a Cargo: " + claves + "\n" + "\n";
	}
	
	public Hashtable<Integer, Celda> getCeldas() {return celdas;}
	
	/*
	 * Recibe como parametro una Celda.
	 * Agrega a la lista general de celdas de la cual esta encargado un Guardian una nueva celda. 
	 */
	public void agregarCelda(Celda celda) {
		celdas.put(celda.getNumero(), celda);
	}

	public int getSalario() {return salario;}
	public void setSalario(int salario) {this.salario = salario;}
	
	public static Hashtable<Integer, Guardian> getGuardianes() {return guardianes;}
	public static void setGuardianes(Hashtable<Integer, Guardian> guardianes) {Guardian.guardianes = guardianes;}
}
