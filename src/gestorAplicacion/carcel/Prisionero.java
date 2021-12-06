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
    
    private static Hashtable<Integer, Celda> celdas;
    
    public Prisionero(int identificacion, String nombre, Celda celda, Hashtable<Integer, Delito> delitos) {
    	this(identificacion,nombre,0,celda,delitos);
    }
    
    public Prisionero(int identificacion, String nombre, int saldo, Celda celda, Hashtable<Integer, Delito> delitos) {
    	super(identificacion, nombre, saldo);
    	this.celda = celda;
    	this.delitos = delitos;
    	// calcular inicioCondena y finCondena
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
}
