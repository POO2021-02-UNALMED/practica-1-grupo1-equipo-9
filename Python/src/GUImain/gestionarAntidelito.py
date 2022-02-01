from tkinter import *
from .utils.menuBar import MenuBar


class GestionarAntidelito(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()

        window.iconify()

    def disenno(self):
        self.geometry("850x500")
        self.option_add("*tearOff", False)
        self.title("Gestion de Antidelitos")


    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Ingresar Antidelito", self.ingresarAntidelito),
                            ("Borrar Antidelito", self.borrarAntidelito), 
                            ("Editar Antidelito", self.editarAntidelito),
                            ("Listar Antidelitos", self.listarAntidelito)]

        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def ingresarAntidelito(self):
        pass

    def borrarAntidelito(self):
        pass

    def editarAntidelito(self):
        pass

    def listarAntidelito(self):
        pass

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()