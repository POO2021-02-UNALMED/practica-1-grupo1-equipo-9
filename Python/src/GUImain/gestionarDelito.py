from tkinter import *
from .utils.menuBar import MenuBar

class GestionarDelito(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()

        window.iconify()

    def disenno(self):
        self.geometry("650x500")
        self.option_add("*tearOff", False)
        self.title("Gestion de Delitos")


    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Ingresar Delito", self.ingresarDelito),
                            ("Borrar Delito", self.borrarDelito), 
                            ("Editar Delito", self.editarDelito),
                            ("Listar Delitos", self.listarDelito)]
                            
        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def ingresarDelito(self):
        pass

    def borrarDelito(self):
        pass

    def editarDelito(self):
        pass

    def listarDelito(self):
        pass

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()