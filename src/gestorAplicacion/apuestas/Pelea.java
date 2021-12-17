/*
 * Autores: 
 * - Beatriz Valentina Gomez Valencia.
 * - Alejandro Salazar Mejia.
 * - Juan Pablo Martinez Echavarria.
 * 
 * La clase Pelea tiene como finalidad implementar metodos para ejecucion de una pelea:
 * - Definir los peleadores (en cada Pelea solo se involucran dos Prisioneros).
 * - Definir un ganador.
 * - Definir una clase de Pelea especial la cuall nombramos BattleRoyale.
 * - Cada pelea posee su respectiva Apuesta.
 * 
 * Posee los siguientes atributos:
 * - codigo (int): Permite la identificacion de cada apuesta (es el mismo que posee la clase Pelea).
 * - genero (genero): Permite identificar si la pelea es entre mujeres u hombres.
 * - peleas (Hashtable<Integer, Pelea>): Permite llevar un registro de de las peleas realizadas, donde
 *   la clave de la Hashtable es el codigo de la pelea y Pelea es this.Pelea.
 * - luchador1 y luchador2 (Prisionero): Los prisioneros involucrados en la Pelea.
 * - armaLuchador1 y armaLuchador2 (String): Cada luchador tiene derecho a un arma.
 * - ganador (Prisionero): El ganador de la Pelea.
 * - apuesta (Apuesta): La apuesta a la cual se dirige this.Pelea.
 */

package gestorAplicacion.apuestas;
import java.io.Serializable;
import java.util.Random;
import java.util.ArrayList;
import java.util.Hashtable;

import gestorAplicacion.carcel.Celda;
import gestorAplicacion.carcel.Prisionero;

public class Pelea implements Serializable{
  
	private static final long serialVersionUID = 1L;
	
	private int codigo; //Cada pelea tiene el mismo codigo que su respectiva apuesta
    private gestorAplicacion.carcel.genero genero;
    private Prisionero luchador1;
    private Prisionero luchador2;
    private String armaLuchador1;
    private String armaLuchador2;
    private Prisionero ganador;
    private Apuesta apuesta;
    
    private static Hashtable<Integer, Pelea> peleas = new Hashtable<>();
    
    /*
     * Cuando se crea una Pelea, automaticamente se crea su respectiva Apuesta.
     */
    public Pelea(int codigo, gestorAplicacion.carcel.genero genero, Prisionero luchador1, Prisionero luchador2,
			String armaLuchador1, String armaLuchador2) {
		this.codigo = codigo;
		this.genero = genero;
		this.luchador1 = luchador1;
		this.luchador2 = luchador2;
		this.armaLuchador1 = armaLuchador1;
		this.armaLuchador2 = armaLuchador2;
		
		this.apuesta = new Apuesta(codigo, this);
		
		peleas.put(codigo, this);
	}
	public void setGanador(Prisionero prisionero) {
		this.ganador = prisionero;
		apuesta.resolverApuesta();
	}
	
    public Prisionero getGanador() {return ganador;}

    /*
     * Cada Pelea puede tener unicamente 2 luchadores.
     */
    public Prisionero[] getLuchadores() {
		Prisionero[] luchadores = {luchador1, luchador2};
    	return luchadores;
    }
    
    /*
     * El metodo battleRoyale recibe como parametro una lista de celdas.
     * Toma los prisioneros de las celdas que recibe como parametro y las ingresa en una lista temporal,
     * luego los empareja de manera aleatoria y se enfrentan en un combate en el cual cada participante tiene
     * una probabiblidad de 50% de ganar.
     * Cada pareja realiza un combate y se elimina de la lista general al prisionero perdedor.
     * Este proceso se repite hasta que en la lista general quede un solo prisionero el cual es el ganador del
     * battleRoyale y recibe como premio un ingremento de 1000 a su saldo.
     * 
     * Durante la ejecucion el metodo retorna un arraylist de strings, que muestra los resultados de los combates
	 * y quien es el Prisionero ganador.
     */
    public static
    Object battleRoyale(ArrayList<Celda> celdas){
		
    	int l1;
    	int l2;
    	Random r = new Random();
    	ArrayList<Integer> luchadores = new ArrayList<Integer>();
    	ArrayList<String> combates = new ArrayList<String>();
    	
    	for(Celda c:celdas) {
    		c.getPrisioneros().forEach((k,v)-> luchadores.add(k));
      	}	
    	do{
    		int rN1 = r.nextInt(luchadores.size());
    		l1=luchadores.get(rN1);
    		luchadores.remove(rN1);
    		
    		int rN2 = r.nextInt(luchadores.size());
    		l2=luchadores.get(rN2);
    		luchadores.remove(rN2);
    		
    		int g = r.nextInt(2);
    		
    		if (g==0){
    			luchadores.add(l1);
    			combates.add("El prisionero "+ l1 +" ha derrotado al prisionero "+ l2);
    		}
    		else{
    			luchadores.add(l2);
    			combates.add("El prisionero "+ l2 +" ha derrotado al prisionero "+ l1);
    		}
    	}while(luchadores.size()>1);
    	
    	Prisionero ganador = Prisionero.getPrisioneros().get(luchadores.get(0));
    	combates.add("El prisionero "+ luchadores.get(0) + " es el ganador y recibio 1000 dolares");
        Object[] resultado = {ganador, combates};
        Prisionero.getPrisioneros().get(luchadores.get(0)).aumentarSaldo(1000);
       
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