package gestorAplicacion.apuestas;

public abstract class Apostador {
	protected int identificacion;
    protected String nombre;
    protected int saldo;
    
    public Apostador(int identificacion, String nombre, int saldo) {
		this.identificacion = identificacion;
		this.nombre = nombre;
		this.saldo = saldo;
	}

	public void aumentarSaldo(double dinero) {
    	
    }
    
    public void reducirSaldo(double dinero) {
    	
    }
    
    public abstract String toString();
}
