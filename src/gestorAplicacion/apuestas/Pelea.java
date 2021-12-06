package gestorAplicacion.apuestas;
import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Prisionero;

public class Pelea {
    private int codigo;
    private gestorAplicacion.carcel.genero genero;
    private Prisionero luchador1;
    private Prisionero luchador2;
    private String armaLuchador1;
    private String armaLuchador2;
    private Prisionero ganador;
    private Apuesta apuesta;
    
    private static Hashtable<Integer, Pelea> peleas;
    
    public
    void setGanador(Prisionero prisionero) {
//    	TODO llama al método apuesta.resolverApuesta
    }
    
    public
    void setLuchadores(Prisionero luch1, Prisionero luch2) {
//    	TODO
    }
    
    public 
    Object battleRoyale(ArrayList<Celda> celdas){
		/*
		 * Devuelve un arraylist de strings, donde cada string es un comentario tipo
		 * "prisionero 1 a derrotado a prisionero 2", etc también debe devolver el
		 * prisionero ganador
		 */
//		TODO
    	ArrayList<String> combates = new ArrayList<String>();
    	Prisionero ganador = null;
    	Object[] resultado = {ganador, combates};
    	return resultado;
    }
}
