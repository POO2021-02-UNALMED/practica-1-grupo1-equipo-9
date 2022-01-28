from tkinter import *
from gestGuardianes import GestionarGuardian

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
        menubar = Menu(self)

        menuArchiv = Menu(menubar)
        menuProcyCons = Menu(menubar)
        menuAyuda = Menu(menubar)

        menubar.add_cascade(menu=menuArchiv, label='Archivo')
        menubar.add_cascade(menu=menuProcyCons, label='Procesos y Consultas')
        menubar.add_cascade(menu=menuAyuda, label='Ayuda')

        menuArchiv.add_command(label="Aplicación", command=self.evento)
        menuArchiv.add_command(label="Salir", command=self.salir)

        menuProcyCons.add_command(label="Gestionar Guardianes", command=lambda: GestionarGuardian(self))
        menuProcyCons.add_command(label="Gestionar Prisioneros", command=lambda: Toplevel())
        menuProcyCons.add_command(label="Gestionar Delitos", command=lambda: Toplevel())
        menuProcyCons.add_command(label="Gestionar Antidelitos", command=lambda: Toplevel())
        menuProcyCons.add_command(label="Gestionar Peleas", command=lambda: Toplevel())
        menuProcyCons.add_command(label="Gestionar Apuestas", command=lambda: Toplevel())

        menuAyuda.add_command(label="Acerca de", command=self.evento)
        

        self['menu'] = menubar

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()