package gestorAplicacion.carcel;
import java.util.Hashtable;
import java.time.LocalDate;

public class Prisionero {
    private gestorAplicacion.carcel.genero genero;
    private Celda celda;
    private LocalDate inicioCondena;
    private LocalDate finCondena;
    private Hashtable<Integer, Delito> delitos; 
    private Hashtable<Integer, Antidelito> antidelitos;
    
    private static Hashtable<Integer, Celda> celdas;
    
    public void agregarDelito(Delito delito) {
    	
    }
    public void agregarAntidelito(Antidelito antidelito) {
    	
    }
    private void incrementarCondena(Long meses) { //reciben como argumento el tiempoCondena de Delito
    	// usar el método LocalDate.plusMonths() y devuelve una copia
    }
    private void dismnuirCondena(Long meses) { //reciben como argumento el rebajarCondena de Antidelito
    	
    }  
}
