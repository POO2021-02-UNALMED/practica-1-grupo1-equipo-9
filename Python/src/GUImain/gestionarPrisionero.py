from email import message
from textwrap import fill
import tkinter as tk
from tkinter import Canvas, Label, ttk
from tkinter import messagebox
from tkinter import font
from turtle import width

from numpy import pad
from gestorAplicacion.delito import Delito
from gestorAplicacion.genero import genero
from gestorAplicacion.antidelito import Antidelito
from gestorAplicacion.prisionero import Prisionero
from .utils.fieldFrame import FieldFrame
from .utils.menuBar import MenuBar


class GestionarPrisionero(tk.Toplevel):

    def __init__(self, window: tk.Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()
        self.frmInicial()

        window.iconify()

    def disenno(self):
        self.geometry("650x450")
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
        frmBase = tk.Frame(self)

        frm_titulo_proceso = tk.Frame(frmBase)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10 ,pady= 10)

        lbl_titulo_proceso = tk.Label(frm_titulo_proceso, text="Gestión de Prisioneros", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = tk.Frame(frmBase, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso,
        text= """En esta ventana tendrá la posibilidad de gestionar todos los aspectos
        relacionados con los prisioneros recluidos en las instalaciones de la Cárcel Apuestera.""", 
        font=('Arial', 10))
        lbl_descripcion_proceso.pack(pady= 10)

        frm_formulario = tk.Frame(frmBase, borderwidth=1, relief="solid")
        frm_formulario.pack(fill=tk.X, pady= 10)
        lbl_formulario = tk.Label(frm_formulario,
        text= """En el menú 'Procesos y Consultas' se encuentran las funcionalidades ofrecidas""", 
        font=('Arial', 10))
        lbl_formulario.pack(fill=tk.X, padx=10 ,pady= 10)


        self.currFrame = frmBase
        frmBase.pack()

    def ingresarPrisionero(self):
        self.currFrame.pack_forget()

        frm_ingresarPrisionero=tk.Frame(self)

        frm_ingresar=FieldFrame(frm_ingresarPrisionero, "Criterios", ["Identificación", "Nombre", "Saldo", "Género", "Celda", "Delitos"], 
         "Valores", [str(len(Prisionero.getPrisioneros())+1), None, None, None, None, None], [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL], 
         "Ingresar Prisionero", "Ingrese los datos solicitados para registrar el prisionero \n" + "Para el campo 'Género', digite M o F \n" + "Para el campo 'Delitos', digite el código de los delitos separados por espacio" )

        def registro():
            from GUImain.exceptionClasses.exceptionObjNoEncontrado import ExceptionObjNoEncontrado

            delitos=frm_ingresar.getValue("Delitos").split()
            ddelitos={}
            
            for i in delitos:
                ddelitos[int(i)]=Delito.getDelitos()[int(i)]

            # Validación del género usando las clases Exception
            try:
                ExceptionObjNoEncontrado(   "Género inválido.", 
                                            frm_ingresar.getValue("Género"), ["M"])
                gen= genero.M
            except:
                try:
                    ExceptionObjNoEncontrado(   "Género inválido.", 
                                                frm_ingresar.getValue("Género"), ["F"])
                    gen= genero.F        
                except ExceptionObjNoEncontrado as f:
                    f.messbox()
                    return 

            Prisionero(frm_ingresar.getValue("Nombre"), int(frm_ingresar.getValue("Saldo")), gen, int(frm_ingresar.getValue("Celda")), ddelitos)
            tk.messagebox.showinfo(message="El prisionero ha sido registrado correctamente")
            self.salir()

        frm_ingresar.set_command_btn_aceptar(registro)
        frm_ingresar.pack(fill=tk.BOTH, expand=True)
        self.currFrame=frm_ingresarPrisionero
        frm_ingresarPrisionero.pack()
      
    def borrarPrisionero(self):
        self.currFrame.pack_forget()

        frm_borrarPrisionero=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_borrarPrisionero)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Borrar Prisionero", font=('Arial', 15))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_borrarPrisionero, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso, text="Seleccione la identificación del Prisionero que desea eliminar", font=('Arial', 10))
        lbl_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        frm_borrar=tk.Frame(frm_borrarPrisionero, borderwidth=1, relief="solid")
        prisioneros=[k for (k,v) in Prisionero.getPrisioneros().items()]

        tk.Label(frm_borrar, text="Identificación: ").grid(column=0, row=1, padx=15, pady=5)
        cbox_identificacion=ttk.Combobox(frm_borrar, values=prisioneros, justify=tk.CENTER, state="readonly")
        cbox_identificacion.grid(column=1,row=1,padx=15,pady=5)


        def func_borrarPrisionero():

            warning=tk.messagebox.askyesno(message="¿Está seguro que desea eliminar el prisionero?")

            if warning:
                Prisionero.getPrisioneros().pop(int(cbox_identificacion.get()))
                tk.messagebox.showinfo(message="El prisionero ha sido eliminado correctamente")
                self.salir()
            else:
                pass


        def cancelar():
            self.salir()

        fuente="Helvetica 10 bold"
        btn_aceptar = tk.Button(frm_borrar, text="Aceptar", font=fuente, command= func_borrarPrisionero)
        btn_aceptar.grid(column=0, row=5, padx=15, pady=15)
        btn_cancelar = tk.Button(frm_borrar, text="Cancelar", font=fuente, command= cancelar)
        btn_cancelar.grid(column=1, row=5, padx=15, pady=15)

        frm_borrar.pack(expand=True, padx=30)
        self.currFrame = frm_borrarPrisionero
        frm_borrarPrisionero.pack()

    def agregarDelito(self):
        self.currFrame.pack_forget()

        frm_agregarDelito=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_agregarDelito)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Agregar Delito", font=('Arial', 15))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_agregarDelito, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso, text="Seleccione la identificación del prisionero y el código del delito que desea agregar", font=('Arial', 10))
        lbl_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        frm_agregar=tk.Frame(frm_agregarDelito, borderwidth=1, relief="solid")

        prisioneros=[k for (k,v) in Prisionero.getPrisioneros().items()]
        delitos=[k for (k,v) in Delito.getDelitos().items()]

        tk.Label(frm_agregar, text="Identificación: ").grid(column=0, row=1, padx=15, pady=5)
        cbox_identificacion=ttk.Combobox(frm_agregar, values=prisioneros, justify=tk.CENTER, state="readonly")
        cbox_identificacion.grid(column=1,row=1,padx=15,pady=5) 

        tk.Label(frm_agregar, text="Código: ").grid(column=0, row=2, padx=15, pady=5)
        cbox_codigo=ttk.Combobox(frm_agregar, values=delitos, justify=tk.CENTER, state="readonly")
        cbox_codigo.grid(column=1,row=2,padx=15,pady=5)  

        def func_agregarDelito():
            prisionero= Prisionero.getPrisioneros()[int(cbox_identificacion.get())]
            delito= Delito.getDelitos()[int(cbox_codigo.get())]
            prisionero.agregarDelito(delito)
            tk.messagebox.showinfo(message="El delito " + cbox_codigo.get()+" ha sido agregado al prisionero "+ cbox_identificacion.get()+ " correctamente")
            self.salir() 

        def cancelar():
            self.salir()

        fuente="Helvetica 10 bold"
        btn_aceptar = tk.Button(frm_agregar, text="Aceptar", font=fuente, command= func_agregarDelito)
        btn_aceptar.grid(column=0, row=5, padx=15, pady=15)
        btn_cancelar = tk.Button(frm_agregar, text="Cancelar", font=fuente, command= cancelar)
        btn_cancelar.grid(column=1, row=5, padx=15, pady=15)

        frm_agregar.pack(expand=True, padx=30)
        self.currFrame = frm_agregarDelito
        frm_agregarDelito.pack()

    def agregarAntidelito(self):
        self.currFrame.pack_forget()

        frm_agregarAntidelito=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_agregarAntidelito)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Agregar Antidelito", font=('Arial', 15))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_agregarAntidelito, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso, text="Seleccione la identificación del prisionero y el código del delito que desea agregar", font=('Arial', 10))
        lbl_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        frm_agregar=tk.Frame(frm_agregarAntidelito, borderwidth=1, relief="solid")

        prisioneros=[k for (k,v) in Prisionero.getPrisioneros().items()]
        antidelitos=[k for (k,v) in Antidelito.getAntidelitos().items()]

        tk.Label(frm_agregar, text="Identificación: ").grid(column=0, row=1, padx=15, pady=5)
        cbox_identificacion=ttk.Combobox(frm_agregar, values=prisioneros, justify=tk.CENTER, state="readonly")
        cbox_identificacion.grid(column=1,row=1,padx=15,pady=5) 

        tk.Label(frm_agregar, text="Código: ").grid(column=0, row=2, padx=15, pady=5)
        cbox_codigo=ttk.Combobox(frm_agregar, values=antidelitos, justify=tk.CENTER, state="readonly")
        cbox_codigo.grid(column=1,row=2,padx=15,pady=5)  

        def func_agregarAntidelito():
            prisionero= Prisionero.getPrisioneros()[int(cbox_identificacion.get())]
            antidelito= Antidelito.getAntidelitos()[int(cbox_codigo.get())]
            prisionero.agregarAntidelito(antidelito)
            tk.messagebox.showinfo(message="El antidelito " + cbox_codigo.get()+" ha sido agregado al prisionero "+ cbox_identificacion.get()+ " correctamente")
            self.salir() 

        def cancelar():
            self.salir()     

        fuente="Helvetica 10 bold"
        btn_aceptar = tk.Button(frm_agregar, text="Aceptar", font=fuente, command= func_agregarAntidelito)
        btn_aceptar.grid(column=0, row=5, padx=15, pady=15)
        btn_cancelar = tk.Button(frm_agregar, text="Cancelar", font=fuente, command= cancelar)
        btn_cancelar.grid(column=1, row=5, padx=15, pady=15)

        frm_agregar.pack(expand=True, padx=30)
        self.currFrame = frm_agregarAntidelito
        frm_agregarAntidelito.pack()

    def listarPrisionero(self):
        self.currFrame.pack_forget()

        frm_listaPrisioneros=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_listaPrisioneros)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10,pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Lista de Prisioneros", font=('Arial', 13, 'bold'))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_listaPrisioneros, borderwidth=2, relief="solid", padx=10)
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descipcion_proceso=tk.Label(frm_descripcion_proceso, text="A continuación podrá ver todos los prisioneros que se encuentran recluidos en la cárcel",
        font=('Arial',10))
        lbl_descipcion_proceso.pack(pady=10)

        container=ttk.Frame(frm_listaPrisioneros, borderwidth=1, relief="solid")
        colores=["gray70", "white"]
        canvas=Canvas(container, width=550, height=250)
        scrollbar=ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar_frame=ttk.Frame(canvas)

        scrollbar_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0,0), window=scrollbar_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for pri in Prisionero.getPrisioneros().values():
            currLabel=Label(scrollbar_frame, background=colores[0], text=pri, width=80)
            colores.append(colores.pop(0))
            currLabel.pack(fill=tk.X)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.currFrame=frm_listaPrisioneros
        frm_listaPrisioneros.pack()

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()