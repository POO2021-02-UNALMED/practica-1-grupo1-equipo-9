from tkinter import *
import tkinter as tk
from tkinter import ttk
from .utils.menuBar import MenuBar
from .utils.fieldFrame import FieldFrame
from gestorAplicacion.delito import Delito

class GestionarDelito(Toplevel):

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

    def frmInicial(self):
        frmBase = tk.Frame(self)

        frm_titulo_proceso = tk.Frame(frmBase)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10 ,pady= 10)

        lbl_titulo_proceso = tk.Label(frm_titulo_proceso, text="Gestión de Delitos", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = tk.Frame(frmBase, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso,
        text= """En esta ventana tendrá la posibilidad de gestionar todos los aspectos
        relacionados con los Delitos.""", 
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

    def ingresarDelito(self):
        self.currFrame.pack_forget()

        frm_ingresarDelito=tk.Frame(self)

        frm_ingresar=FieldFrame(frm_ingresarDelito, "Criterios", ["Código", "Nombre", "Descripción", "Nivel", "Tiempo Condena"], 
         "Valores", [None, None, None, None, None, None], [tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL], 
         "Ingresar Delito", "Ingrese los datos solicitados para registrar el delito" )

        def registro():

            Delito(int(frm_ingresar.getValue("Código")), frm_ingresar.getValue("Nombre"), frm_ingresar.getValue("Descripción"), int(frm_ingresar.getValue("Nivel")), int(frm_ingresar.getValue("Tiempo Condena")))
            tk.messagebox.showinfo(message="El delito ha sido registrado correctamente")
            self.salir()

        frm_ingresar.set_command_btn_aceptar(registro)
        frm_ingresar.pack(fill=tk.BOTH, expand=True)
        self.currFrame=frm_ingresarDelito
        frm_ingresarDelito.pack()

    def borrarDelito(self):
        self.currFrame.pack_forget()

        frm_borrarDelito=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_borrarDelito)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Borrar Delito", font=('Arial', 15))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_borrarDelito, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso, text="Seleccione el código del Delito que desea eliminar", font=('Arial', 10))
        lbl_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        frm_borrar=tk.Frame(frm_borrarDelito, borderwidth=1, relief="solid")

        delitos=[k for (k,v) in Delito.getDelitos().items()]

        tk.Label(frm_borrar, text="Código: ").grid(column=0, row=1, padx=15, pady=5)
        cbox_codigo=ttk.Combobox(frm_borrar, values=delitos, justify=tk.CENTER, state="readonly")
        cbox_codigo.grid(column=1,row=1,padx=15,pady=5)


        def func_borrarDelito():

            tk.messagebox.askyesno(message="¿Está seguro que desea eliminar el delito?")

            if(False):
                self.salir()
            else:
                Delito.getDelitos().pop(int(cbox_codigo.get()))
                tk.messagebox.showinfo(message="El delito ha sido eliminado correctamente")
                self.salir() 


        def cancelar():
            self.salir()

        fuente="Helvetica 10 bold"
        btn_aceptar = tk.Button(frm_borrar, text="Aceptar", font=fuente, command= func_borrarDelito)
        btn_aceptar.grid(column=0, row=5, padx=15, pady=15)
        btn_cancelar = tk.Button(frm_borrar, text="Cancelar", font=fuente, command= cancelar)
        btn_cancelar.grid(column=1, row=5, padx=15, pady=15)

        frm_borrar.pack(expand=True, padx=30)
        self.currFrame = frm_borrarDelito
        frm_borrarDelito.pack()

    def editarDelito(self):
        pass

    def listarDelito(self):
        #agregar scroll horizontal
        self.currFrame.pack_forget()

        frm_listaDelitos=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_listaDelitos)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10,pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Lista de Delitos", font=('Arial', 13, 'bold'))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_listaDelitos, borderwidth=2, relief="solid", padx=10)
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descipcion_proceso=tk.Label(frm_descripcion_proceso, text="A continuación podrá ver todos los delitos registrados",
        font=('Arial',10))
        lbl_descipcion_proceso.pack(pady=10)

        container=ttk.Frame(frm_listaDelitos, borderwidth=1, relief="solid")
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

        for delito in Delito.getDelitos().values():
            currLabel=Label(scrollbar_frame, background=colores[0], text=delito, width=80)
            colores.append(colores.pop(0))
            currLabel.pack(fill=tk.X)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.currFrame=frm_listaDelitos
        frm_listaDelitos.pack()

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()