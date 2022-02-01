import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from click import command
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


        # Formulario --------------------------------------------------------------

        frm_inicial = FieldFrame(
            frm_ingresarGuardian,
            "Criterios",
            ["Código", "Nombre", "Saldo", "Salario", "Celdas"],
            "Valores",
            [str(len(Guardian.getGuardianes())+1001), "b", "", "", ""],
            [tk.DISABLED, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
            "Ingresar Guardian",
            "Registre los datos solicitados para ingresar al Guardian. \n"+
            "Para el campo 'Celdas', digite los números de celdas separados por espacio"
        )

        #RECORDAR Serializar
        def registro():
            celdas = frm_inicial.getValue("Celdas").split()
            dictceldas = {}
            for i in celdas:
                dictceldas[int(i)] = Celda.getCeldas()[int(i)]

            Guardian(frm_inicial.getValue("Nombre"), int(frm_inicial.getValue("Saldo")), int(frm_inicial.getValue("Salario")), dictceldas)
            messagebox.showinfo("Confirmación", "Se ha registrado el Guardian correctamente")
            self.salir()
        
        #Hacer excepcion 

        frm_inicial.set_command_btn_aceptar(registro)
        frm_inicial.pack(fill=tk.BOTH, expand=True)

        self.currFrame = frm_ingresarGuardian
        frm_ingresarGuardian.pack()

    def borrarGuardian(self):
        self.currFrame.pack_forget()
        frm_borrarGuardian = Frame(self)

        frm_titulo_proceso = Frame(frm_borrarGuardian)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10 ,pady= 10)

        lbl_titulo_proceso = Label(frm_titulo_proceso, text="Borrar Guardian", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = Frame(frm_borrarGuardian, borderwidth=2, relief="solid", padx= 10)
        frm_descripcion_proceso.pack(fill=X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso,
        text= "A continuacón se mostrará una lista de los guardianes registrados en la carcel. \n"+
        "Seleccione un código de identificación del guardian que desea eliminar de la base de datos.", 
        font=('Arial', 10))
        lbl_descripcion_proceso.pack(pady= 10)


        # Formulario --------------------------------------------------------------

        frm_formulario = Frame(frm_borrarGuardian, borderwidth=1, relief="solid")
        guardianes = [k for (k, v) in Guardian.getGuardianes().items()]
        Label(frm_formulario, text= "Código Guardian: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigo = ttk.Combobox(frm_formulario, values=guardianes, justify=CENTER)
        combox_codigo['state'] = 'readonly'
        combox_codigo.grid(column=1, row=1, padx=15, pady=5)

        def func_borrarGuardian():
            Guardian.getGuardianes().pop(int(combox_codigo.get()))
            messagebox.showinfo("Confirmación", "Se ha eliminado al guardian " + combox_codigo.get() + " correctamente")
            self.salir()

        def func_cancelar():
            self.salir()    

        # Botones
        fuente = "Helvetica 10 bold"
        btn_aceptar = Button(frm_formulario, text="Borrar", font=fuente, command= func_borrarGuardian)
        btn_aceptar.grid(column=0, row=2, padx=15, pady=15)
        btn_cancelar = Button(frm_formulario, text="Cancelar", font=fuente, command= func_cancelar)
        btn_cancelar.grid(column=1, row=2, padx=15, pady=15)

        frm_formulario.pack(expand=True, padx=30)

        self.currFrame = frm_borrarGuardian
        frm_borrarGuardian.pack()

    def editarGuardian(self):
        global frm_principal
        self.currFrame.pack_forget()
        frm_editarGuardian = Frame(self)


        # Formulario --------------------------------------------------------------
        
        frm_formulario = Frame(frm_editarGuardian, borderwidth=1, relief="solid")
        guardianes = [k for (k, v) in Guardian.getGuardianes().items()]
        Label(frm_formulario, text= "Código Guardian: ").grid(column=0, row=1, padx=15, pady=5)
        combox_codigo = ttk.Combobox(frm_formulario, values=guardianes, justify=CENTER)
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

        combox_codigo.bind("<<ComboboxSelected>>", fun_datguard)

        #RECORDAR Serializar
        def registro():
            celdas = frm_principal.getValue("Celdas").split()
            dictceldas = {}
            for i in celdas:
                dictceldas[int(i)] = Celda.getCeldas()[int(i)]

            #idenguard = combox_codigo.get()
            #datosguardian = Guardian.getGuardianes()[int(idenguard)]

            #datosguardian.setNombre(frm_principal.getValue("Nombre"))
            #datosguardian.setSaldo(int(frm_principal.getValue("Saldo")))
            #datosguardian.setSalario(int(frm_principal.getValue("Salario")))
            #datosguardian.setCeldas(dictceldas)

            messagebox.showinfo("Confirmación", "Se han modificado correctamente los datos del guardian seleccionado")
            self.salir()
        
        frm_principal.set_command_btn_aceptar(registro)
        
        self.currFrame = frm_editarGuardian
        frm_editarGuardian.pack()

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