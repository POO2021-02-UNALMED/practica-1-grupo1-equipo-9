from tkinter import *
from .menuBar import MenuBar

class GestionarApuesta(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()

        window.iconify()

    def disenno(self):
        self.geometry("850x500")
        self.option_add("*tearOff", False)
        self.title("Gestion de Apuestas")


    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Ingresar Apostador", self.ingresarApostador),
                            ("Resultado Apuestas", self.resultadoApuestas)]

        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def ingresarApostador(self):
        pass

    def resultadoApuestas(self):
        pass

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()