package gestorAplicacion.carcel;
import java.util.Hashtable;
import java.time.LocalDate;

import gestorAplicacion.apuestas.Apostador;

public class Prisionero extends Apostador{
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
		this.finCondena = 0;
		this.celda = celda; celda.ingresarPrisionero(this);
		this.delitos = delitos;
		
		prisioneros.put(this.identificacion, this);
		// TODO calcular inicioCondena y finCondena
	}

	public void agregarDelito(Delito delito) {
		delitos.put(delito.getCodigo(), delito);
		incrementarCondena(delitos);
    }
    
    public void agregarAntidelito(Antidelito antidelito) {
    	antidelitos.put(this.identificacion, antidelito);
    	disminuirCondena(antidelitos);
    }
	//se cambio long meses por la hashtable
    
    private void incrementarCondena(Hashtable<Integer, Delito> delitos) { //reciben como argumento el tiempoCondena de Delito
    	// usar el metodo LocalDate.plusMonths() y devuelve una copia
    	int meses=0;
    	for(Integer k: delitos.keySet()) {
    		meses+=delitos.get(k).getTiempoCondena();
    	}
    	finCondena = inicioCondena.plusMonths(meses);
    }
    
    private void disminuirCondena(Hashtable<Integer, Antidelito> antidelitos) { //reciben como argumento el rebajarCondena de Antidelito
    	int meses=0;
    	for(Integer k: antidelitos.keySet()) {
    		meses+=antidelitos.get(k).getRebajaCondena();
    	}
    	finCondena= inicioCondena.minusMonths(meses);
    
    }
    
    @Override
	public String toString() {
		// TODO Auto-generated method stub
		return null;
	}

	public gestorAplicacion.carcel.genero getGenero() {	return genero;	}
	public void setGenero(gestorAplicacion.carcel.genero genero) {this.genero = genero;}

	public Celda getCelda() {return celda;}
	public void setCelda(Celda celda) {	this.celda = celda;	}

	public LocalDate getInicioCondena() {return inicioCondena;}

	public LocalDate getFinCondena() {return finCondena;}

	public void setFinCondena(LocalDate finCondena) {	this.finCondena = finCondena;	}

	public Hashtable<Integer, Delito> getDelitos() {	return delitos; }

	public Hashtable<Integer, Antidelito> getAntidelitos() {	return antidelitos;	}

	public static Hashtable<Integer, Prisionero> getPrisioneros() {	return prisioneros;	}
    
    
}
