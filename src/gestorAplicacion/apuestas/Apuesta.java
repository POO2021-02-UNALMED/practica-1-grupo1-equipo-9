package gestorAplicacion.apuestas;
import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.carcel.Prisionero;

public class Apuesta {
	private static Hashtable<Integer,Apuesta> apuestas= new Hashtable<Integer,Apuesta>();
	private int codigo; //Cada pelea tiene el mismo código que su respectiva apuesta
    private ArrayList<Object[]> apostadores= new ArrayList<Object[]>(); 
    private Pelea pelea;
    
    public Apuesta(int codigo, Pelea pelea) {
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
    	double totalGanadores = 0;
//    	Primero necesito saber cuánto se recogió en total y cuanto se recogió entre los ganadores
    	for (Object[] objects : apostadores) {
    		Prisionero prisionero = (Prisionero) objects[1];
    		double apuesta = (Integer) objects[2];
    		montoTotal += apuesta;
    		if (pelea.getGanador().equals(prisionero)) {totalGanadores += apuesta;}
		}
    	
//    	Se paga a los apostadores ganadores proporcionalmente al dinero que apostaron.
    	for (Object[] objects : apostadores) {
//    		Casteo explícito de un objeto Object a Apostador, Prisionero e Int.
    		Apostador apostador = (Apostador) objects[0];
    		Prisionero prisionero = (Prisionero) objects[1];
    		double apuesta = (Integer) objects[2];
    		
    		if (pelea.getGanador().equals(prisionero)) {
    			double k = apuesta/totalGanadores;
    			apostador.aumentarSaldo(k*montoTotal);
    			
    		}
		}
    	
    	System.out.println(montoTotal);
    }
    
    public void agregarApostador(Apostador apostador, Prisionero prisionero, Integer apuesta) {
		/*
		 * apostador es el Apostador que ingresa a this Apuesta 
		 * prisionero es el luchador por el que apostador va a apostar 
		 * apuesta es la cantidad que se va a apostar
		 */
    	
//    	Revisa si el apostador tiene saldo suficiente para apostar.
    	if (apuesta > apostador.getSaldo()) {return;}
    	
    	apostador.reducirSaldo(apuesta);
    	Object[] agregando = {apostador, prisionero, apuesta};
    	apostadores.add(agregando);
    }

	public int getCodigo() {return codigo;}
	public void setCodigo(int codigo) {	this.codigo = codigo;}

	public Pelea getPelea() {return pelea;}
	public void setPelea(Pelea pelea) {	this.pelea = pelea;}

	public ArrayList<Object[]> getApostadores() {return apostadores;}
    
    
}
