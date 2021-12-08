package gestorAplicacion.carcel;

import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.apuestas.Apostador;

public class Guardian extends Apostador{
    private int salario;
    private ArrayList<Object[]> traslados = new ArrayList<>();
    private Hashtable<Integer, Celda> celdas = new Hashtable<>();
    
    private static Hashtable<Integer, Guardian> guardianes = new Hashtable<>();
        
    public Guardian(int identificacion, String nombre, int saldo, int salario) {
		super(identificacion, nombre, saldo);
		this.setSalario(salario);
	}
    
	public Guardian(int identificacion, String nombre, int saldo, int salario, Hashtable<Integer, Celda> celdas) {
		super(identificacion, nombre, saldo);
		this.setSalario(salario);
		this.celdas = celdas;
	}

    public void trasladarPrisionero(Prisionero prisionero, Celda celda) {
		Celda celdaOrigen = prisionero.getCelda(); 
    	prisionero.getCelda().extraerPrisionero(prisionero);
		celda.ingresarPrisionero(prisionero);
		
		Object[] traslado = {celdaOrigen, prisionero, celda};
		
		this.agregarTraslado(traslado);
		
    	/*
		 * Utiliza el m�todo agregarTraslado y le pasa un Object[3] donde
		 * el primero elemento es la Celda de origen, el segundo es el prisionero
		 * trasladado y la tercera es la celda destino
		 */
    }
    
    public ArrayList<Object[]> getTraslados() {return traslados;}
    private void agregarTraslado(Object[] objetos) {
    	traslados.add(objetos);
//    	agrega la informaci�n del traslado al los 'traslados'(atributo) que ha hecho this Apostador 
    }

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return null;
	}
	
	public Hashtable<Integer, Celda> getCeldas() {return celdas;}
	public void agregarCelda(Celda celda) {
		celdas.put(celda.getNumero(), celda);
	}

	public int getSalario() {return salario;}
	public void setSalario(int salario) {this.salario = salario;}
	
	public static Hashtable<Integer, Guardian> getGuardianes() {return guardianes;}
}
