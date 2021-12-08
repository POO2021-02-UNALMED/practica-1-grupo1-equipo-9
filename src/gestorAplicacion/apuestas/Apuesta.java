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
   
    }
    
    public void agregarApostador(Apostador apostador,Prisionero prisionero,Integer apuesta) {
    	
    }

	public int getCodigo() {return codigo;}
	public void setCodigo(int codigo) {	this.codigo = codigo;}

	public Pelea getPelea() {return pelea;}
	public void setPelea(Pelea pelea) {	this.pelea = pelea;}

	public ArrayList<Object[]> getApostadores() {return apostadores;}
    
    
}
