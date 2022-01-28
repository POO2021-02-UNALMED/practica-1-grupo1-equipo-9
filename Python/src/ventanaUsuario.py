from tkinter import *
from gestGuardianes import GestionarGuardian
from menuPrincipal import MenuPrincipal


class VentanaUsuario(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window
        self.geometry("400x220")
        self.option_add("*tearOff", False)
        self.title("Ventana Principal de Usuario")

        self.crearMenu()

        frame_a = Frame(self)
        frame_b = Frame(self)

        Label(frame_a, font=('Arial', 15),
                text="Gestion de la Carcel Apuestera", width=30, height=5).pack()
        Label(frame_b, font=('Arial', 10),
                text="En el menú 'Procesos y Consultas' podra elegir\n que entidad desea gestionar").pack()

        frame_a.pack()
        frame_b.pack()

        window.iconify()

    def crearMenu(self):

        menubar = MenuPrincipal(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Gestionar Guardianes", lambda: GestionarGuardian(self)),
                            ("Gestionar Prisioneros", lambda: Toplevel()), 
                            ("Gestionar Delitos", lambda: Toplevel()),
                            ("Gestionar Antidelitos", lambda: Toplevel()),
                            ("Gestionar Peleas", lambda: Toplevel()),
                            ("Gestionar Apuestas", lambda: Toplevel())]
        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()