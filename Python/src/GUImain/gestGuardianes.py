from tkinter import *
from .menuPrincipal import MenuBar

class GestionarGuardian(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()

        window.iconify()

    def disenno(self):
        self.geometry("850x500")
        self.option_add("*tearOff", False)
        self.title("Gestion de Guardianes")


    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Ingresar guardian", self.ingresarGuardian),
                            ("Borrar guardian", self.borrarGuardian), 
                            ("Editar guardian", self.editarGuardian),
                            ("Listar guardianes", self.listarGuardian),
                            ("Trasladar prisionero", self.trasladarPrisionero),
                            ("Listar trasladados", self.listarTraslados)]
        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def ingresarGuardian(self):
        pass

    def borrarGuardian(self):
        pass

    def editarGuardian(self):
        pass

    def listarGuardian(self):
        pass

    def trasladarPrisionero(self):
        pass

    def listarTraslados(self):
        pass

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()