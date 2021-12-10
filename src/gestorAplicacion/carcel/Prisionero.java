package gestorAplicacion.carcel;
import java.util.Hashtable;
import java.time.LocalDate;

import gestorAplicacion.apuestas.Apostador;

public class Prisionero extends Apostador{
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private gestorAplicacion.carcel.genero genero;
    private Celda celda;
    private LocalDate inicioCondena;
    private LocalDate finCondena;
    private Hashtable<Integer, Delito> delitos; 
    private Hashtable<Integer, Antidelito> antidelitos = new Hashtable<>();
    
    private static Hashtable<Integer, Prisionero> prisioneros = new Hashtable<>();
    //Se agrego inicio condena y fin condena
    
    public Prisionero(int identificacion, String nombre, gestorAplicacion.carcel.genero genero, Celda celda, Hashtable<Integer, Delito> delitos) {
    	this(identificacion,nombre,0, genero, celda, delitos);
    }
    
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
		// TODO calcular inicioCondena y finCondena
	}
    
	public void agregarDelito(Delito delito) {
		//Este metodo se utiliza cuando un prisionero ya esta en la carcel y se le quiere agregar otro delito
		delitos.put(delito.getCodigo(), delito);
		incrementarCondena(delito.getTiempoCondena());
    }
    
    public void agregarAntidelito(Antidelito antidelito) {
    	antidelitos.put(antidelito.getCodigo(), antidelito);
    	disminuirCondena(antidelito.getRebajaCondena());
    }
    
    private void incrementarCondena(long meses) { //reciben como argumento el tiempoCondena de Delito
    	// usar el metodo LocalDate.plusMonths() y devuelve una copia
    	finCondena = finCondena.plusMonths(meses);
    }
    
    private void disminuirCondena(long meses) { //reciben como argumento el rebajarCondena de Antidelito
    	
    	finCondena= finCondena.minusMonths(meses);
    
    }
    
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
				+ "Antidelitos: " + nombresAntidelitos + "\n" + "\n";
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
    
    
}
