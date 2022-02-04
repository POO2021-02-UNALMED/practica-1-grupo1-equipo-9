from GUImain import ventanaPrincipal
from baseDatos.deserializador import deserializar


window = ventanaPrincipal.VentanaPrincipal()

deserializar()

window.mainloop()