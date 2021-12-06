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
    private Hashtable<Integer, Antidelito> antidelitos;
    
    private static Hashtable<Integer, Prisionero> prisioneros;
    
    public Prisionero(int identificacion, String nombre, gestorAplicacion.carcel.genero genero, Celda celda, Hashtable<Integer, Delito> delitos) {
    	this(identificacion,nombre,0, genero, celda, delitos);
    }
    
    public Prisionero(int identificacion, String nombre, int saldo, gestorAplicacion.carcel.genero genero, Celda celda,
			Hashtable<Integer, Delito> delitos) {
		super(identificacion, nombre, saldo);
		this.genero = genero;
		this.celda = celda; celda.getPrisioneros().put(this.identificacion, this);
		this.delitos = delitos;
		// TODO calcular inicioCondena y finCondena
	}

	public void agregarDelito(Delito delito) {
    	
    }
    
    public void agregarAntidelito(Antidelito antidelito) {
    	
    }
    
    private void incrementarCondena(Long meses) { //reciben como argumento el tiempoCondena de Delito
    	// usar el m�todo LocalDate.plusMonths() y devuelve una copia
    }
    
    private void dismnuirCondena(Long meses) { //reciben como argumento el rebajarCondena de Antidelito
    	
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
