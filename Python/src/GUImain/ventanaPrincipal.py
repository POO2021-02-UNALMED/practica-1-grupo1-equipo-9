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
            "Fiel creyente de la disciplina como camino para el éxito.\n" +
            "Actualmente se encuentra adelantando sus estudios en Estadística e Ingeniería Mecánica.\n" +
            "Es un apasionado por el área del conocimiento en general.\n" +
            "Aficionado por la tecnología, especialmente el hardware sin dejar a un lado su amor por los deportes.\n",
            [
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "JP1.jpeg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "JP2.jpeg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "JP3.jpeg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "JP4.jpg")
            ]
        ),
        (
            "Alejandro",
            "Amante de la programación, y la matemática aplicada y pura.\n" +
            "Una persona disciplinada y comprometida con el estudio.",
            [
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "Alejo1.jpg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "Alejo2.jpg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "Alejo3.jpg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "Alejo4.jpg"),
            ]
        ),
        (
            "Valentina",
            "Estudiante de estadística, con gusto por las matemáticas.\n" +
            "Aficionada las artes marciales, con un continuo interés en el aprendizaje constante,\n" +
            "también disfruta de la resolución de problemas mediante el uso de la computación y las matemáticas.",
            [
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "V1.jpg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "V2.jpeg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "V3.jpeg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "V4.jpeg"),
            ]
        ),
        (
            "Camilo Rivera",
            "Estudiando de Ingeniería de Sistemas, con gusto por la seguridad de la información.",
            [
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "C1.jpeg"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "C3.png"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "dev1.png"),
                os.path.join(settings.BASE_DIR, "src",
                             "GUImain", "assets", "C2.png"),
            ]
        ),
    ]
    info_desarrolladores_iter = 1

    imagenes_sistema = [
        os.path.join(settings.BASE_DIR, "src",
                     "GUImain", "assets", "desc.png"),
        os.path.join(settings.BASE_DIR, "src",
                     "GUImain", "assets", "dev2.jpeg"),
    ]
    imagenes_sistema_iter = 1

    def __init__(self):
        super().__init__()
        self.diseno()
        self.crearContenido()
        self.crearMenu()
        self.btn_imagenes_sistema_event()
        self.btn_desarrolladores_event()
    

    def diseno(self):
        self.geometry("1080x480")
        self.option_add("*tearOff", False)
        self.title("Presentación")


    def crearContenido(self):

        # Frame left
        frm_p1 = tk.Frame(self, borderwidth=2, relief="solid")
        frm_p1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        frm_p3 = tk.Frame(frm_p1)
        frm_p3.pack(fill=tk.X)
        lbl_bienvenida = tk.Label(
            frm_p3, text="Bienvenidos \nSistema de apuestas en la carcel X")
        lbl_bienvenida.pack(fill=tk.BOTH, expand=True)

        frm_p4 = tk.Frame(frm_p1, borderwidth=2, relief="solid")
        frm_p4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        image_open = Image.open(self.imagenes_sistema[0]).resize((320, 320))
        img_sistema = ImageTk.PhotoImage(image_open)
        self.lbl_sistema = tk.Label(frm_p4, image=img_sistema)
        self.lbl_sistema.pack()
        self.lbl_sistema.bind("<Enter>", self.btn_imagenes_sistema_event)
        btn_sistema = tk.Button(frm_p4, text="Ingresar a sistema",
                                command=lambda: ventanaUsuario.VentanaUsuario(self))
        btn_sistema.pack()

        # Frame right
        frm_p2 = tk.Frame(self, borderwidth=2, relief="solid")
        frm_p2.pack(fill=tk.BOTH, expand=True)

        frm_p5 = tk.Frame(frm_p2)
        frm_p5.pack(fill=tk.X)
        self.var_desarrolladores = tk.StringVar()
        self.var_desarrolladores.set(
            f"""{self.info_desarrolladores[0][0]}\n""" +
            f"""{self.info_desarrolladores[0][1]}""")
        lbl_presentacion = tk.Label(
            frm_p5, textvariable=self.var_desarrolladores)
        lbl_presentacion.pack()
        lbl_presentacion.bind(
            "<ButtonPress-1>", self.btn_desarrolladores_event)

        frm_p6 = tk.Frame(frm_p2, borderwidth=2, relief="solid")
        frm_p6.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        row = 0
        col = 0
        self.lbl_image_list = []
        for i in range(4):
            image_open = Image.open(
                self.info_desarrolladores[0][2][i]).resize((180, 180))
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
            f"""{self.info_desarrolladores[self.info_desarrolladores_iter][0]}\n""" +
            f"""{self.info_desarrolladores[self.info_desarrolladores_iter][1]}"""
        )

        for i in range(4):
            image_open = Image.open(
                self.info_desarrolladores[self.info_desarrolladores_iter][2][i]).resize((180, 180))
            img_desarrolladores = ImageTk.PhotoImage(image_open)
            self.lbl_image_list[i].config(image=img_desarrolladores)
            self.lbl_image_list[i].photo_ref = img_desarrolladores

        self.info_desarrolladores_iter += 1

    def btn_imagenes_sistema_event(self, e=None):
        # Validación de iterador de lista de desarrollares
        if self.imagenes_sistema_iter >= len(self.imagenes_sistema):
            self.imagenes_sistema_iter = 0

        image_open = Image.open(
            self.imagenes_sistema[self.imagenes_sistema_iter]).resize((320, 320))
        img_sistema = ImageTk.PhotoImage(image_open)
        self.lbl_sistema.config(image=img_sistema)
        self.lbl_sistema.photo_ref = img_sistema

        self.imagenes_sistema_iter += 1

    def menu_descripcion_event(self, e=None):

        top_level_window = tk.Toplevel(self, width=100)
        top_level_window.geometry("380x380")
        top_level_window.title("Descripción")

        frm_descripcion = tk.Frame(top_level_window)
        frm_descripcion.pack(fill=tk.BOTH, expand=True)

        # Titulo
        lbl_tmp = tk.Label(
            frm_descripcion,
            text="Sistema de apuestas en la carcel X",
            padx=10,
            font=("Call of Ops Duty", 13)
        )
        lbl_tmp.pack(fill=tk.BOTH, expand=True)

        # Contenido
        description_text = """
        El dominio de nuestra aplicación se centra
        en un sistema de información
        sobre una cárcel muy particular.
        El gobernador (warden, en inglés) de esta cárcel
        administra todos los aspectos sobre los prisioneros,
        guardianes, celdas, etc.
        Lo que hace especial a esta cárcel,
        es que regularmente  se organizan eventos
        donde prisioneros pueden pelear entre sí,
        y los demás prisioneros
        y guardianes apuestan a un ganador.
        Todo este sistema de apuestas
        es administrado por el gobernador.
        """

        lbl_tmp = tk.Label(frm_descripcion, text=description_text, padx=10)
        lbl_tmp.pack(fill=tk.BOTH, expand=True)

        # Versión
        lbl_tmp = tk.Label(frm_descripcion, text="Versión V0.0.1", padx=10)
        lbl_tmp.pack(fill=tk.BOTH, expand=True)

        # btn_descripcion = tk.Button(frm_descripcion, text="Hola")
        # btn_descripcion.grid(column=0, row=0)

        # image_open_descripcion = Image.open(os.path.join(settings.BASE_DIR, "src", "GUImain", "assets", "desc.png")).resize((180, 180))
        # img_descripcion = ImageTk.PhotoImage(image_open_descripcion)
