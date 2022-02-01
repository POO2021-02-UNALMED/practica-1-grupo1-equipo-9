import os
from .utils import menuBar
import settings
import tkinter as tk
from PIL import Image, ImageTk
from . import ventanaUsuario


class VentanaPrincipal(tk.Tk):

    info_desarrolladores = [
        ("Desarrollador Uno", "Desarrollador Backed", "2 mes", os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev1.png")),
        ("Desarrollador Dos", "UI/UX", "1 mes", os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev2.jpeg")),
    ]
    info_desarrolladores_iter = 1

    imagenes_sistema = [
        os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev1.png"),
        os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev2.jpeg")
    ]
    imagenes_sistema_iter = 1

    def crearContenido(self):
        self.geometry("850x400")
        self.option_add("*tearOff", False)
        self.title("Presentación")

        self.crearMenu()

        # Frame left
        frm_p1 = tk.Frame(self, borderwidth=2, relief="solid")
        frm_p1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        frm_p3 = tk.Frame(frm_p1)
        frm_p3.pack(fill=tk.X)
        lbl_bienvenida = tk.Label(frm_p3, text="Bienvenidos \nSistema de apuestas en la carcel X")
        lbl_bienvenida.pack(fill=tk.BOTH, expand=True)

        frm_p4 = tk.Frame(frm_p1, borderwidth=2, relief="solid")
        frm_p4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        image_open = Image.open(self.imagenes_sistema[0]).resize((320,320))
        img_sistema = ImageTk.PhotoImage(image_open)
        self.lbl_sistema = tk.Label(frm_p4, image=img_sistema)
        self.lbl_sistema.pack()
        self.lbl_sistema.bind("<Enter>", self.btn_imagenes_sistema_event)
        btn_sistema = tk.Button(frm_p4, text="Ingresar a sistema", command= lambda: ventanaUsuario.VentanaUsuario(self))
        btn_sistema.pack()

        # Frame right
        frm_p2 = tk.Frame(self, borderwidth=2, relief="solid")
        frm_p2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        frm_p5 = tk.Frame(frm_p2)
        frm_p5.pack(fill=tk.X)
        self.var_desarrolladores = tk.StringVar()
        self.var_desarrolladores.set(f"""Nombre: {self.info_desarrolladores[0][0]}
        Cargo: {self.info_desarrolladores[0][1]}
        Experiencia: {self.info_desarrolladores[0][2]}""")
        lbl_presentacion = tk.Label(frm_p5, textvariable=self.var_desarrolladores)
        lbl_presentacion.pack()
        lbl_presentacion.bind("<ButtonPress-1>", self.btn_desarrolladores_event)

        frm_p6 = tk.Frame(frm_p2, borderwidth=2, relief="solid")
        frm_p6.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        image_open = Image.open(self.info_desarrolladores[0][3]).resize((360,360))
        img_desarrolladores = ImageTk.PhotoImage(image_open)
        self.lbl_image = tk.Label(frm_p6, image=img_desarrolladores)
        self.lbl_image.pack(fill=tk.BOTH, expand=True)


    def crearMenu(self):
        menu_principal = menuBar.MenuBar(self)
        # Menu Inicio
        menu_opciones = [
            ("Descripción", self.menu_descripcion_event),
            ("Salir", self.quit),
        ]
        menu_principal.add_menu_options("Inicio", menu_opciones)


    # Button events
    def btn_desarrolladores_event(self, e):
        # Validación de iterador de lista de desarrollares
        if self.info_desarrolladores_iter >= len(self.info_desarrolladores):
            self.info_desarrolladores_iter = 0

        self.var_desarrolladores.set(
            f"""Nombre: {self.info_desarrolladores[self.info_desarrolladores_iter][0]}
        Cargo: {self.info_desarrolladores[self.info_desarrolladores_iter][1]}
        Experiencia: {self.info_desarrolladores[self.info_desarrolladores_iter][2]}""")

        image_open = Image.open(self.info_desarrolladores[self.info_desarrolladores_iter][3]).resize((360,360))
        img_desarrolladores = ImageTk.PhotoImage(image_open)
        self.lbl_image.config(image=img_desarrolladores)
        self.lbl_image.photo_ref = img_desarrolladores

        self.info_desarrolladores_iter += 1


    def btn_imagenes_sistema_event(self, e):
        # Validación de iterador de lista de desarrollares
        if self.imagenes_sistema_iter >= len(self.imagenes_sistema):
            self.imagenes_sistema_iter = 0

        image_open = Image.open(self.imagenes_sistema[self.imagenes_sistema_iter]).resize((320,320))
        img_sistema = ImageTk.PhotoImage(image_open)
        self.lbl_sistema.config(image=img_sistema)
        self.lbl_sistema.photo_ref = img_sistema

        self.imagenes_sistema_iter += 1

    def menu_descripcion_event(self):
        print("Descripción")

    def opcion1(self):
        print("Opcion 1")

    def opcion2(self):
        print("Opcion 2")

    def opcion3(self):
        print("Opcion 3")

    def opcion4(self):
        print("Opcion 4")