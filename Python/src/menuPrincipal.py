from tkinter import *


class MenuPrincipal(Menu):

    def __init__(self, window) -> None:
        # Menu inicio
        super().__init__(window)
        window['menu'] = self

    def add_menu_options(self, label: str, options: list):
        # Menu inicio opciones
        menu_opciones = Menu()
        for label_option, command_option in options:
            menu_opciones.add_command(label=label_option, command=command_option)

        self.add_cascade(menu=menu_opciones, label=label)
    
