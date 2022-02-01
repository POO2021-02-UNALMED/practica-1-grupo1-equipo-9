import tkinter as tk
from .utils.menuBar import MenuBar
from .utils.fieldFrame import FieldFrame
from .utils.table import Table
from gestorAplicacion.pelea import Pelea
from gestorAplicacion.prisionero import Prisionero
from gestorAplicacion.genero import genero as genero_enum



class GestionarPelea(tk.Toplevel):

    def __init__(self, window: tk.Tk):
        super().__init__(window)
        self.MASTER = window

        self.disenno()
        self.crearMenu()
        self.frmInicial()

        window.iconify()


    def disenno(self):
        # self.geometry("650x400")
        self.option_add("*tearOff", False)
        self.title("Gestion de Peleas")


    def crearMenu(self):
        menubar = MenuBar(self)

        menuArchiv = [  ("Aplicación", self.evento),
                        ("Salir", self.salir) ]
        menubar.add_menu_options("Archivo", menuArchiv)
        
        menuProcyCons = [
            ("Registrar Pelea", [
                ("Ingresar", self.frm_registrar_pelea),
                ("Consultar código prisionero", self.deep_consultar_codigo_prisionero_event),
                ("Consultar armas disponibles", self.depp_consultar_armas_habilitadas_event)
            ]),
            ("Definir Pelea", self.definir_pelea), 
            ("Listar Peleas", self.listar_pelea),
            ("Battle Royale", self.battle_royale)
        ]

        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)


    def frmInicial(self):
        frmBase = tk.Frame(self)

        frm_titulo_proceso = tk.Frame(frmBase)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10 ,pady= 10)

        lbl_titulo_proceso = tk.Label(frm_titulo_proceso, text="Gestión de las Apuestas", font=('Arial', 15))
        lbl_titulo_proceso.pack()
        
        frm_descripcion_proceso = tk.Frame(frmBase, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10 ,pady= 10)

        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso,
        text= """Esta funcionalidad sirve para gestionar las peleas en cuanto al registro, a la visualización
        del estado de las peleas, a la creación de una pelea conjunta llamada BattleRoyale y a definir una pelea""", 
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


    def frm_registrar_pelea(self):
        
        self.currFrame.pack_forget()

        frm_registrarPelea = tk.Frame(self)

        self.frm_inicial = FieldFrame(
            frm_registrarPelea,
            "Criterios",
            ["Código", "Género(M/F)", "Código prisionero 1", "Código prisionero 2", "Arma 1", "Arma 2"],
            "Valores",
            ["", "", "", "", "", ""],
            [tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL, tk.NORMAL],
            "Ingresar Pelea",
            "Registre los datos de una pelea.\nPara este caso habilitamos un submenu para consultar los codigos de los prisioneros"
        )
        
        self.frm_inicial.set_command_btn_aceptar(self.registrar_pelea_event)
        self.frm_inicial.pack(fill=tk.BOTH, expand=True)

        self.currFrame = frm_registrarPelea
        frm_registrarPelea.pack()


    def registrar_pelea_event(self):
        codigo = self.frm_inicial.getValue("Código")
        genero = self.frm_inicial.getValue("Género(M/F)")
        codigo_prisionero1 = self.frm_inicial.getValue("Código prisionero 1")
        codigo_prisionero2 = self.frm_inicial.getValue("Código prisionero 2")
        arma1 = self.frm_inicial.getValue("Arma 1")
        arma2 = self.frm_inicial.getValue("Arma 2")

        # Validación de codigo de nueva pelea
        # TODO: Validar que el codigo de la nueva pelea no exista

        # Validación de que la letra ingresada sea la correcta
        if genero.lower() == "m":
            genero = genero_enum.M
        elif genero.lower() == "f":
            genero  = genero_enum.F
        else:
            # TODO: Mostrar el campo en el cual aparecio un error en un cuadro de dialogo
            pass

        # Validación del codigo de los prisioneros exista
        # TODO: Buscar en la lista de prisioneros a ver si los codigos existen
        prisionero1 = Prisionero.getPrisioneros()[int(codigo_prisionero1)]
        prisionero2 = Prisionero.getPrisioneros()[int(codigo_prisionero2)]

        # Validación de armas
        # TODO: Validar que las armas existan

        pelea = Pelea(codigo, genero, prisionero1, prisionero2, "arma10", "arma20")
        print(pelea)



    def definir_pelea(self):
        pass

    def listar_pelea(self):
        pass

    def battle_royale(self):
        pass
    
    def deep_consultar_codigo_prisionero_event(self):
        prisioneros = Prisionero.getPrisioneros()
        header = [
            "Código",
            "Género",
            "Inicio de condena",
            "Fin de condena"
        ]
        data = [header]
        for k, v in prisioneros.items():
            data.append(
                [
                    v.identificacion,
                    v.getGenero().value,
                    v.getInicioCondena(),
                    v.getFinCondena()
                ]
            )
        top_level_window = tk.Toplevel(self)
        tbl = Table(top_level_window, data)


    def depp_consultar_armas_habilitadas_event(self):
        pass

    def evento(self):
        print("click!")

    def salir(self):
        self.MASTER.deiconify()
        self.destroy()