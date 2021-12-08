package gestorAplicacion.apuestas;
import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Prisionero;

public class Pelea {
    private int codigo; //Cada pelea tiene el mismo código que su respectiva apuesta
    private gestorAplicacion.carcel.genero genero;
    private Prisionero luchador1;
    private Prisionero luchador2;
    private String armaLuchador1;
    private String armaLuchador2;
    private Prisionero ganador;
    private Apuesta apuesta;
    
    private static Hashtable<Integer, Pelea> peleas;
    
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
		 * "prisionero 1 a derrotado a prisionero 2", etc tambiï¿½n debe devolver el
		 * prisionero ganador
		 */
//		TODO
    	ArrayList<String> combates = new ArrayList<String>();
    	Prisionero ganador = null;
    	Object[] resultado = {ganador, combates};
    	return resultado;
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
}
