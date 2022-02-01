import tkinter as tk


class Table:

    def __init__(self, window, data: list):
        total_rows = len(data)
        total_columns = len(data[0])

        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = tk.Entry(
                    window,
                    width=20,
                    fg='blue',
                    font=('Arial', 16, 'bold'),
                    textvariable=tk.StringVar(value=data[i][j]),
                    state=tk.DISABLED
                )
                  
                self.e.grid(row=i, column=j)