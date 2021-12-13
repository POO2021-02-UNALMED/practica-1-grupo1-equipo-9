package gestorAplicacion.apuestas;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Prisionero;

public class Pelea implements Serializable{
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private int codigo; //Cada pelea tiene el mismo c�digo que su respectiva apuesta
    private gestorAplicacion.carcel.genero genero;
    private Prisionero luchador1;
    private Prisionero luchador2;
    private String armaLuchador1;
    private String armaLuchador2;
    private Prisionero ganador;
    private Apuesta apuesta;
    
    private static Hashtable<Integer, Pelea> peleas = new Hashtable<>();
    
    public Pelea(int codigo, gestorAplicacion.carcel.genero genero, Prisionero luchador1, Prisionero luchador2,
			String armaLuchador1, String armaLuchador2) {
		this.codigo = codigo;
		this.genero = genero;
		this.luchador1 = luchador1;
		this.luchador2 = luchador2;
		this.armaLuchador1 = armaLuchador1;
		this.armaLuchador2 = armaLuchador2;
		
		this.apuesta = new Apuesta(codigo, this);
//		Se crea automaticamente la apuesta correspondiente a esta pelea
		
		peleas.put(codigo, this);
	}
	public void setGanador(Prisionero prisionero) {
		this.ganador = prisionero;
		apuesta.resolverApuesta();
	}
    public Prisionero getGanador() {return ganador;}

    public Prisionero[] getLuchadores() {
		Prisionero[] luchadores = {luchador1, luchador2};
    	return luchadores;
    }
    
    public 
    Object battleRoyale(ArrayList<Celda> celdas){
		/*
		 * Devuelve un arraylist de strings, donde cada string es un comentario tipo
		 * "prisionero 1 ha derrotado a prisionero 2", etc tambien debe devolver el
		 * prisionero ganador
		 */
    	
    	/*Hashtable<Integer,Prisionero> luchadores = new Hashtable<Integer,Prisionero>();
    	for (Celda c: celdas) {
    		c.getPrisioneros().forEach((k,v)-> luchadores.put(k,v));
    		//while o for
    			int rN1 = (int)(Math.random()*(luchadores.size()));
    			int rN2 = (int)(Math.random()*(luchadores.size()));
    			if(rN1==rN2) {rN2 = (int)(Math.random()*(luchadores.size()));}
    			else {
    				
    			}
    	}*/
    	int l1;
    	int l2;
    	ArrayList<Integer> luchadores = new ArrayList<Integer>();
    	ArrayList<String> combates = new ArrayList<String>();
    	for(Celda c:celdas) {
    		c.getPrisioneros().forEach((k,v)-> luchadores.add(k));
    		
    		int rN1 = (int)(Math.random()*(luchadores.size()));
    		l1=luchadores.get(rN1);
    		luchadores.remove(rN1); //luchadores.remove(luchadores.indexOf(rN1))
			int rN2 = (int)(Math.random()*(luchadores.size()));
			l2=luchadores.get(rN2);
			luchadores.remove(rN2);
			
			/*pelea entre l1 y l2
			*if (l1 gana){
			*	luchadores.add(l1);
			*	combates.add("El prisionero 1 ha derrotado al prisionero 2")
			*	return combates + Prisioneros.get(l1)}
			*else{
			*	luchadores.add(l2);
			*	combates.add("El prisionero 2 ha derrotado al prisionero 1")
			*	return combates+ Prisioneros.get(l2)}
			*/
    		
    	}
    	
    	return combates;
    	/*Prisionero ganador = null;
    	Object[] resultado = {ganador, combates};
    	return resultado;*/
    }

    public int getCodigo() {return codigo;}
	public void setCodigo(int codigo) {this.codigo = codigo;}
    
	public gestorAplicacion.carcel.genero getGenero() {return genero;}
	public void setGenero(gestorAplicacion.carcel.genero genero) {this.genero = genero;}

	public String getArmaLuchador1() {return armaLuchador1;}
	public void setArmaLuchador1(String armaLuchador1) {this.armaLuchador1 = armaLuchador1;}

	public String getArmaLuchador2() {return armaLuchador2;}
	public void setArmaLuchador2(String armaLuchador2) {this.armaLuchador2 = armaLuchador2;}
	
	public Apuesta getApuesta() {return apuesta;}
	public void setApuesta(Apuesta apuesta) {this.apuesta = apuesta;}
	
	public static Hashtable<Integer, Pelea> getPeleas() {return peleas;}
	public static void setPeleas(Hashtable<Integer, Pelea> peleas) {Pelea.peleas = peleas;}
	
	@Override
	public String toString() {
		
		return "PELEA: " + codigo + "\n" 
				+ "Genero: " + genero + "\n" 
				+ "Luchador 1: " + luchador1.getNombre() +"\n" 
				+ "Luchador 2: " + luchador2.getNombre() + "\n" 
				+ "Arma luchador 1: " + armaLuchador1 + "\n" 
				+ "Arma luchador 2: " + armaLuchador2 + "\n" 
				+ "Ganador: " + (ganador == null ? "Aun no hay ganador" : ganador.getNombre()) + "\n";
	}  
	
	
}
