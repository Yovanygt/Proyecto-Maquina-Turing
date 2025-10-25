import tkinter as tk

ventana = tk.Tk()
ventana.title("Prueba de interfaz Tkinter")
ventana.geometry("300x150")

etiqueta = tk.Label(ventana, text="¡Tkinter está funcionando!", font=("Arial", 12))
etiqueta.pack(pady=40)

ventana.mainloop()
