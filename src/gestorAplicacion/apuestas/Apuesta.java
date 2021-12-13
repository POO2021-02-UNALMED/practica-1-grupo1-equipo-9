package gestorAplicacion.apuestas;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.carcel.Prisionero;

public class Apuesta implements Serializable{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private static Hashtable<Integer,Apuesta> apuestas= new Hashtable<Integer,Apuesta>();

	private int codigo; //Cada pelea tiene el mismo codigo que su respectiva apuesta
    private ArrayList<Object[]> apostadores= new ArrayList<Object[]>(); 
    private Pelea pelea;
    private double montoTotal;
    private double montoTotalGanadores;
    private ArrayList<String> estadisticas;
    
    
    public Apuesta(int codigo, Pelea pelea) {
//    	Las apuestas se crean automatica cuando se crea una pelea
		this.codigo = codigo;
		this.pelea = pelea;
		/*
		 * Si el arreglo apostadores esta vacio, es porque nadie aposto en esta pelea
		 */
		apuestas.put(codigo, this);
	}

	public String resultadoApuesta() {
    	/*
    	 * Retorna una lista de los apostadores que participaron en una apuesta en 
    	 * particular, y el dinero que ganaron o perdieron
    	 */
		
		if (pelea.getGanador() == null) {return "La pelea aun no tiene ganador";}
		if (getApostadores().isEmpty()) {return "La pelea con código " + getCodigo() + "no tuvo apuestas";}
		
		String resultadoMonto1 = "El monto total recogido en la apuesta fue: " + montoTotal + "\n" ;
		String resultadoMonto2 = "El dinero total apostado por los ganadores de esta apuesta fue: " + montoTotalGanadores + "\n\n" ;
		
		String resulta3 = "Las estadisticas de esta apuesta son las siguientes: \n";
		String resulta4 = "";
		for (String string : estadisticas) {
			resulta4 += string + "\n"; 
		}
		
    	return resultadoMonto1 + resultadoMonto2 + resulta3 + resulta4;
    }
    
    public void resolverApuesta() {
    	if (apostadores.isEmpty()) {return;}
    	
    	double montoTotal = 0;
    	double totalGanadores = 0;
//    	Primero necesito saber cuanto se recogio en total y cuanto se recogio entre los ganadores
    	for (Object[] objects : apostadores) {
    		Prisionero prisionero = (Prisionero) objects[1];
    		double apuesta = (Integer) objects[2];
    		montoTotal += apuesta;
    		if (pelea.getGanador().equals(prisionero)) {totalGanadores += apuesta;}
		}
    	
    	ArrayList<String> estadisticas = new ArrayList<>();
    	
//    	Se paga a los apostadores ganadores proporcionalmente al dinero que apostaron.
    	for (Object[] objects : apostadores) {
//    		Casteo explicito de un objeto Object a Apostador, Prisionero e Int.
    		Apostador apostador = (Apostador) objects[0];
    		Prisionero prisionero = (Prisionero) objects[1];
    		double apuesta = (Integer) objects[2];
    		
    		if (pelea.getGanador().equals(prisionero)) {
    			double k = apuesta/totalGanadores;
    			double ganancia = k*montoTotal;
    			apostador.aumentarSaldo(ganancia);
    			estadisticas.add("ID Apostador: " + apostador.getIdentificacion() + "\t\t+" + (ganancia - apuesta) + "\t\t" + "Saldo actual: " + apostador.getSaldo());
    			
    		} else {
    			estadisticas.add("ID Apostador: " + apostador.getIdentificacion() + "\t\t-" + (apuesta) + "\t\t" + "Saldo actual: " + apostador.getSaldo());
    		}
		}
    	
    	this.montoTotal = montoTotal;
    	this.montoTotalGanadores = totalGanadores;
    	this.estadisticas = estadisticas;
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
    
	public static Hashtable<Integer, Apuesta> getApuestas() {return apuestas;}
	public static void setApuestas(Hashtable<Integer, Apuesta> apuestas) {Apuesta.apuestas = apuestas;}
    
}
