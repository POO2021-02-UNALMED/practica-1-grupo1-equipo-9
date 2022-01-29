from tkinter import *
from .menuBar import MenuBar

class GestionarPelea(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()

        window.iconify()

    def disenno(self):
        self.geometry("850x500")
        self.option_add("*tearOff", False)
        self.title("Gestion de Peleas")


    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Registrar Pelea", self.registrarPelea),
                            ("Definir Pelea", self.definirPelea), 
                            ("Listar Peleas", self.listarPelea),
                            ("Battle Royale", self.battleRoyale)]

        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def registrarPelea(self):
        pass

    def definirPelea(self):
        pass

    def listarPelea(self):
        pass

    def battleRoyale(self):
        pass

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()