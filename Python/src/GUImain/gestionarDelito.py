from tkinter import *
import tkinter as tk
from tkinter import ttk
from .utils.menuBar import MenuBar
from .utils.fieldFrame import FieldFrame
from tkinter import messagebox
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
        self.geometry("700x550")
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
        from baseDatos.serializador import serializar

        self.currFrame.pack_forget()

        frm_ingresarDelito=tk.Frame(self)

        frm_ingresar=FieldFrame(frm_ingresarDelito, "Criterios", ["Código", "Nombre", "Descripción", "Nivel", "Tiempo Condena"], 
         "Valores", [str(len(Delito.getDelitos())+1), None, None, None, None, None], [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL], 
         "Ingresar Delito", "Ingrese los datos solicitados para registrar el delito" )

        def registro():
            from GUImain.exceptionClasses.exceptionCampoVacio import ExceptionCampoVacio
            from GUImain.exceptionClasses.exceptionValorNegativo import ExceptionValorNegativo
            from GUImain.exceptionClasses.exceptionNoInt import ExceptionNoInt

            try:
                ExceptionCampoVacio(frm_ingresar.getValue("Nombre"),
                                    frm_ingresar.getValue("Descripción"),
                                    frm_ingresar.getValue("Nivel"),
                                    frm_ingresar.getValue("Tiempo Condena"))
            except ExceptionCampoVacio as f:
                f.messbox()
                return

            try:
                ExceptionNoInt("El campo nivel debe ser un entero.", frm_ingresar.getValue("Nivel"))
            except ExceptionNoInt as f:
                f.messbox()
                return

            try:
                ExceptionValorNegativo("El nivel no puede ser negativo.", int(frm_ingresar.getValue("Nivel"))) 
            except ExceptionValorNegativo as f:
                f.messbox()
                return  

            try:
                ExceptionNoInt("El campo tiempo de condena debe ser un entero.", frm_ingresar.getValue("Tiempo Condena"))
            except ExceptionNoInt as f:
                f.messbox()
                return

            try:
                ExceptionValorNegativo("El tiempo de condena no puede ser negativo.", int(frm_ingresar.getValue("Tiempo Condena")))    
            except ExceptionValorNegativo as f:
                f.messbox()
                return

            Delito(frm_ingresar.getValue("Nombre"), frm_ingresar.getValue("Descripción"), int(frm_ingresar.getValue("Nivel")), int(frm_ingresar.getValue("Tiempo Condena")))
            serializar()
            tk.messagebox.showinfo(message="El delito ha sido registrado correctamente")
            self.salir()

        frm_ingresar.set_command_btn_aceptar(registro)
        frm_ingresar.pack(fill=tk.BOTH, expand=True)
        self.currFrame=frm_ingresarDelito
        frm_ingresarDelito.pack()

    def borrarDelito(self):
        from baseDatos.serializador import serializar
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
            warning= tk.messagebox.askyesno(message="¿Está seguro que desea eliminar el delito?")

            if warning:
                Delito.getDelitos().pop(int(cbox_codigo.get()))
                tk.messagebox.showinfo(message="El delito ha sido eliminado correctamente")
                serializar()
                self.salir()
            else:
                pass 

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
        global frm_principal
        from baseDatos.serializador import serializar
        
        self.currFrame.pack_forget()
        frm_editarDelito = tk.Frame(self)

        # Formulario --------------------------------------------------------------
        
        frm_formulario = tk.Frame(frm_editarDelito, borderwidth=1, relief="solid")
        antidelitos = [k for (k, v) in Delito.getDelitos().items()]
        tk.Label(frm_formulario, text= "Código Delito: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigo = ttk.Combobox(frm_formulario, values=antidelitos, justify=tk.CENTER)
        combox_codigo['state'] = 'readonly'
        combox_codigo.grid(column=1, row=1, padx=15, pady=5)

        frm_formulario.pack(expand=True, padx=30)

        frm_principal = FieldFrame(
            frm_editarDelito,
            "Criterios", 
            ["Código", "Nombre", "Descripción", "Nivel", "Tiempo Condena"], 
            "Valores", 
            ["", "", "", "", "", ""],
            [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
            "Editar Delito",
            "Seleccione en la parte superior el código del Delito que desea modificar. \n" +
            "Modifique solo los campos que desea editar del Delito.")
        
        frm_principal.pack(fill=tk.BOTH, expand=True)

        #RECORDAR Serializar
        def registro():
            from GUImain.exceptionClasses.exceptionCampoVacio import ExceptionCampoVacio
            from GUImain.exceptionClasses.exceptionValorNegativo import ExceptionValorNegativo
            from GUImain.exceptionClasses.exceptionNoInt import ExceptionNoInt
            
            try:
                ExceptionCampoVacio(frm_principal.getValue("Nombre"),
                                    frm_principal.getValue("Descripción"),
                                    frm_principal.getValue("Nivel"),
                                    frm_principal.getValue("Tiempo Condena"))
            except ExceptionCampoVacio as f:
                f.messbox()
                return

            try:
                ExceptionNoInt("El campo nivel debe ser un entero.", frm_principal.getValue("Nivel"))
            except ExceptionNoInt as f:
                f.messbox()
                return

            try:
                ExceptionValorNegativo("El nivel no puede ser negativo.", int(frm_principal.getValue("Nivel"))) 
            except ExceptionValorNegativo as f:
                f.messbox()
                return  

            try:
                ExceptionNoInt("El tiempo de condena debe ser un entero.", frm_principal.getValue("Tiempo Condena"))
            except ExceptionNoInt as f:
                f.messbox()
                return

            try:
                ExceptionValorNegativo("El tiempo de condena no puede ser negativo.", int(frm_principal.getValue("Tiempo Condena")))    
            except ExceptionValorNegativo as f:
                f.messbox()
                return


            Delito._delitos[int(combox_codigo.get())].setNombre(frm_principal.getValue("Nombre"))
            Delito._delitos[int(combox_codigo.get())].setDescripcion(frm_principal.getValue("Descripción"))
            Delito._delitos[int(combox_codigo.get())].setNivel(int(frm_principal.getValue("Nivel")))
            Delito._delitos[int(combox_codigo.get())].setTiempoCondena(int(frm_principal.getValue("Tiempo Condena")))
            serializar()
            tk.messagebox.showinfo(message="El delito ha sido editado correctamente")
            self.salir()

        def fun_datanti(e):
            global frm_principal
            codDelito = combox_codigo.get()
            datosDelito = Delito.getDelitos()[int(codDelito)]

            frm_aux = FieldFrame(
                frm_editarDelito,
                "Criterios", 
                ["Código", "Nombre", "Descripción", "Nivel", "Tiempo Condena"], 
                "Valores", 
                [str(datosDelito.getCodigo()),
                 datosDelito.getNombre(),
                 datosDelito.getDescripcion(),
                 datosDelito.getNivel(),
                 datosDelito.getTiempoCondena()],
                [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
                "Editar Delito",
                "Seleccione en la parte superior el código del Delito que desea modificar. \n" +
                "Modifique solo los campos que desea editar del Delito."
            )

            frm_principal.pack_forget()
            frm_aux.pack(fill=tk.BOTH, expand=True)
            frm_principal = frm_aux
            frm_principal.set_command_btn_aceptar(registro)

        combox_codigo.bind("<<ComboboxSelected>>", fun_datanti)
        
        self.currFrame = frm_editarDelito
        frm_editarDelito.pack()

    def listarDelito(self):
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
        canvas=Canvas(container, width=650, height=400)
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
            currLabel=Label(scrollbar_frame, background=colores[0], text=delito, width=95)
            colores.append(colores.pop(0))
            currLabel.pack(fill=tk.X)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.currFrame=frm_listaDelitos
        frm_listaDelitos.pack()

    def evento(self):
        messagebox.showinfo(title="Integrantes", 
        message="Beatriz Valentina Gomez Valencia \n"+
        "Alejandro Salazar Mejía \n"+
        "Juan Pablo Martínez Echavarría \n"+
        "Hernan Camilo Rivera Arteaga")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()