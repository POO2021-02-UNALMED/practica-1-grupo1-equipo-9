from tkinter import *
import tkinter as tk
from tkinter import Canvas, Label, ttk
from .utils.menuBar import MenuBar
from tkinter import messagebox

from gestorAplicacion.antidelito import Antidelito
from .utils.fieldFrame import FieldFrame

class GestionarAntidelito(Toplevel):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()        
        self.frmInicial()

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

    def frmInicial(self):
        frmBase = tk.Frame(self)

        frm_titulo_proceso = tk.Frame(frmBase)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10 ,pady= 10)

        lbl_titulo_proceso = tk.Label(frm_titulo_proceso, text="Gestión de Antidelitos", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = tk.Frame(frmBase, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso,
        text= """En esta ventana tendrá la posibilidad de gestionar todos los aspectos
        relacionados con los Antidelitos.""", 
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

    def ingresarAntidelito(self):
        self.currFrame.pack_forget()
        frm_ingresarAntidelito = tk.Frame(self)


        # Formulario --------------------------------------------------------------

        frm_inicial = FieldFrame(
            frm_ingresarAntidelito,
            "Criterios",
            ["Código", "Nombre", "Descripción", "Rebaja de Condena"],
            "Valores",
            [str(len(Antidelito.getAntidelitos())+1), "", "", "", ""],
            [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
            "Ingresar Antidelito",
            "Registre los datos solicitados para ingresar un nuevo Antidelito."
        )

        #RECORDAR Serializar
        def registro():
            from GUImain.exceptionClasses.exceptionCampoVacio import ExceptionCampoVacio
            from GUImain.exceptionClasses.exceptionValorNegativo import ExceptionValorNegativo
            
            try:
                ExceptionCampoVacio(frm_inicial.getValue("Nombre"),
                                    frm_inicial.getValue("Descripción"),
                                    frm_inicial.getValue("Rebaja de Condena"))
            except ExceptionCampoVacio as f:
                f.messbox()
                return

            try:
                ExceptionValorNegativo("La rebaja de condena no puede ser negativa", int(frm_inicial.getValue("Rebaja de Condena"))) 
            except ExceptionValorNegativo as f:
                f.messbox()
                return

            Antidelito(frm_inicial.getValue("Nombre"), frm_inicial.getValue("Descripción"), int(frm_inicial.getValue("Rebaja de Condena")))
            tk.messagebox.showinfo("Confirmación", "Se ha registrado el Antidelito correctamente")
            self.salir()
        
        #Hacer excepcion 

        frm_inicial.set_command_btn_aceptar(registro)
        frm_inicial.pack(fill=tk.BOTH, expand=True)

        self.currFrame = frm_ingresarAntidelito
        frm_ingresarAntidelito.pack()

    def borrarAntidelito(self):
        self.currFrame.pack_forget()
        frm_borrarAntidelito = tk.Frame(self)

        frm_titulo_proceso = tk.Frame(frm_borrarAntidelito)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10 ,pady= 10)

        lbl_titulo_proceso = tk.Label(frm_titulo_proceso, text="Borrar Antidelito", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = tk.Frame(frm_borrarAntidelito, borderwidth=2, relief="solid", padx= 10)
        frm_descripcion_proceso.pack(fill=tk.X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso,
        text= "A continuacón se mostrará una lista de los Antidelitos registrados en la carcel. \n"+
        "Seleccione un código de identificación del Antidelito que desea eliminar de la base de datos.", 
        font=('Arial', 10))
        lbl_descripcion_proceso.pack(pady= 10)


        # Formulario --------------------------------------------------------------

        frm_formulario = tk.Frame(frm_borrarAntidelito, borderwidth=1, relief="solid")
        guardianes = [k for (k, v) in Antidelito.getAntidelitos().items()]
        tk.Label(frm_formulario, text= "Código Antidelito: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigo = ttk.Combobox(frm_formulario, values=guardianes, justify=tk.CENTER)
        combox_codigo['state'] = 'readonly'
        combox_codigo.grid(column=1, row=1, padx=15, pady=5)

        def func_borrarAntidelito():
            Antidelito.getAntidelitos().pop(int(combox_codigo.get()))
            tk.messagebox.showinfo("Confirmación", "Se ha eliminado el delito " + combox_codigo.get() + " correctamente")
            self.salir()

        def func_cancelar():
            self.salir()    

        # Botones
        fuente = "Helvetica 10 bold"
        btn_aceptar = tk.Button(frm_formulario, text="Borrar", font=fuente, command= func_borrarAntidelito)
        btn_aceptar.grid(column=0, row=2, padx=15, pady=15)
        btn_cancelar = tk.Button(frm_formulario, text="Cancelar", font=fuente, command= func_cancelar)
        btn_cancelar.grid(column=1, row=2, padx=15, pady=15)

        frm_formulario.pack(expand=True, padx=30)

        self.currFrame = frm_borrarAntidelito
        frm_borrarAntidelito.pack()

    def editarAntidelito(self):
        global frm_principal
        self.currFrame.pack_forget()
        frm_editarAntidelito = tk.Frame(self)


        # Formulario --------------------------------------------------------------
        
        frm_formulario = tk.Frame(frm_editarAntidelito, borderwidth=1, relief="solid")
        antidelitos = [k for (k, v) in Antidelito.getAntidelitos().items()]
        tk.Label(frm_formulario, text= "Código Antidelito: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigo = ttk.Combobox(frm_formulario, values=antidelitos, justify=tk.CENTER)
        combox_codigo['state'] = 'readonly'
        combox_codigo.grid(column=1, row=1, padx=15, pady=5)

        frm_formulario.pack(expand=True, padx=30)

        frm_principal = FieldFrame(
            frm_editarAntidelito,
            "Criterios",
            ["Código", "Nombre", "Descripción", "Rebaja de Condena"],
            "Valores",
            ["", "", "", ""],
            [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL],
            "Editar Antidelito",
            "Seleccione en la parte superior el código del antidelito que desea modificar. \n" +
            "Modifique solo los campos que desea editar del antidelito."
        )
        
        frm_principal.pack(fill=tk.BOTH, expand=True)

        #RECORDAR Serializar
        def registro():
            from GUImain.exceptionClasses.exceptionCampoVacio import ExceptionCampoVacio
            from GUImain.exceptionClasses.exceptionValorNegativo import ExceptionValorNegativo
            
            try:
                ExceptionCampoVacio(frm_principal.getValue("Nombre"),
                                    frm_principal.getValue("Descripción"),
                                    frm_principal.getValue("Rebaja de Condena"))
            except ExceptionCampoVacio as f:
                f.messbox()
                return

            try:
                ExceptionValorNegativo("La rebaja de condena no puede ser negativa", int(frm_principal.getValue("Rebaja de Condena"))) 
            except ExceptionValorNegativo as f:
                f.messbox()
                return  

            codAntidelito = combox_codigo.get()
            datosAntidelito = Antidelito.getAntidelitos()[int(codAntidelito)]

            datosAntidelito.setNombre(frm_principal.getValue("Nombre"))
            datosAntidelito.setDescripcion(frm_principal.getValue("Descripción"))
            datosAntidelito.setRebajaCondena(int(frm_principal.getValue("Rebaja de Condena")))

            tk.messagebox.showinfo("Confirmación", "Se han modificado correctamente los datos del antidelito seleccionado")
            self.salir()

        def fun_datanti(e):
            global frm_principal
            codAntidelito = combox_codigo.get()
            datosAntidelito = Antidelito.getAntidelitos()[int(codAntidelito)]

            frm_aux = FieldFrame(
                frm_editarAntidelito,
                "Criterios",
                ["Código", "Nombre", "Descripción", "Rebaja de Condena"],
                "Valores",
                [str(datosAntidelito.getCodigo()), 
                datosAntidelito.getNombre(),
                datosAntidelito.getDescripcion(), 
                str(datosAntidelito.getRebajaCondena())],
                [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL],
                "Editar Antidelito",
                "Seleccione en la parte superior el código del antidelito que desea modificar. \n" +
                "Modifique solo los campos que desea editar del antidelito."
            )

            frm_principal.pack_forget()
            frm_aux.pack(fill=tk.BOTH, expand=True)
            frm_principal = frm_aux
            frm_principal.set_command_btn_aceptar(registro)

        combox_codigo.bind("<<ComboboxSelected>>", fun_datanti)
        
        self.currFrame = frm_editarAntidelito
        frm_editarAntidelito.pack()

    def listarAntidelito(self):
        self.currFrame.pack_forget()

        frm_listaAntidelitos=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_listaAntidelitos)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10,pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Lista de Antidelitos", font=('Arial', 13, 'bold'))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_listaAntidelitos, borderwidth=2, relief="solid", padx=10)
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descipcion_proceso=tk.Label(frm_descripcion_proceso, text="A continuación podrá ver todos los Antidelitos registrados en la cárcel",
        font=('Arial',10))
        lbl_descipcion_proceso.pack(pady=10)

        container=ttk.Frame(frm_listaAntidelitos, borderwidth=1, relief="solid")
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

        for antidelito in Antidelito.getAntidelitos().values():
            currLabel=Label(scrollbar_frame, background=colores[0], text=antidelito, width=80)
            colores.append(colores.pop(0))
            currLabel.pack(fill=tk.X)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.currFrame=frm_listaAntidelitos
        frm_listaAntidelitos.pack()

    def evento(self):
        messagebox.showinfo(title="Integrantes", 
        message="Beatriz Valentina Gomez Valencia \n"+
        "Alejandro Salazar Mejía \n"+
        "Juan Pablo Martínez Echavarría \n"+
        "Hernan Camilo Rivera Arteaga")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()