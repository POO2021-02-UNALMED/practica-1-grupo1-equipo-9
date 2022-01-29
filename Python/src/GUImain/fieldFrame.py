import tkinter as tk


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
        frm_descripcion_proceso.pack(fill=tk.X, padx=10)
        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso, text=descripcionProceso)
        lbl_descripcion_proceso.pack()

        frm_formulario = tk.Frame(self, borderwidth=1, relief="solid")
        frm_formulario.pack(fill=tk.BOTH, expand=True, padx=30)
        lbl_titulo_criterio = tk.Label(frm_formulario, text=tituloCriterios)
        lbl_titulo_criterio.grid(column=0, row=0)
        lbl_titulo_criterio = tk.Label(frm_formulario, text=tituloValores)
        lbl_titulo_criterio.grid(column=1, row=0)
        
        self.entry_dict = {}
        row = 1
        for criterio, valor in list(zip(criterios, valores)):
            lbl_criterio = tk.Label(frm_formulario, text=criterio)
            lbl_criterio.grid(column=0, row=row)
            entry_valor = tk.Entry(frm_formulario)
            entry_valor.grid(column=1, row=row)
            self.entry_dict[criterio] = entry_valor

            row += 1

        btn_aceptar = tk.Button(frm_formulario, text="Aceptar")
        btn_aceptar.grid(column=0, row=row)
        btn_cancelar = tk.Button(frm_formulario, text="Cancelar")
        btn_cancelar.grid(column=1, row=row)



    def getValue(self, criterio: str):
        """[summary]

        Args:
            criterio (str): el criterio cuyo valor se quiere obtener

        Returns:
            str: el valor del criterio cuyo nombre es 'criterio'
        """
        criterio_valor = self.entry_dict[criterio].get()
        return criterio_valor