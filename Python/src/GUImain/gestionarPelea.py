import tkinter as tk
from .utils.menuBar import MenuBar
from .utils.fieldFrame import FieldFrame
from .utils.fieldFrameWithEntryType import FieldFrameWithEntryType
from .utils.table import Table
from gestorAplicacion.celda import Celda
from gestorAplicacion.pelea import Pelea
from gestorAplicacion.prisionero import Prisionero
from gestorAplicacion.genero import genero as genero_enum
from GUImain.exceptionClasses.exceptionInconsistenciaGeneros import ErrorInconsistenciaGeneros
from tkinter import messagebox




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
                ("Ingresar", self.registrar_pelea_frm),
                ("Consultar código prisionero", self.deep_consultar_codigo_prisionero_event),
            ]),
            ("Definir Pelea", [
                ("Ingresar", self.definir_pelea_frm),
                ("Consultar código prisionero", self.deep_consultar_codigo_prisionero_event),
            ]), 
            ("Listar Peleas", self.listar_pelea_frm),
            ("Battle Royale", [
                ("Ingresar", self.battle_royale_frm),
                ("Consultar código celdas", self.deep_consultar_codigo_celdas_event),
            ])
        ]

        menubar.add_menu_options('Procesos y Consultas', menuProcyCons)


        menuAyuda = [ ("Acerca de", self.evento) ]
        menubar.add_menu_options("Ayuda", menuAyuda)


    def frmInicial(self):
        frmBase = tk.Frame(self)

        frm_titulo_proceso = tk.Frame(frmBase)
        frm_titulo_proceso.pack(side=tk.TOP, fill=tk.X, padx=10 ,pady= 10)

        lbl_titulo_proceso = tk.Label(frm_titulo_proceso, text="Gestión de las Peleas", font=('Arial', 15))
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


    def registrar_pelea_frm(self):
        
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
        from baseDatos.serializador import serializar
        from GUImain.exceptionClasses.exceptionCampoVacio import ExceptionCampoVacio
        from GUImain.exceptionClasses.exceptionObjNoEncontrado import ExceptionObjNoEncontrado

        codigo = self.frm_inicial.getValue("Código")
        genero = self.frm_inicial.getValue("Género(M/F)")
        codigo_prisionero1 = self.frm_inicial.getValue("Código prisionero 1")
        codigo_prisionero2 = self.frm_inicial.getValue("Código prisionero 2")
        arma1 = self.frm_inicial.getValue("Arma 1")
        arma2 = self.frm_inicial.getValue("Arma 2")

        try:
            ExceptionCampoVacio(
                codigo,
                genero,
                codigo_prisionero1,
                codigo_prisionero2,
                arma1,
                arma2
            )
        except ExceptionCampoVacio as f:
            f.messbox()
            return


        # Validación de codigo de nueva pelea
        # el codigo de la nueva pelea no debe existir
        try:        
            Pelea.getPeleas()[int(codigo)]
            messagebox.showinfo("Validación", f"El codigo {codigo} de la pelea no debe existir")
            return
        except KeyError:
            pass

        # Validación de que la letra ingresada sea la correcta
        if genero.lower() == "m":
            genero = genero_enum.M
        elif genero.lower() == "f":
            genero  = genero_enum.F
        else:
            # TODO: Mostrar el campo en el cual aparecio un error en un cuadro de dialogo
            pass

        # Validación del codigo de los prisioneros exista
        prisioneros = Prisionero.getPrisioneros()
        try:
            ExceptionObjNoEncontrado(f"No se encontró apostador con el ID: {int(codigo_prisionero1)}", 
                                        int(codigo_prisionero1), prisioneros)
            ExceptionObjNoEncontrado(f"No se encontró apostador con el ID: {int(codigo_prisionero1)}", 
                                        int(codigo_prisionero2), prisioneros)

        except ExceptionObjNoEncontrado as f:
            f.messbox()
            return
        
        prisionero1 = Prisionero.getPrisioneros()[int(codigo_prisionero1)]
        prisionero2 = Prisionero.getPrisioneros()[int(codigo_prisionero2)]
        
        # Validación para que el genero de los dos prisioneros sea el mismo
        try:
            ErrorInconsistenciaGeneros("El género de los luchadores debe ser el mismo.",
                                        prisionero1.getGenero(), prisionero2.getGenero())
        except ErrorInconsistenciaGeneros as f:
            f.messbox()                
            return

        # Validar que el genero de los prisioneros coincida con el de la pelea
        try:
            ErrorInconsistenciaGeneros(f"El género de la pelea es {genero.value}, por tanto el de los prisioneros también debe ser {genero.value}",
                                        prisionero1.getGenero(), genero)
        except ErrorInconsistenciaGeneros as f:
            f.messbox()                
            return

        # Validación de armas
        # TODO: Validar que las armas existan

        pelea = Pelea(codigo, genero, prisionero1, prisionero2, arma1, arma2)
        
        serializar()
        messagebox.showinfo("Confirmación", f"Se ha creado la pelea con Codigo: {pelea.getCodigo()}")


    def definir_pelea_frm(self):
        self.currFrame.pack_forget()

        frm_definirPelea = tk.Frame(self)

        self.frm_inicial = FieldFrame(
            frm_definirPelea,
            "Criterios",
            ["Código Pelea", "Identificación de prisionero ganador"],
            "Valores",
            ["", ""],
            [tk.NORMAL, tk.NORMAL],
            "Definir Pelea",
            "En esta funcionalidad se escoge arbitrariamente al ganador de una pelea"
        )
        
        self.frm_inicial.set_command_btn_aceptar(self.definir_pelea_event)
        self.frm_inicial.pack(fill=tk.BOTH, expand=True)

        self.currFrame = frm_definirPelea
        frm_definirPelea.pack()


    def definir_pelea_event(self):
        from baseDatos.serializador import serializar
        from GUImain.exceptionClasses.exceptionCampoVacio import ExceptionCampoVacio
        from GUImain.exceptionClasses.exceptionObjNoEncontrado import ExceptionObjNoEncontrado
        
        codigo_pelea = self.frm_inicial.getValue("Código Pelea")
        codigo_prisionero = self.frm_inicial.getValue("Identificación de prisionero ganador")

        try:
            ExceptionCampoVacio(codigo_pelea,
                                codigo_prisionero)
        except ExceptionCampoVacio as f:
            f.messbox()
            return

        # Buscar objetos Pelea y Prisionero
        peleas = Pelea.getPeleas()
        prisioneros = Prisionero.getPrisioneros()
        try:
            ExceptionObjNoEncontrado(f"No se encontró la pelea con el ID: {int(codigo_pelea)}", 
                                        int(codigo_pelea), peleas)
            ExceptionObjNoEncontrado(f"No se encontró apostador con el ID: {int(codigo_prisionero)}", 
                                        int(codigo_prisionero), prisioneros)

        except ExceptionObjNoEncontrado as f:
            f.messbox()
            return

        pelea = peleas[int(codigo_pelea)]
        ganador = prisioneros[int(codigo_prisionero)]

        pelea.setGanador(ganador)

        serializar()
        messagebox.showinfo("Confirmación", f"El ganador para la pelea con codigo [{codigo_pelea}] es el prisionero con el codigo [{codigo_prisionero}]")


    def listar_pelea_frm(self):
        self.currFrame.pack_forget()

        frm_registrarPelea = tk.Frame(self)

        peleas = Pelea.getPeleas()
        header = [
            "Código",
            "Género",
            "Luchador1",
            "Arma1",
            "Luchador2",
            "Arma2",
            "Ganador"
        ]
        data = [header]
        for k, v in peleas.items():
            luchador1, luchador2 = v.getLuchadores()
            data.append(
                [
                    v.getCodigo(),
                    v.getGenero().value,
                    f"({luchador1.identificacion}) {luchador1.getNombre()}",
                    v.getArmaLuchador1(),
                    f"({luchador2.identificacion}) {luchador2.getNombre()}",
                    v.getArmaLuchador2(),
                    "Aun no hay ganador" if not v.getGanador() else f"({v.getGanador().identificacion}) {v.getGanador().getNombre()}"
                ]
            )

        tbl = Table(frm_registrarPelea, data)

        self.currFrame = frm_registrarPelea
        frm_registrarPelea.pack()


    def listar_pelea_event(self):
        pass


    def battle_royale_frm(self):
        self.currFrame.pack_forget()

        frm_battleRoyale = tk.Frame(self)

        self.frm_inicial = FieldFrameWithEntryType(
            frm_battleRoyale,
            "Criterios",
            ["Género", "Codigos de celda a escoger (separadas por comas)"],
            "Valores",
            [[genero_enum.M.value, genero_enum.F.value], ""],
            [tk.READABLE, tk.NORMAL],
            [tk.ttk.Combobox, tk.Entry],
            "Battle Royale",
            "Lo prisioneros de los codigos de las celdas escogidas se enfrentan hasta que haya un solo ganados"
        )
        
        self.frm_inicial.set_command_btn_aceptar(self.battle_royale_event)
        self.frm_inicial.pack(fill=tk.BOTH, expand=True)

        self.currFrame = frm_battleRoyale
        frm_battleRoyale.pack()


    def battle_royale_event(self):
        from baseDatos.serializador import serializar
        from GUImain.exceptionClasses.exceptionCampoVacio import ExceptionCampoVacio
        
        genero = self.frm_inicial.getValue("Género")
        codigos_celdas = self.frm_inicial.getValue("Codigos de celda a escoger (separadas por comas)")

        try:
            ExceptionCampoVacio(genero,
                                codigos_celdas)
        except ExceptionCampoVacio as f:
            f.messbox()
            return


        # Procesar entrada codigos_celdas
        codigos_celdas = codigos_celdas.strip(",").strip(" ").replace(" ", "").split(",")

        # Buscar objetos de Celda
        celdas = Celda.getCeldas()
        celdas_escojidas = [celdas[int(i)] for i in codigos_celdas]
        
        # # Validar que todas las celdas sean del mismo genero
        # try:
        #     for celda in celdas_escojidas:
        #         ErrorInconsistenciaGeneros(f"El género de las celdas en el battlee royale deben ser {genero} {celda.getGenero().value}",
        #                                     str(celda.getGenero().value), str(genero))
                    
        # except ErrorInconsistenciaGeneros as f:
        #     f.messbox()                
        #     return

        # try:
        #     ErrorInconsistenciaGeneros("El género de la pelea es " + genero.value,
        #                                 prisionero1.getGenero(), genero)
        # except ErrorInconsistenciaGeneros as f:
        #     f.messbox()                
        #     return

        combates = Pelea.battleRoyale(celdas_escojidas)
        combates_msg = ""
        for c in combates:
            combates_msg += c + "\n"
        serializar()
        messagebox.showinfo("Confirmación", combates_msg)

    
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

    
    def deep_consultar_codigo_celdas_event(self):
        celdas = Celda.getCeldas()
        header = [
            "Código",
            "Género",
            "Largo",
            "Ancho",
            "Capacidad Máxima"
        ]
        data = [header]
        for k, v in celdas.items():
            data.append(
                [
                    v.getNumero(),
                    v.getGenero().value,
                    v.getLargo(),
                    v.getAncho(),
                    v.getCapMax()
                ]
            )
        top_level_window = tk.Toplevel(self)
        tbl = Table(top_level_window, data)


    def evento(self):
        messagebox.showinfo(title="Integrantes", 
        message="Beatriz Valentina Gomez Valencia \n"+
        "Alejandro Salazar Mejía \n"+
        "Juan Pablo Martínez Echavarría \n"+
        "Hernan Camilo Rivera Arteaga")


    def salir(self):
        self.MASTER.deiconify()
        self.destroy()