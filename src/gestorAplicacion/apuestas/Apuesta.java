package gestorAplicacion.apuestas;
import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.carcel.Prisionero;

public class Apuesta {
	private static Hashtable<Integer,Apuesta> apuestas= new Hashtable<Integer,Apuesta>();
	private int codigo; //Cada pelea tiene el mismo código que su respectiva apuesta
    private ArrayList<Object[]> apostadores= new ArrayList<Object[]>(); 
    private Pelea pelea;
    
    Apuesta(int codigo, Pelea pelea) {
//    	Las apuestas se crean automatica cuando se crea una pelea
		this.codigo = codigo;
		this.pelea = pelea;
		/*
		 * Si el arreglo apostadores está vacío, es porque nadie apostó en esta pelea
		 */
		apuestas.put(codigo, this);
	}

	public String resultadoApuesta() {
    	/*
    	 * Retorna una lista de los apostadores que participaron en una apuesta en 
    	 * particular, y el dinero que ganaron o perdieron
    	 */
    	return null;
    }
    
    public void resolverApuesta() {
    	if (apostadores.isEmpty()) {return;}
    	
    	double montoTotal = 0;
    	for (Object[] objects : apostadores) {
    		double apuesta = (Integer) objects[2];
    		montoTotal += apuesta;
		}
    	
    	
    }
    
    public void agregarApostador(Apostador apostador, Prisionero prisionero, Integer apuesta) {
		/*
		 * apostador es el Apostador que ingresa a this Apuesta 
		 * prisionero es el luchador por el que apostador va a apostar 
		 * apuesta es la cantidad que se va a apostar
		 */
    	Object[] agregando = {apostador, prisionero, apuesta};
    	apostadores.add(agregando);
    }

	public int getCodigo() {return codigo;}
	public void setCodigo(int codigo) {	this.codigo = codigo;}

	public Pelea getPelea() {return pelea;}
	public void setPelea(Pelea pelea) {	this.pelea = pelea;}

	public ArrayList<Object[]> getApostadores() {return apostadores;}
    
    
}
