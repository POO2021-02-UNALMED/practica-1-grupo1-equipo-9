/*
 * Autores: 
 * - Beatriz Valentina Gomez Valencia.
 * - Alejandro Salazar Mejia.
 * - Juan Pablo Martinez Echavarria.
 * 
 * La clase Prisionero cumple con la funcionalidad de representar a las personas que han sido
 * condenadas a pasar un tiempo en prision por delitos cometidos.
 * Cada Prisionero reside en una Celda de la prision.
 * Se hereda de la clase Apostador, es decir todo Prisionero es un Apostador.
 * Esta clase se relaciona con las clases Celda y Pelea e indirectamente con la clase Apuesta.
 * Todo Prisionero puede ser un Peleador.
 * 
 * Posee los siguientes atributos:
 * - genero (genero): Permite identificar si un Prisionero es hombre o mujer.
 * - celda (celda): Permite identificar en cual Celda se encuentra this.Prisionero.
 * - inicioCondena (LocalDate): Contiene la fecha en la cual el Prisionero se ingreso en la Prision.
 * - finCondena (LocalDate): Contiene la fecha en la que un Prisionero cumple su condena.
 * - delitos (Hashtable<Integer,Delito>): Permite almacenar en una Hashtable los delitos que un Prisionero
 *   ha cometido. Posee como clave el codigo del Delito y su respectivo valor es el Delito con dicho codigo.
 * - antidelitos (Hashtable<Integer,Antidelito>): Permite almacenar en una Hashtable los antidelitos que un 
 *   Prisionero ha realizado. Posee como clave el codigo del Antidelito y su respectivo valor es el Antidelito
 *   con dicho codigo.
 * - prisioneros (Hashtable<Integer,Prisionero>): Permite llevar un registro de los Prisioneros ingresados, donde
 *   la clave de la Hashtable es la identificacion del Prisionoero y su valor es el Prisionero con dicho codigo.
 */

package gestorAplicacion.carcel;
import java.util.Hashtable;
import java.time.LocalDate;

import gestorAplicacion.apuestas.Apostador;

public class Prisionero extends Apostador{
 
	private static final long serialVersionUID = 1L;
	
	private gestorAplicacion.carcel.genero genero;
    private Celda celda;
    private LocalDate inicioCondena;
    private LocalDate finCondena;
    private Hashtable<Integer, Delito> delitos; 
    private Hashtable<Integer, Antidelito> antidelitos = new Hashtable<>();
    
    private static Hashtable<Integer, Prisionero> prisioneros = new Hashtable<>();
   
    /*
     * Constructor usado si un Prisionero no posee saldo al momento de ser ingresado.
     */
    public Prisionero(int identificacion, String nombre, gestorAplicacion.carcel.genero genero, Celda celda, Hashtable<Integer, Delito> delitos) {
    	this(identificacion,nombre,0, genero, celda, delitos);
    }
    
    /*
     * Cada vez que se ingresa un nuevo prisionero a la prision, sus datos se almacenan en una lista 
     * general de prisioneros.
     * Tambien cumple la funcion de calcular el tiempo de condena segun los delitos que haya cometido.
     */
    public Prisionero(int identificacion, String nombre, int saldo, gestorAplicacion.carcel.genero genero, Celda celda, 
    		Hashtable<Integer, Delito> delitos) {
		super(identificacion, nombre, saldo);
		this.genero = genero;
		this.inicioCondena = LocalDate.now();
		this.celda = celda; celda.ingresarPrisionero(this);
		this.delitos = delitos;
		
		//Se suma el total de meses que el prisionero va a estar en la carcel y se agregan al inicio de su condena
		int meses=0;
    	for(Integer k: delitos.keySet()) {
    		meses+=delitos.get(k).getTiempoCondena();
    	}
    	
    	this.finCondena = this.inicioCondena;
    	incrementarCondena(meses);
		
		prisioneros.put(this.identificacion, this);
	}
    
    /*
     * Este metodo se utiliza cuando un prisionero ya esta en la carcel y se le quiere agregar otro delito.
     * Recibe como parametro un objeto de clase Delito, el cual se quiere agregar a la lista de delitos
     * que un prisionero posee.
     */
	public void agregarDelito(Delito delito) {
		delitos.put(delito.getCodigo(), delito);
		incrementarCondena(delito.getTiempoCondena());
    }
    
	/*
	 * Este metodo se utiliza cuando un prisionero ya esta en la carcel y se le quiere agregar un antidelito.
	 * Recibe como parametro un objeto de clase Antidelito.
	 */
    public void agregarAntidelito(Antidelito antidelito) {
    	antidelitos.put(antidelito.getCodigo(), antidelito);
    	disminuirCondena(antidelito.getRebajaCondena());
    }
    
    /*
     * Reciben como argumento el tiempoCondena de un Delito en particular y se incrementa al tiempo de condena
     * que un Prisionero debe cumplir.
     * Se usa el metodo plusMonths() y devuelve una copia.
     */
    private void incrementarCondena(long meses) {
    	finCondena = finCondena.plusMonths(meses);
    }
    
    /*
     * Reciben como argumento rebajaCondena de un Antidelito en particular y se disminuye al tiempo de condena
     * que un Prisionero debe cumplir.
     */
    private void disminuirCondena(long meses) { //reciben como argumento el rebajarCondena de Antidelito
    	finCondena= finCondena.minusMonths(meses);
    
    }
    
    /*
	 * Se imprimen los datos del prisionero con la lista de delitos y antidelitos de este.
	 */
    @Override
	public String toString() {
    	
    	String nombresDelitos = "";
		for(Integer k: delitos.keySet()) {
			nombresDelitos += delitos.get(k).getNombre() + " ";
		}
		
		String nombresAntidelitos = "";
		for(Integer k: antidelitos.keySet()) {
			nombresAntidelitos += antidelitos.get(k).getNombre() + " ";
		}
		
		return "PRISIONERO: " + getIdentificacion() + "\n" 
				+ "Nombre: " + getNombre() + "\n"
				+ "Genero: " + getGenero() + "\n"
				+ "Saldo: " + getSaldo() + "\n"
				+ "Celda: " + getCelda().getNumero() + "\n"
				+ "Inicio de Condena: " + getInicioCondena() + "\n"
				+ "Fin de Condena: " + getFinCondena() + "\n"
				+ "Delitos: " + nombresDelitos + "\n"
				+ "Antidelitos: " + (antidelitos == null ? "Aun no tiene Antidelitos registrados" : nombresAntidelitos) + "\n" + "\n";
	}

	public gestorAplicacion.carcel.genero getGenero() {	return genero;	}
	public void setGenero(gestorAplicacion.carcel.genero genero) {this.genero = genero;}

	public Celda getCelda() {return celda;}
	public void setCelda(Celda celda) {	this.celda = celda;	}

	public LocalDate getInicioCondena() {return inicioCondena;}
	public void setInicioCondena(LocalDate inicioCondena) {this.inicioCondena=inicioCondena;}

	public LocalDate getFinCondena() {return finCondena;}
	public void setFinCondena(LocalDate finCondena) {this.finCondena=finCondena;}

	public Hashtable<Integer, Delito> getDelitos() {	return delitos; }

	public Hashtable<Integer, Antidelito> getAntidelitos() {	return antidelitos;	}

	public static Hashtable<Integer, Prisionero> getPrisioneros() {	return prisioneros;	}
    public static void setPrisioneros(Hashtable<Integer, Prisionero> prisioneros) {Prisionero.prisioneros = prisioneros;}
    
}
