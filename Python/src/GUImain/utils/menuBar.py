import tkinter as tk


class MenuBar(tk.Menu):

    def __init__(self, window) -> None:
        # Menu inicio
        super().__init__(window)
        window['menu'] = self

    def add_menu_options(self, label: str, options: list):
        # Menu inicio opciones
        menu_opciones = tk.Menu()
        for label_option, command_option in options:
            # Esto para poder colocar un segundo nivel de menu (submenus)
            if type(command_option) == list:
                menu_opciones_deep = tk.Menu()
                for label_option_deep, command_option_deep in command_option:
                    menu_opciones_deep.add_command(label=label_option_deep, command=command_option_deep)

                menu_opciones.add_cascade(menu=menu_opciones_deep, label=label_option)

            else:    
                menu_opciones.add_command(label=label_option, command=command_option)
        

        self.add_cascade(menu=menu_opciones, label=label)
    
