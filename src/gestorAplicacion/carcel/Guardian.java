package gestorAplicacion.carcel;

import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.apuestas.Apostador;

public class Guardian extends Apostador{
    private int salario;
    private ArrayList<Object[]> traslados = new ArrayList<>();
    private Hashtable<Integer, Celda> celdas = new Hashtable<>();
    
    private static Hashtable<Integer, Guardian> guardianes = new Hashtable<>();
    
    public
    void trasladarPrisionero(Prisionero prisionero, Celda celda) {
		/*
		 * Utiliza el método agregarTraslado y le pasa un Object[3] donde
		 * el primero elemento es la Celda de origen, el segundo es el prisionero
		 * trasladado y la tercera es la celda destino
		 */
    }
    
    private
    void agregarTraslado(Object[] objetos) {
//    	agrega la información del traslado al los 'traslados'(atributo) que ha hecho this Apostador 
    }

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return null;
	}
}
