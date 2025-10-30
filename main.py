

import tkinter as tk
from tkinter import ttk, messagebox
from turing_machine import TuringMachine


class SimuladorTuring:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Simulador de Maquina de Turing")
        self.raiz.geometry("700x400")
        self.raiz.configure(bg="#F0F0F0")

        # ======== CONFIGURACION BASICA DE LA MAQUINA ========
        self.estados = {"q0", "q1"}
        self.alfabeto = {"0", "1"}


        self.transiciones = {
    ("q0", "1"): ("q1", "1", "R"),
    ("q1", "1"): ("q0", "1", "R"),
    ("q0", "0"): ("q0", "0", "R"),


    ("q1", "0"): ("q1", "0", "R"),
    ("q0", "_"): ("q0", "_", "S"),  
    ("q1", "_"): ("q1", "_", "S")   
    }

        self.estado_inicial = "q0"
        self.estados_aceptacion = {"q0"}

        self.maquina = TuringMachine(
            self.estados, self.alfabeto, self.transiciones,
            self.estado_inicial, self.estados_aceptacion
        )

        # ELEMENTOS DE LA INTERFAZ 
        self.crear_interfaz()

    # ---------------------------------------------------
    def crear_interfaz(self):
       
       
        titulo = tk.Label(self.raiz, text="Simulador de Máquina de Turing", 
                          font=("Arial", 16, "bold"), bg="#F0F0F0")
        titulo.pack(pady=10)

       
        marco_entrada = tk.Frame(self.raiz, bg="#F0F0F0")
        marco_entrada.pack(pady=10)

        tk.Label(marco_entrada, text="Cadena de entrada:", bg="#F0F0F0").pack(side="left", padx=5)
        self.entrada_cadena = tk.Entry(marco_entrada, width=30)
        self.entrada_cadena.pack(side="left", padx=5)

        tk.Button(marco_entrada, text="Cargar", command=self.cargar_cadena).pack(side="left", padx=5)

        
        self.canvas = tk.Canvas(self.raiz, width=650, height=100, bg="white", relief="sunken")
        self.canvas.pack(pady=20)

        
        marco_botones = tk.Frame(self.raiz, bg="#F0F0F0")
        marco_botones.pack(pady=10)

        tk.Button(marco_botones, text="▶ Ejecutar todo", command=self.ejecutar_toda).pack(side="left", padx=10)
        tk.Button(marco_botones, text="⏭ Paso a paso", command=self.ejecutar_paso).pack(side="left", padx=10)
        tk.Button(marco_botones, text="🔄 Reiniciar", command=self.reiniciar).pack(side="left", padx=10)

        
        self.lbl_estado = tk.Label(self.raiz, text="Estado actual: q0", font=("Arial", 12), bg="#F0F0F0")
        self.lbl_estado.pack(pady=5)

       
        self.lbl_resultado = tk.Label(self.raiz, text="", font=("Arial", 12, "bold"), bg="#F0F0F0")
        self.lbl_resultado.pack(pady=5)

    # ---------------------------------------------------
    def dibujar_cinta(self):
        
        self.canvas.delete("all")
        x = 20
        y = 40
        tamaño = 40

        for i, simbolo in enumerate(self.maquina.cinta):
            color = "lightblue" if i == self.maquina.posicion_cabezal else "white"
            self.canvas.create_rectangle(x, y, x + tamaño, y + tamaño, outline="black", fill=color)
            self.canvas.create_text(x + tamaño / 2, y + tamaño / 2, text=simbolo, font=("Arial", 14))
            x += tamaño

        
        cabeza_x = 20 + self.maquina.posicion_cabezal * tamaño + tamaño / 2
        self.canvas.create_polygon(
            cabeza_x - 5, 30, cabeza_x + 5, 30, cabeza_x, 15, fill="red"
        )

    # ---------------------------------------------------
    def cargar_cadena(self):
       
        cadena = self.entrada_cadena.get().strip()
        if not cadena:
            messagebox.showwarning("Aviso", "Debe ingresar una cadena para procesar.")
            return
        self.maquina.cargar_cadena(cadena)
        self.lbl_estado.config(text=f"Estado actual: {self.maquina.estado_actual}")
        self.lbl_resultado.config(text="")
        self.dibujar_cinta()

    # ---------------------------------------------------
    def ejecutar_paso(self):
        paso_realizado = self.maquina.paso()
        self.dibujar_cinta()

        if self.maquina.detener:
       
            self.lbl_estado.config(text=f"Estado actual: {self.maquina.estado_actual}")
            self.mostrar_resultado()
        

        else:
            self.lbl_estado.config(text=f"Estado actual: {self.maquina.estado_actual}")

    # ---------------------------------------------------
    def ejecutar_toda(self):
        
        self.maquina.ejecutar_toda()
        self.dibujar_cinta()
        self.mostrar_resultado()

    # ---------------------------------------------------
    def mostrar_resultado(self):
       
        if self.maquina.aceptada:
            self.lbl_resultado.config(text="✅ Cadena aceptada", fg="green")
        else:
            self.lbl_resultado.config(text="❌ Cadena rechazada", fg="red")

    # ---------------------------------------------------
    def reiniciar(self):
        
        self.maquina.resetear()
        self.entrada_cadena.delete(0, tk.END)
        self.canvas.delete("all")
        self.lbl_estado.config(text="Estado actual: q0")
        self.lbl_resultado.config(text="")



# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    raiz = tk.Tk()
    app = SimuladorTuring(raiz)
    raiz.mainloop()
