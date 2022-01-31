from tkinter import *
from .menuBar import MenuBar
from tkinter import ttk


class GestionarApuesta(Toplevel):

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
        self.title("Gestion de Apuestas")

    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [   ("Ingresar Apostador", self.ingresarApostador),
                            ("Resultado Apuestas", self.resultadoApuestas)]

        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)

    def frmInicial(self):
        frmBase = Frame(self)

        frm_titulo_proceso = Frame(frmBase)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10 ,pady= 10)

        lbl_titulo_proceso = Label(frm_titulo_proceso, text="Gestión de las Apuestas", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = Frame(frmBase, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso,
        text= """En esta ventana tendrá la posibilidad de gestionar todos los aspectos
        relacionados con las apuestas organizadas en las instalaciones de la Cárcel Apuestera.""", 
        font=('Arial', 10))
        lbl_descripcion_proceso.pack(pady= 10)

        frm_formulario = Frame(frmBase, borderwidth=1, relief="solid")
        frm_formulario.pack(fill=X, pady= 10)
        lbl_formulario = Label(frm_formulario,
        text= """En el menú 'Procesos y Consultas' se encuentras las funcionalidades ofrecidas en este menú""", 
        font=('Arial', 10))
        lbl_formulario.pack(fill=X, padx=10 ,pady= 10)


        self.currFrame = frmBase
        frmBase.pack()

    def ingresarApostador(self):
        self.currFrame.pack_forget()

        frm_ingresarApostador = Frame(self)

        frm_titulo_proceso = Frame(frm_ingresarApostador)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10 ,pady= 10)

        lbl_titulo_proceso = Label(frm_titulo_proceso, text="Ingresar Apostador", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = Frame(frm_ingresarApostador, borderwidth=2, relief="solid", padx= 10)
        frm_descripcion_proceso.pack(fill=X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = Label(frm_descripcion_proceso,
        text= "Registra la apuesta de algún apostador (prisionero o guardián) a alguna pelea.\n"+
        "Primero ingrese el número de identificación del apostador que desea apostar.\n"+
        "Despúes seleccione la pelea a la que el apostador desea apostar.\n"+
        "Por último seleccione el peleador y el dinero apostado al peleador.", 
        font=('Arial', 10))
        lbl_descripcion_proceso.pack(pady= 10)

        frm_formulario = Frame(frm_ingresarApostador, borderwidth=1, relief="solid")

        Label(frm_formulario, text= "Identificación: ").grid(column=0, row=0, padx=15, pady=5)
        entry_Identificacion = Entry( frm_formulario, justify=CENTER)
        entry_Identificacion.grid(column=1, row=0, padx=15, pady=5)

        Label(frm_formulario, text= "Pelea: ").grid(column=0, row=1, padx=15, pady=5)
        combox_Pelea = ttk.Combobox(frm_formulario)
        combox_Pelea.grid(column=1, row=1, padx=15, pady=5)

        Label(frm_formulario, text= "Peleador: ").grid(column=0, row=2, padx=15, pady=5)
        combox_Peleador = ttk.Combobox(frm_formulario)
        combox_Peleador.grid(column=1, row=2, padx=15, pady=5)

        Label(frm_formulario, text= "Apuesta ($): ").grid(column=0, row=3, padx=15, pady=5)
        entry_Dinero = Entry( frm_formulario, justify=CENTER)
        entry_Dinero.grid(column=1, row=3, padx=15, pady=5)


        # Botones
        fuente = "Helvetica 10 bold"
        btn_aceptar = Button(frm_formulario, text="Aceptar", font=fuente, command= lambda: print("click"))
        btn_aceptar.grid(column=0, row=4, padx=15, pady=15)
        btn_cancelar = Button(frm_formulario, text="Borrar", font=fuente, command= lambda: print("click"))
        btn_cancelar.grid(column=1, row=4, padx=15, pady=15)


        frm_formulario.pack(expand=True, padx=30)


        self.currFrame = frm_ingresarApostador
        frm_ingresarApostador.pack()



    def resultadoApuestas(self):
        self.currFrame.pack_forget()

        frm_resultadoApuestas = Frame(self)

        frm_titulo_proceso = Frame(frm_resultadoApuestas)
        frm_titulo_proceso.pack(side=TOP, fill=X, padx=10 ,pady= 10)

        lbl_titulo_proceso = Label(frm_titulo_proceso, text="Resultado Apuestas", font=('Arial', 15))
        lbl_titulo_proceso.pack()

        
        self.currFrame = frm_resultadoApuestas
        frm_resultadoApuestas.pack()

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()