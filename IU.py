import tkinter as tk

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap('icon.ico')
        self.title('Detección de Somnolencia')
        # Configuración tamaño mínimo de la venta
        self.rowconfigure(0, minsize=600, weight=1)
        # Configuración mínima de la segunda columna
        self.columnconfigure(1, minsize=600, weight=1)
        # Atributo de campo de texto
        self.campo_video = tk.Frame()
        # Creación de componentes
        self._crear_componentes()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2,bg='black')
        boton_abrir = tk.Button(frame_botones, text='Iniciar')
        boton_guardar = tk.Button(frame_botones, text='Terminar')
        # Los botones los expandimos de manera horizontal (sticky='we')
        boton_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        # Se coloca el frame de manera vertical
        frame_botones.grid(row=0, column=0, sticky='ns')
        # Agregamos el campo de texto, se expandirá por completo el espacio disponible
        self.campo_video.grid(row=0, column=1, sticky='nswe')


if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()