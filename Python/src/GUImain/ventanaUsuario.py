from tkinter import *
from tkinter import messagebox
from .gestionarAntidelito import GestionarAntidelito
from .gestionarApuesta import GestionarApuesta
from .gestionarDelito import GestionarDelito
from .gestionarGuardian import GestionarGuardian
from .gestionarPelea import GestionarPelea
from .gestionarPrisionero import GestionarPrisionero
from .utils.menuBar import MenuBar


class VentanaUsuario(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window
        self.crearContenido()
        window.iconify()


    def crearContenido(self):
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


    def crearMenu(self):

        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Gestionar Guardianes", lambda: GestionarGuardian(self)),
                            ("Gestionar Prisioneros", lambda: GestionarPrisionero(self)), 
                            ("Gestionar Delitos", lambda: GestionarDelito(self)),
                            ("Gestionar Antidelitos", lambda: GestionarAntidelito(self)),
                            ("Gestionar Peleas", lambda: GestionarPelea(self)),
                            ("Gestionar Apuestas", lambda: GestionarApuesta(self))]
        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)


    def evento(self):
        messagebox.showinfo(title="Integrantes", 
        message="Beatriz Valentina Gomez Valencia \n"+
        "Alejandro Salazar Mejía \n"+
        "Juan Pablo Martínez Echavarría \n"+
        "Hernan Camilo Rivera Arteaga")


    def salir(self):
        self.MASTER.deiconify()
        self.destroy()