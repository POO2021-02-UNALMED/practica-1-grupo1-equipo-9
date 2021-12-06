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
    
}
