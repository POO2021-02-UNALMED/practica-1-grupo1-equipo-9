import os
from .utils import menuBar
import settings
import tkinter as tk
from PIL import Image, ImageTk
from . import ventanaUsuario


class VentanaPrincipal(tk.Tk):

    info_desarrolladores = [
        (
            "Juan Martinez",
            "Descripción",
            [
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "JP1.jpeg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "JP2.jpeg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "JP3.jpeg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "JP4.jpg")
            ]
        ),
        (
            "Alejandro",
            "Descripción",
            [
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "Alejo1.jpg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "Alejo2.jpg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "Alejo3.jpg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "Alejo4.jpg"),
            ]
        ),
        (
            "Valentina",
            "Descripción",
            [
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "V1.jpg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "V2.jpeg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "V3.jpeg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "V4.jpeg"),
            ]
        ),
        (
            "Camilo Rivera",
            "Descripción",
            [
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev1.png"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev2.jpeg"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev1.png"),
                os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev2.jpeg"),
            ]
        ),
    ]
    info_desarrolladores_iter = 1

    imagenes_sistema = [
        os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev1.png"),
        os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "dev2.jpeg")
    ]
    imagenes_sistema_iter = 1

    def __init__(self):
        super().__init__()
        self.crearContenido()
        self.btn_imagenes_sistema_event()
        self.btn_desarrolladores_event()

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
        frm_p2.pack(fill=tk.BOTH, expand=True)

        frm_p5 = tk.Frame(frm_p2)
        frm_p5.pack(fill=tk.X)
        self.var_desarrolladores = tk.StringVar()
        self.var_desarrolladores.set(
            f"""{self.info_desarrolladores[0][0]}\n"""+
            f"""{self.info_desarrolladores[0][1]}""")
        lbl_presentacion = tk.Label(frm_p5, textvariable=self.var_desarrolladores)
        lbl_presentacion.pack()
        lbl_presentacion.bind("<ButtonPress-1>", self.btn_desarrolladores_event)

        frm_p6 = tk.Frame(frm_p2, borderwidth=2, relief="solid")
        frm_p6.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        row = 0
        col = 0
        self.lbl_image_list = []
        for i in range(4):
            image_open = Image.open(self.info_desarrolladores[0][2][i]).resize((180, 180))
            img_desarrolladores = ImageTk.PhotoImage(image_open)

            lbl_tmp = tk.Label(frm_p6, image=img_desarrolladores)
            self.lbl_image_list.append(lbl_tmp)
            
            lbl_tmp.grid(column=col, row=row)
            if row == 0 and col == 0:
                col = 1
            elif row == 0 and col == 1:
                row = 1
                col = 0
            else:
                col = 1



    def crearMenu(self):
        menu_principal = menuBar.MenuBar(self)
        # Menu Inicio
        menu_opciones = [
            ("Descripción", self.menu_descripcion_event),
            ("Salir", self.quit),
        ]
        menu_principal.add_menu_options("Inicio", menu_opciones)


    # Button events
    def btn_desarrolladores_event(self, e=None):
        # Validación de iterador de lista de desarrollares
        if self.info_desarrolladores_iter >= len(self.info_desarrolladores):
            self.info_desarrolladores_iter = 0

        self.var_desarrolladores.set(
            f"""{self.info_desarrolladores[self.info_desarrolladores_iter][0]}\n"""+
            f"""{self.info_desarrolladores[self.info_desarrolladores_iter][1]}"""
        )

        for i in range(4):
            image_open = Image.open(self.info_desarrolladores[self.info_desarrolladores_iter][2][i]).resize((180, 180))
            img_desarrolladores = ImageTk.PhotoImage(image_open)
            self.lbl_image_list[i].config(image=img_desarrolladores)
            self.lbl_image_list[i].photo_ref = img_desarrolladores

        self.info_desarrolladores_iter += 1


    def btn_imagenes_sistema_event(self, e=None):
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