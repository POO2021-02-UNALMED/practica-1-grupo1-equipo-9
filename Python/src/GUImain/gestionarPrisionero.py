from tkinter import *
from .utils.menuBar import MenuBar

class GestionarPrisionero(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()

        window.iconify()

    def disenno(self):
        self.geometry("850x500")
        self.option_add("*tearOff", False)
        self.title("Gestion de Prisioneros")


    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Ingresar Prisionero", self.ingresarPrisionero),
                            ("Borrar Prisionero", self.borrarPrisionero), 
                            ("Agregar Delito", self.agregarDelito),
                            ("Agregar Antidelito", self.agregarAntidelito),
                            ("Listar Prisioneros", self.listarPrisionero)]

        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def ingresarPrisionero(self):
        pass

    def borrarPrisionero(self):
        pass

    def agregarDelito(self):
        pass

    def agregarAntidelito(self):
        pass

    def listarPrisionero(self):
        pass

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()