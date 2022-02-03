from tkinter import *
import tkinter as tk
from tkinter import Canvas, Label, ttk

from gestorAplicacion.prisionero import Prisionero
from .utils.menuBar import MenuBar
from .utils.fieldFrame import FieldFrame
from gestorAplicacion.guardian import Guardian
from gestorAplicacion.celda import Celda


class GestionarGuardian(tk.Toplevel):

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
        frmBase = tk.Frame(self)

        frm_titulo_proceso = tk.Frame(frmBase)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10 ,pady= 10)

        lbl_titulo_proceso = tk.Label(frm_titulo_proceso, text="Gestión de los Guardianes", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = tk.Frame(frmBase, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso,
        text= """En esta ventana tendrá la posibilidad de gestionar todos los aspectos
        relacionados con los guardianes en las instalaciones de la Cárcel Apuestera.""", 
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

    def ingresarGuardian(self):
        self.currFrame.pack_forget()
        frm_ingresarGuardian = tk.Frame(self)


        # Formulario --------------------------------------------------------------

        frm_inicial = FieldFrame(
            frm_ingresarGuardian,
            "Criterios",
            ["Código", "Nombre", "Saldo", "Salario", "Celdas"],
            "Valores",
            [str(len(Guardian.getGuardianes())+1001), "", "", "", ""],
            [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
            "Ingresar Guardian",
            "Registre los datos solicitados para ingresar al Guardian. \n"+
            "Para el campo 'Celdas', digite los números de celdas separados por espacio"
        )

        #RECORDAR Serializar
        def registro():
            from GUImain.exceptionClasses.exceptionValorNegativo import ExceptionValorNegativo

            celdas = frm_inicial.getValue("Celdas").split()
            dictceldas = {}
            for i in celdas:
                dictceldas[int(i)] = Celda.getCeldas()[int(i)]

            try:
                ExceptionValorNegativo("El saldo no puede ser negativo.", int(frm_inicial.getValue("Saldo")))
            except ExceptionValorNegativo as f:
                f.messbox()
                return

            Guardian(frm_inicial.getValue("Nombre"), int(frm_inicial.getValue("Saldo")), int(frm_inicial.getValue("Salario")), dictceldas)
            tk.messagebox.showinfo("Confirmación", "Se ha registrado el Guardian correctamente")
            self.salir()
        
        #Hacer excepcion 

        frm_inicial.set_command_btn_aceptar(registro)
        frm_inicial.pack(fill=tk.BOTH, expand=True)

        self.currFrame = frm_ingresarGuardian
        frm_ingresarGuardian.pack()

    def borrarGuardian(self):
        self.currFrame.pack_forget()
        frm_borrarGuardian = tk.Frame(self)

        frm_titulo_proceso = tk.Frame(frm_borrarGuardian)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10 ,pady= 10)

        lbl_titulo_proceso = tk.Label(frm_titulo_proceso, text="Borrar Guardian", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = tk.Frame(frm_borrarGuardian, borderwidth=2, relief="solid", padx= 10)
        frm_descripcion_proceso.pack(fill=tk.X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso,
        text= "A continuacón se mostrará una lista de los guardianes registrados en la carcel. \n"+
        "Seleccione un código de identificación del guardian que desea eliminar de la base de datos.", 
        font=('Arial', 10))
        lbl_descripcion_proceso.pack(pady= 10)


        # Formulario --------------------------------------------------------------

        frm_formulario = tk.Frame(frm_borrarGuardian, borderwidth=1, relief="solid")
        guardianes = [k for (k, v) in Guardian.getGuardianes().items()]
        tk.Label(frm_formulario, text= "Código Guardian: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigo = ttk.Combobox(frm_formulario, values=guardianes, justify=tk.CENTER)
        combox_codigo['state'] = 'readonly'
        combox_codigo.grid(column=1, row=1, padx=15, pady=5)

        def func_borrarGuardian():
            Guardian.getGuardianes().pop(int(combox_codigo.get()))
            tk.messagebox.showinfo("Confirmación", "Se ha eliminado al guardian " + combox_codigo.get() + " correctamente")
            self.salir()

        def func_cancelar():
            self.salir()    

        # Botones
        fuente = "Helvetica 10 bold"
        btn_aceptar = tk.Button(frm_formulario, text="Borrar", font=fuente, command= func_borrarGuardian)
        btn_aceptar.grid(column=0, row=2, padx=15, pady=15)
        btn_cancelar = tk.Button(frm_formulario, text="Cancelar", font=fuente, command= func_cancelar)
        btn_cancelar.grid(column=1, row=2, padx=15, pady=15)

        frm_formulario.pack(expand=True, padx=30)

        self.currFrame = frm_borrarGuardian
        frm_borrarGuardian.pack()

    def editarGuardian(self):
        global frm_principal
        self.currFrame.pack_forget()
        frm_editarGuardian = tk.Frame(self)


        # Formulario --------------------------------------------------------------
        
        frm_formulario = tk.Frame(frm_editarGuardian, borderwidth=1, relief="solid")
        guardianes = [k for (k, v) in Guardian.getGuardianes().items()]
        tk.Label(frm_formulario, text= "Código Guardian: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigo = ttk.Combobox(frm_formulario, values=guardianes, justify=tk.CENTER)
        combox_codigo['state'] = 'readonly'
        combox_codigo.grid(column=1, row=1, padx=15, pady=5)

        frm_formulario.pack(expand=True, padx=30)

        frm_principal = FieldFrame(
            frm_editarGuardian,
            "Criterios",
            ["Código", "Nombre", "Saldo", "Salario", "Celdas"],
            "Valores",
            ["", "", "", "", ""],
            [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
            "Editar Guardian",
            "Seleccione en la parte superior el código del guardian que desea modificar. \n" +
            "Modifique solo los campos que desea editar del guardian. \n" +
            "Para el campo 'Celdas', digite los números de celdas separados por espacio."
        )
        
        frm_principal.pack(fill=tk.BOTH, expand=True)

        #RECORDAR Serializar
        def registro():
            celdas = frm_principal.getValue("Celdas").split()
            dictceldas = {}
            for i in celdas:
                dictceldas[int(i)] = Celda.getCeldas()[int(i)]

            idenguard = combox_codigo.get()
            datosguardian = Guardian.getGuardianes()[int(idenguard)]

            datosguardian.setNombre(frm_principal.getValue("Nombre"))
            datosguardian.setSaldo(float(frm_principal.getValue("Saldo")))
            datosguardian.setSalario(float(frm_principal.getValue("Salario")))
            datosguardian.setCeldas(dictceldas)

            tk.messagebox.showinfo("Confirmación", "Se han modificado correctamente los datos del guardian seleccionado")
            self.salir()

        def fun_datguard(e):
            global frm_principal
            idenguard = combox_codigo.get()
            datosguardian = Guardian.getGuardianes()[int(idenguard)]

            celdas = [k for (k,v) in datosguardian.getCeldas().items()]
            textceldas = ""
            for i in celdas:
                textceldas += str(i) + " "

            frm_aux = FieldFrame(
                frm_editarGuardian,
                "Criterios",
                ["Código", "Nombre", "Saldo", "Salario", "Celdas"],
                "Valores",
                [str(datosguardian.getIdentificacion()), 
                datosguardian.getNombre(),
                str(datosguardian.getSaldo()), 
                str(datosguardian.getSalario()),
                textceldas],
                [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
                "Editar Guardian",
                "Seleccione en la parte superior el código del guardian que desea modificar. \n" +
                "Modifique solo los campos que desea editar del guardian. \n" +
                "Para el campo 'Celdas', digite los números de celdas separados por espacio"
            )

            frm_principal.pack_forget()
            frm_aux.pack(fill=tk.BOTH, expand=True)
            frm_principal = frm_aux
            frm_principal.set_command_btn_aceptar(registro)

        combox_codigo.bind("<<ComboboxSelected>>", fun_datguard)
        
        self.currFrame = frm_editarGuardian
        frm_editarGuardian.pack()

    def listarGuardian(self):
        self.currFrame.pack_forget()

        frm_listaGuardianes=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_listaGuardianes)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10,pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Lista de Guardianes", font=('Arial', 13, 'bold'))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_listaGuardianes, borderwidth=2, relief="solid", padx=10)
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descipcion_proceso=tk.Label(frm_descripcion_proceso, text="A continuación podrá ver todos los guardianes registrados en la cárcel",
        font=('Arial',10))
        lbl_descipcion_proceso.pack(pady=10)

        container=ttk.Frame(frm_listaGuardianes, borderwidth=1, relief="solid")
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

        for guardian in Guardian.getGuardianes().values():
            currLabel=Label(scrollbar_frame, background=colores[0], text=guardian, width=80)
            colores.append(colores.pop(0))
            currLabel.pack(fill=tk.X)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.currFrame=frm_listaGuardianes
        frm_listaGuardianes.pack()

    def trasladarPrisionero(self):
        self.currFrame.pack_forget()

        frm_traslaPrisonero = Frame(self)

        frm_titulo_proceso = Frame(frm_traslaPrisonero)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10 ,pady= 10)

        lbl_titulo_proceso = Label(frm_titulo_proceso, text="Trasladar Prisonero", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = Frame(frm_traslaPrisonero, borderwidth=2, relief="solid", padx= 10)
        frm_descripcion_proceso.pack(fill=X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso,
        text= "Traslade a un prisionero de una celda a otra.\n"+
        "Seleccione el guardian que realizará el traslado.\n"+
        "Luego seleccione al prisionero que desea trasladar de celda.\n"+
        "Por último seleccione una nueva celda compatible con el prisionero.", 
        font=('Arial', 10))
        lbl_descripcion_proceso.pack(pady= 10)

        # Formulario --------------------------------------------------------------

        frm_formulario = Frame(frm_traslaPrisonero, borderwidth=1, relief="solid")

        guardianes = [k for (k, v) in Guardian.getGuardianes().items()]
        tk.Label(frm_formulario, text= "Código Guardian: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigog = ttk.Combobox(frm_formulario, values=guardianes, justify=tk.CENTER)
        combox_codigog['state'] = 'readonly'
        combox_codigog.grid(column=1, row=1, padx=15, pady=5)

        prisioneros = [k for (k, v) in Prisionero.getPrisioneros().items()]
        tk.Label(frm_formulario, text= "Código Prisionero: ").grid(column=0, row=2, padx=15, pady=5)
        combox_codigop = ttk.Combobox(frm_formulario, values=prisioneros, justify=tk.CENTER)
        combox_codigop['state'] = 'readonly'
        combox_codigop.grid(column=1, row=2, padx=15, pady=5)

        Label(frm_formulario, text= "Número Celda: ").grid(column=0, row=3, padx=15, pady=5)
        combox_numcelda = ttk.Combobox(frm_formulario, justify=CENTER)
        combox_numcelda['state'] = 'readonly'
        combox_numcelda.grid(column=1, row=3, padx=15, pady=5)

        def getCeldas(e):
            global celdas 
            if int(combox_codigop.get()) in Prisionero.getPrisionerosMASCULINOS():
                celdas = []
                aux = Celda.getCeldasMASCULINAS()
                for i in aux:
                    if Celda.getCeldas()[i].getCapMax() > len(Celda.getCeldas()[i].getPrisioneros()):
                        celdas.append(i)
            else:
                celdas = []
                aux = Celda.getCeldasFEMENINAS()
                for i in aux:
                    if Celda.getCeldas()[i].getCapMax() > len(Celda.getCeldas()[i].getPrisioneros()):
                        celdas.append(i)
            combox_numcelda.set("")
            combox_numcelda["values"] = [i for i in celdas]

        combox_codigop.bind("<<ComboboxSelected>>", getCeldas)

        def func_traslaPrisionero():
            prisionero = Prisionero.getPrisioneros()[int(combox_codigop.get())]
            celda = Celda.getCeldas()[int(combox_numcelda.get())]
            guardian = Guardian.getGuardianes()[int(combox_codigog.get())]
            guardian.trasladarPrisionero(prisionero,celda)
            tk.messagebox.showinfo("Confirmación", "Se ha trasladado al prisionero " + combox_codigop.get() + " correctamente")
            self.salir()

        def func_cancelar():
            self.salir()

        # Botones
        fuente = "Helvetica 10 bold"
        btn_aceptar = tk.Button(frm_formulario, text="Aceptar", font=fuente, command= func_traslaPrisionero)
        btn_aceptar.grid(column=0, row=4, padx=15, pady=15)
        btn_cancelar = tk.Button(frm_formulario, text="Cancelar", font=fuente, command= func_cancelar)
        btn_cancelar.grid(column=1, row=4, padx=15, pady=15)

        frm_formulario.pack(expand=True, padx=30)

        self.currFrame = frm_traslaPrisonero
        frm_traslaPrisonero.pack()

    def listarTraslado(self):
        global container
        self.currFrame.pack_forget()

        frm_listaTraslados=tk.Frame(self)

        frm_titulo_proceso=tk.Frame(frm_listaTraslados)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10,pady=10)

        lbl_titulo_proceso=tk.Label(frm_titulo_proceso, text="Lista de Traslados", font=('Arial', 13, 'bold'))
        lbl_titulo_proceso.pack()

        frm_descripcion_proceso=tk.Frame(frm_listaTraslados, borderwidth=2, relief="solid", padx=10)
        frm_descripcion_proceso.pack(fill=tk.X, padx=10, pady=10)

        lbl_descipcion_proceso=tk.Label(frm_descripcion_proceso, text="Seleccione el código del guardian. \n"+
        "A continuación se mostrará el registro de traslados del guardian seleccionado.",
        font=('Arial',10))
        lbl_descipcion_proceso.pack(pady=10)

        frm_formulario = tk.Frame(frm_listaTraslados, borderwidth=1, relief="solid")
        guardianes = [k for (k, v) in Guardian.getGuardianes().items()]
        tk.Label(frm_formulario, text= "Código Guardian: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigo = ttk.Combobox(frm_formulario, values=guardianes, justify=tk.CENTER)
        combox_codigo['state'] = 'readonly'
        combox_codigo.grid(column=1, row=1, padx=15, pady=5)
        frm_formulario.pack(expand=True, padx=30)

        container=ttk.Frame(frm_listaTraslados, borderwidth=1, relief="solid")
        colores=["gray70", "white"]
        canvas=Canvas(container, width=550, height=230)
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

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def fun_listaTraslados(e):
            global container
            containeraux = ttk.Frame(frm_listaTraslados, borderwidth=1, relief="solid")
            colores = ["gray70", "white"]
            canvas = Canvas(containeraux, width=550, height=230)
            scrollbar=ttk.Scrollbar(containeraux, orient="vertical", command=canvas.yview)
            scrollbar_frame=ttk.Frame(canvas)

            scrollbar_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )
            canvas.create_window((0,0), window=scrollbar_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            for traslado in Guardian.getGuardianes()[int(combox_codigo.get())].listaTraslados():
                currLabel=Label(scrollbar_frame, background=colores[0], text=traslado, width=80)
                colores.append(colores.pop(0))
                currLabel.pack(fill=tk.X)

            container.pack_forget()
            containeraux.pack()
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            container = containeraux


        combox_codigo.bind("<<ComboboxSelected>>", fun_listaTraslados)

        self.currFrame=frm_listaTraslados
        frm_listaTraslados.pack()

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()