import os
import tkinter as tk
from PIL import Image, ImageTk
from menuPrincipal import MenuPrincipal
import menuOpciones

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

info_desarrolladores = [
    ("Desarrollador Uno", "Desarrollador Backed", "2 mes", os.path.join(BASE_DIR, "src", "dev1.png")),
    ("Desarrollador Dos", "UI/UX", "1 mes", os.path.join(BASE_DIR, "src", "dev2.jpeg")),
]
info_desarrolladores_iter = 1

imagenes_sistema = [
    os.path.join(BASE_DIR, "src", "dev1.png"),
    os.path.join(BASE_DIR, "src", "dev2.jpeg")
]
imagenes_sistema_iter = 1

# Button events
def btn_desarrolladores_event(e):
    global var_desarrolladores, lbl_presentacion, info_desarrolladores, info_desarrolladores_iter

    # Validación de iterador de lista de desarrollares
    if info_desarrolladores_iter >= len(info_desarrolladores):
        info_desarrolladores_iter = 0

    var_desarrolladores.set(
        f"""Nombre: {info_desarrolladores[info_desarrolladores_iter][0]}
    Cargo: {info_desarrolladores[info_desarrolladores_iter][1]}
    Experiencia: {info_desarrolladores[info_desarrolladores_iter][2]}""")

    image_open = Image.open(info_desarrolladores[info_desarrolladores_iter][3]).resize((360,360))
    img_desarrolladores = ImageTk.PhotoImage(image_open)
    lbl_image.config(image=img_desarrolladores)
    lbl_image.photo_ref = img_desarrolladores

    info_desarrolladores_iter += 1


def btn_imagenes_sistema_event(e):
    global lbl_sistema, imagenes_sistema, imagenes_sistema_iter

    # Validación de iterador de lista de desarrollares
    if imagenes_sistema_iter >= len(imagenes_sistema):
        imagenes_sistema_iter = 0

    image_open = Image.open(imagenes_sistema[imagenes_sistema_iter]).resize((320,320))
    img_sistema = ImageTk.PhotoImage(image_open)
    lbl_sistema.config(image=img_sistema)
    lbl_sistema.photo_ref = img_sistema

    imagenes_sistema_iter += 1
    


# Window Making
window = tk.Tk()
window.geometry("850x400")
window.option_add("*tearOff", False)
window.title("Presentación")

menu_principal = MenuPrincipal(window)
# Menu Inicio
menu_opciones = [
    ("Descripción", menuOpciones.menu_descripcion_event),
    ("Salir", window.quit),
]
menu_principal.add_menu_options("Inicio", menu_opciones)

# Menu Dos para ejemplificar la creación de nuevos menus
menu_opciones = [
    ("Opcion 1", menuOpciones.opcion1),
    ("Opcion 2", menuOpciones.opcion2),
    ("Opcion 3", menuOpciones.opcion3),
    ("Opcion 4", menuOpciones.opcion4),
]
menu_principal.add_menu_options("Menu Dos", menu_opciones)


# Frame left
frm_p1 = tk.Frame(window, borderwidth=2, relief="solid")
frm_p1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frm_p3 = tk.Frame(frm_p1)
frm_p3.pack(fill=tk.X)
lbl_bienvenida = tk.Label(frm_p3, text="Bienvenidos \nSistema de apuestas en la carcel X")
lbl_bienvenida.pack(fill=tk.BOTH, expand=True)

frm_p4 = tk.Frame(frm_p1, borderwidth=2, relief="solid")
frm_p4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
image_open = Image.open(imagenes_sistema[0]).resize((320,320))
img_sistema = ImageTk.PhotoImage(image_open)
lbl_sistema = tk.Label(frm_p4, image=img_sistema)
lbl_sistema.pack()
lbl_sistema.bind("<Enter>", btn_imagenes_sistema_event)
btn_sistema = tk.Button(frm_p4, text="Ingresar a sistema")
btn_sistema.pack()



# Frame right
frm_p2 = tk.Frame(window, borderwidth=2, relief="solid")
frm_p2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

frm_p5 = tk.Frame(frm_p2)
frm_p5.pack(fill=tk.X)
var_desarrolladores = tk.StringVar()
var_desarrolladores.set(f"""Nombre: {info_desarrolladores[0][0]}
Cargo: {info_desarrolladores[0][1]}
Experiencia: {info_desarrolladores[0][2]}""")
lbl_presentacion = tk.Label(frm_p5, textvariable=var_desarrolladores)
lbl_presentacion.pack()
lbl_presentacion.bind("<ButtonPress-1>", btn_desarrolladores_event)

frm_p6 = tk.Frame(frm_p2, borderwidth=2, relief="solid")
frm_p6.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
image_open = Image.open(info_desarrolladores[0][3]).resize((360,360))
img_desarrolladores = ImageTk.PhotoImage(image_open)
lbl_image = tk.Label(frm_p6, image=img_desarrolladores)
lbl_image.pack(fill=tk.BOTH, expand=True)


# clicked = tk.StringVar() 
# clicked.set("Monday")

# drop_menu = tk.OptionMenu(frm_scene, clicked, "Monday", "Tuesday", "Wednesday")
# drop_menu.pack()



window.mainloop()