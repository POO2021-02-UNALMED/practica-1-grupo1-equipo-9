/*
 * Autores: 
 * - Beatriz Valentina Gomez Valencia.
 * - Alejandro Salazar Mejia.
 * - Juan Pablo Martinez Echavarria.
 *  
 * La clase Apostador tiene como finalidad aplicar el concepto de clase Abstracta y Herencia.
 * Esta clase es Padre de las clases Guardian y Prisionero las cuales comparten los siguientes atributos:
 * - identificacion (int): Permite la identificacion de cada apostador por medio de un entero.
 * - nombre (String): Permite la identificacion por medio de String.
 * - saldo (int): Representa la cantidad de dinero que un Apostador tiene en su cuenta. 
 */

package gestorAplicacion.apuestas;

import java.io.Serializable;

public abstract class Apostador implements Serializable{

	private static final long serialVersionUID = 1L;
	
	protected int identificacion;
    protected String nombre;
    protected int saldo;
    
    /*
     * Apostador es una clase abstracta, solo se usa su constructor en las clases que heredan 
     * de el (Prisionero y Guardian).
     */
    protected Apostador(int identificacion, String nombre, int saldo) {
		this.identificacion = identificacion;
		this.nombre = nombre;
		this.saldo = saldo;
	}
    
    /*
     * Recibe como parametro dinero.
     * Tiene como finalidad agregar una cantidad especificada al saldo del Apostador. 
     */
	public void aumentarSaldo(double dinero) {
    	this.saldo += dinero;
    }
    
	/*
	 * Recibe como parametro dinero.
     * Tiene como finalidad agregar una cantidad especificada al saldo del Apostador.
	 */
    public void reducirSaldo(double dinero) {
    	this.saldo -= dinero;
    }
    
    public abstract String toString();

	public int getIdentificacion() {return identificacion;	}
	public void setIdentificacion(int identificacion) {	this.identificacion = identificacion;}

	public String getNombre() {	return nombre;}
	public void setNombre(String nombre) {this.nombre = nombre;}

	public int getSaldo() {	return saldo;}
	public void setSaldo(int saldo) {this.saldo = saldo;}    
}