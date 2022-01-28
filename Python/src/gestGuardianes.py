from tkinter import *

class GestionarGuardian(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window
        self.geometry("850x500")
        self.option_add("*tearOff", False)
        self.title("Gestion de Guardianes")

        self.crearMenu()

        window.iconify()

    def crearMenu(self):
        menubar = Menu(self)

        menuArchiv = Menu(menubar)
        menuProcyCons = Menu(menubar)
        menuAyuda = Menu(menubar)

        menubar.add_cascade(menu=menuArchiv, label='Archivo')
        menubar.add_cascade(menu=menuProcyCons, label='Procesos y Consultas')
        menubar.add_cascade(menu=menuAyuda, label='Ayuda')

        menuArchiv.add_command(label="Aplicación", command=self.evento)
        menuArchiv.add_command(label="Salir", command=self.salir)

        menuProcyCons.add_command(label="Ingresar guardian", command= self.evento)
        menuProcyCons.add_command(label="Borrar guardian", command= self.evento)
        menuProcyCons.add_command(label="Editar guardian", command= self.evento)
        menuProcyCons.add_command(label="Listar guardianes", command= self.evento)
        menuProcyCons.add_command(label="Trasladar prisionero", command= self.evento)
        menuProcyCons.add_command(label="Listar trasladados", command= self.evento)


        menuAyuda.add_command(label="Acerca de", command=self.evento)
        

        self['menu'] = menubar

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()