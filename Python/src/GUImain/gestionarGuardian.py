import tkinter as tk
from tkinter import *
from .menuBar import MenuBar
from .fieldFrame import FieldFrame
from gestorAplicacion.guardian import Guardian
from gestorAplicacion.celda import Celda

class GestionarGuardian(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()
        self.frmInicial()

        window.iconify()

    def disenno(self):
        self.geometry("650x400")
        self.option_add("*tearOff", False)
        self.title("Gestion de Guardianes")

    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Ingresar Guardian", self.ingresarGuardian),
                            ("Borrar Guardian", self.borrarGuardian), 
                            ("Editar Guardian", self.editarGuardian),
                            ("Listar Guardianes", self.listarGuardian),
                            ("Trasladar Prisionero", self.trasladarPrisionero),
                            ("Listar Trasladados", self.listarTraslado)]

        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)

        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def frmInicial(self):
        frmBase = Frame(self)

        frm_titulo_proceso = Frame(frmBase)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10 ,pady= 10)

        lbl_titulo_proceso = Label(frm_titulo_proceso, text="Gestión de los Guardianes", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = Frame(frmBase, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso,
        text= """En esta ventana tendrá la posibilidad de gestionar todos los aspectos
        relacionados con los guardianes en las instalaciones de la Cárcel Apuestera.""", 
        font=('Arial', 10))
        lbl_descripcion_proceso.pack(pady= 10)

        frm_formulario = Frame(frmBase, borderwidth=1, relief="solid")
        frm_formulario.pack(fill=X, pady= 10)
        lbl_formulario = Label(frm_formulario,
        text= """En el menú 'Procesos y Consultas' se encuentran las funcionalidades ofrecidas""", 
        font=('Arial', 10))
        lbl_formulario.pack(fill=X, padx=10 ,pady= 10)


        self.currFrame = frmBase
        frmBase.pack()

    def ingresarGuardian(self):

        self.currFrame.pack_forget()

        frm_ingresarGuardian = Frame(self)

        frm_inicial = FieldFrame(
            frm_ingresarGuardian,
            "Criterios",
            ["Código", "Nombre", "Saldo", "Salario", "Celdas"],
            "Valores",
            [str(len(Guardian.getGuardianes())+1001), "b", "", "", ""],
            [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
            "Ingresar Guardian",
            "Registre los datos solicitados para ingresar al Guardian. \n Para el campo 'Celdas', digite los números de celdas separados por espacio"
        )

        def registro():
            celdas = frm_inicial.getValue("Celdas").split()
            dictceldas = {}
            for i in celdas:
                dictceldas[int(i)] = Celda.getCeldas()[int(i)]

            print(Guardian(frm_inicial.getValue("Nombre"), int(frm_inicial.getValue("Saldo")), int(frm_inicial.getValue("Salario")), dictceldas))

        frm_inicial.set_command_btn_aceptar(registro)
        frm_inicial.pack(fill=tk.BOTH, expand=True)

        self.currFrame = frm_ingresarGuardian
        frm_ingresarGuardian.pack()

    def borrarGuardian(self):
        pass

    def editarGuardian(self):
        pass

    def listarGuardian(self):
        pass

    def trasladarPrisionero(self):
        pass

    def listarTraslado(self):
        pass

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()