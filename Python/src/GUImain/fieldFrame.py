import tkinter as tk
from typing import Any, Literal


class FieldFrame(tk.Frame):

    def __init__(self, window, tituloCriterios, criterios, tituloValores, valores, habilitado, tituloProceso, descripcionProceso):
        """crea un nuevo objeto de tipo FieldFrame

        Args:
            tituloCriterios (str): titulo para la columna "Criterio"
            criterios (list): array con los nombres de los criterios
            tituloValores (str): titulo para la columna "valor"
            valores (list): array con los valores iniciales; Si ‘None’, no hay valores iniciales
            habilitado (list): array con los campos no-editables por el usuario; Si ‘None’, todos son editables
            tituloProceso (str):
            descripcionProceso (str):
        """
        super().__init__(window)
        lbl_titulo_proceso = tk.Label(self, text=tituloProceso)
        lbl_titulo_proceso.pack(side=tk.TOP)
        
        frm_descripcion_proceso = tk.Frame(self, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, expand=True)
        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso, text=descripcionProceso)
        lbl_descripcion_proceso.pack()

        frm_formulario = tk.Frame(self, borderwidth=1, relief="solid")
        frm_formulario.pack(fill=tk.BOTH, expand=True)
        lbl_titulo_criterio = tk.Label(frm_formulario, text=tituloCriterios)
        lbl_titulo_criterio.grid(column=0, row=0)
        lbl_titulo_criterio = tk.Label(frm_formulario, text=tituloValores)
        lbl_titulo_criterio.grid(column=1, row=0)
        
        row = 1
        for criterio, valor in list(zip(criterios, valores)):
            lbl_criterio = tk.Label(frm_formulario, text=criterio)
            lbl_criterio.grid(column=0, row=row)
            entry_valor = tk.Entry(frm_formulario)
            entry_valor.grid(column=1, row=row)

            row += 1

        # # Frame left
        # frm_p1 = tk.Frame(self, borderwidth=2, relief="solid")
        # frm_p1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # frm_p3 = tk.Frame(frm_p1)
        # frm_p3.pack(fill=tk.X)
        # lbl_bienvenida = tk.Label(frm_p3, text="Bienvenidos \nSistema de apuestas en la carcel X")
        # lbl_bienvenida.pack(fill=tk.BOTH, expand=True)

        # frm_p4 = tk.Frame(frm_p1, borderwidth=2, relief="solid")
        # frm_p4.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # image_open = Image.open(self.imagenes_sistema[0]).resize((320,320))
        # img_sistema = ImageTk.PhotoImage(image_open)
        # self.lbl_sistema = tk.Label(frm_p4, image=img_sistema)
        # self.lbl_sistema.pack()
        # self.lbl_sistema.bind("<Enter>", self.btn_imagenes_sistema_event)
        # btn_sistema = tk.Button(frm_p4, text="Ingresar a sistema", command= lambda: ventanaUsuario.VentanaUsuario(self))
        # btn_sistema.pack()



    def getValue(self, criterio: str):
        """[summary]

        Args:
            criterio (str): el criterio cuyo valor se quiere obtener

        Returns:
            [type]: el valor del criterio cuyo nombre es 'criterio'
        """
        return criterio