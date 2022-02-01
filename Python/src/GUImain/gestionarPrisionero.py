from cgitb import text
from importlib.metadata import entry_points
from struct import pack
from textwrap import fill
from tkinter import *
from tkinter import font
from tkinter import messagebox

from gestorAplicacion.prisionero import Prisionero
from .utils.fieldFrame import FieldFrame

from numpy import pad
from .utils.menuBar import MenuBar


class GestionarPrisionero(Toplevel):

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

    def frmInicial(self):
        frmBase = Frame(self)

        frm_titulo_proceso = Frame(frmBase)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10 ,pady= 10)

        lbl_titulo_proceso = Label(frm_titulo_proceso, text="Gestión de Prisioneros", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = Frame(frmBase, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso,
        text= """En esta ventana tendrá la posibilidad de gestionar todos los aspectos
        relacionados con los prisioneros recluidos en las instalaciones de la Cárcel Apuestera.""", 
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

    def ingresarPrisionero(self):
        self.currFrame.pack_forget()

        frm_ingresarPrisionero=Frame(self)

        frm_ingresar=FieldFrame(frm_ingresarPrisionero, "Criterios", ["Identificación", "Nombre", "Saldo", "Género", "Celda", "Delitos"], 
         "Valores", [str(len(Prisionero.getPrisioneros())+1), None, None, None, None, None], [DISABLED, NORMAL, NORMAL, NORMAL, NORMAL, NORMAL], "Ingresar Prisionero", 
         "Ingrese los datos solicitados para registrar el Prisionero")

        def registro():
            pass

        frm_ingresar.set_command_btn_aceptar(registro)
        frm_ingresar.pack(fill=BOTH, expand=TRUE)
        self.currFrame=frm_ingresarPrisionero
        frm_ingresarPrisionero.pack()

        
    def borrarPrisionero(self):
        self.currFrame.pack_forget()

        frm_borrarPrisionero=Frame(self)

        frm_titulo_proceso=Frame(frm_borrarPrisionero)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10, pady=10)

        lbl_titulo_proceso=Label(frm_titulo_proceso, text="Borrar Prisionero", font=('Arial', 15))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=Frame(frm_borrarPrisionero, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=X, padx=10, pady=10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso, text="Ingrese la identificación del Prisionero", font=('Arial', 10))
        lbl_descripcion_proceso.pack(fill=X, padx=10, pady=10)


        frm_dato=Frame(frm_borrarPrisionero, borderwidth=1, relief="solid")

        Label(frm_dato, text="Identificación: ").grid(column=0, row=0, padx=15, pady=5)
        entry_Identificacion=Entry(frm_dato, justify=CENTER)
        entry_Identificacion.grid(column=1, row=0, padx=15,pady=5)

        def borrar():
            entry_Identificacion.delete(0,END)
            entry_Identificacion.insert(0,"")

        def func_borrarPrisionero():
            messagebox.askyesno(message="¿Está seguro que desea eliminar el Prisionero?")

            if(True):
                pass
            else:
                pass    

        fuente="Helvetica 10 bold"
        btn_aceptar = Button(frm_dato, text="Aceptar", font=fuente, command= func_borrarPrisionero)
        btn_aceptar.grid(column=0, row=5, padx=15, pady=15)
        btn_borrar = Button(frm_dato, text="Borrar", font=fuente, command= borrar)
        btn_borrar.grid(column=1, row=5, padx=15, pady=15)

        frm_dato.pack(expand=True, padx=30)
        self.currFrame = frm_borrarPrisionero
        frm_borrarPrisionero.pack()

    def agregarDelito(self):
        self.currFrame.pack_forget()

        frm_agregarDelito=Frame(self)

        frm_titulo_proceso=Frame(frm_agregarDelito)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10, pady=10)

        lbl_titulo_proceso=Label(frm_titulo_proceso, text="Agregar Delito", font=('Arial', 15))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=Frame(frm_agregarDelito, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=X, padx=10, pady=10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso, text="Ingrese el Delito que desea agregar al Prisionero", font=('Arial', 10))
        lbl_descripcion_proceso.pack(fill=X, padx=10, pady=10)


        frm_dato=Frame(frm_agregarDelito, borderwidth=1, relief="solid")

        Label(frm_dato, text="Nombre: ").grid(column=0, row=0, padx=15, pady=5)
        entry_Nombre=Entry(frm_dato, justify=CENTER)
        entry_Nombre.grid(column=1, row=0, padx=15,pady=5)

        def borrar():
            entry_Nombre.delete(0,END)
            entry_Nombre.insert(0,"")

        def func_agregarDelito():
            pass

        fuente="Helvetica 10 bold"
        btn_aceptar = Button(frm_dato, text="Aceptar", font=fuente, command= func_agregarDelito)
        btn_aceptar.grid(column=0, row=5, padx=15, pady=15)
        btn_borrar = Button(frm_dato, text="Borrar", font=fuente, command= borrar)
        btn_borrar.grid(column=1, row=5, padx=15, pady=15)

        frm_dato.pack(expand=True, padx=30)
        self.currFrame = frm_agregarDelito 
        frm_agregarDelito.pack()

    def agregarAntidelito(self):
        self.currFrame.pack_forget()

        frm_agregarAntidelito=Frame(self)

        frm_titulo_proceso=Frame(frm_agregarAntidelito)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10, pady=10)

        lbl_titulo_proceso=Label(frm_titulo_proceso, text="Agregar Antidelito", font=('Arial', 15))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=Frame(frm_agregarAntidelito, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=X, padx=10, pady=10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso, text="Ingrese el Antidelito que desea agregar al Prisionero", font=('Arial', 10))
        lbl_descripcion_proceso.pack(fill=X, padx=10, pady=10)

        frm_dato=Frame(frm_agregarAntidelito, borderwidth=1, relief="solid")

        Label(frm_dato, text="Nombre: ").grid(column=0, row=0, padx=15, pady=5)
        entry_Nombre=Entry(frm_dato, justify=CENTER)
        entry_Nombre.grid(column=1, row=0, padx=15,pady=5)

        def borrar():
            entry_Nombre.delete(0,END)
            entry_Nombre.insert(0,"")

        def func_agregarAntidelito():
            pass

        fuente="Helvetica 10 bold"
        btn_aceptar = Button(frm_dato, text="Aceptar", font=fuente, command= func_agregarAntidelito)
        btn_aceptar.grid(column=0, row=5, padx=15, pady=15)
        btn_borrar = Button(frm_dato, text="Borrar", font=fuente, command= borrar)
        btn_borrar.grid(column=1, row=5, padx=15, pady=15)

        frm_dato.pack(expand=True, padx=30)
        self.currFrame = frm_agregarAntidelito 
        frm_agregarAntidelito.pack()

    def listarPrisionero(self):
        self.currFrame.pack_forget()

        frm_listaPrisioneros=Frame(self)

        frm_titulo_proceso=Frame(frm_listaPrisioneros)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10,pady=10)

        lbl_titulo_proceso=Label(frm_titulo_proceso, text="Lista de Prisioneros", font=('Arial', 13, 'bold'))
        lbl_titulo_proceso.pack()

        self.currFrame=frm_listaPrisioneros
        frm_listaPrisioneros.pack()

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()