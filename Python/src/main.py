from GUImain import ventanaPrincipal
from baseDatos.deserializador import deserializar


window = ventanaPrincipal.VentanaPrincipal()
window.crearContenido()

deserializar()

window.mainloop()