import tkinter as tk


class FieldFrame(tk.Frame):

    def __init__(   self, window, tituloCriterios, criterios, tituloValores, 
                    valores, habilitado, tituloProceso, descripcionProceso):
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
        lbl_titulo_proceso.pack(side=tk.TOP, pady= 10)
        
        frm_descripcion_proceso = tk.Frame(self, borderwidth=2, relief="solid")
        frm_descripcion_proceso.pack(fill=tk.X, padx=10)
        lbl_descripcion_proceso = tk.Label(frm_descripcion_proceso, text=descripcionProceso)
        lbl_descripcion_proceso.pack(pady= 10)

        frm_formulario = tk.Frame(self, borderwidth=1, relief="solid", padx=100, pady=10)
        
        fuente = "Helvetica 10 bold"
        lbl_titulo_criterio = tk.Label(frm_formulario, text=tituloCriterios, font= fuente)
        lbl_titulo_criterio.grid(column=0, row=0, padx=15, pady=15)
        lbl_titulo_criterio = tk.Label(frm_formulario, text=tituloValores, font= fuente)
        lbl_titulo_criterio.grid(column=1, row=0, padx=15, pady=15)
        
        self.entry_dict = {}
        row = 1
        for criterio, valor, habil in list(zip(criterios, valores, habilitado)):
            lbl_criterio = tk.Label(frm_formulario, text=criterio)
            lbl_criterio.grid(column=0, row=row, padx=15, pady=5)
            entry_valor = tk.Entry( frm_formulario, textvariable= tk.StringVar(value=valor),
                                    justify=tk.CENTER, state= habil)
            entry_valor.grid(column=1, row=row, padx=15, pady=5)
            self.entry_dict[criterio] = entry_valor

            row += 1

        # Botón Aceptar
        btn_aceptar = tk.Button(frm_formulario, text="Aceptar", font=fuente)
        btn_aceptar.grid(column=0, row=row, padx=15, pady=15)
        self.btn_aceptar = btn_aceptar
        btn_cancelar = tk.Button(frm_formulario, text="Borrar", font=fuente, command= self.funcBorrar)
        btn_cancelar.grid(column=1, row=row, padx=15, pady=15)

        frm_formulario.pack(expand=True, padx=30)

    def set_command_btn_aceptar(self, command):
        self.btn_aceptar.configure(command = command)

    def getValue(self, criterio: str):
        """[summary]

        Args:
            criterio (str): el criterio cuyo valor se quiere obtener

        Returns:
            str: el valor del criterio cuyo nombre es 'criterio'
        """
        criterio_valor = self.entry_dict[criterio].get()
        return criterio_valor

    def funcBorrar(self):
        for v in self.entry_dict.values():
            if v["state"] == "normal":
                v.delete(0,tk.END)
                v.insert(0,"")