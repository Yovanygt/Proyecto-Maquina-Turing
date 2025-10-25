"""
Descripción:
Esta clase representa el funcionamiento interno de una Máquina de Turing.
Aquí se define la cinta, el cabezal, los estados y las reglas de transición
que permiten movernos, escribir y cambiar de estado paso a paso.

Esta versión incluye una mejora para evitar errores cuando el cabezal
intenta moverse fuera de los límites de la cinta, agregando el símbolo
en blanco automáticamente.
"""

class TuringMachine:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion, simbolo_blanco="_"):
        # Conjunto de estados de la máquina (por ejemplo: q0, q1, q2)
        self.estados = estados

        # Alfabeto válido de símbolos (por ejemplo: 0, 1)
        self.alfabeto = alfabeto

        # Diccionario de transiciones: (estado, símbolo) → (nuevo_estado, símbolo_escrito, dirección)
        self.transiciones = transiciones

        # Estado desde el que empieza la ejecución
        self.estado_inicial = estado_inicial

        # Estados donde la cadena se considera aceptada
        self.estados_aceptacion = estados_aceptacion

        # Símbolo en blanco (por defecto es "_")
        self.simbolo_blanco = simbolo_blanco

        # Variables que cambian durante la ejecución
        self.resetear()

    # -------------------------------------------------------------------
    def resetear(self):
        """Reinicia la máquina para una nueva cadena."""
        self.cinta = []
        self.posicion_cabezal = 0
        self.estado_actual = self.estado_inicial
        self.detener = False
        self.aceptada = False

    # -------------------------------------------------------------------
    def cargar_cadena(self, cadena):
        """Carga la cadena en la cinta y coloca el cabezal en la primera posición."""
        self.resetear()
        # Cada símbolo de la cadena se guarda como una lista
        self.cinta = list(cadena)
        if len(self.cinta) == 0:
            self.cinta = [self.simbolo_blanco]
        self.posicion_cabezal = 0

    # -------------------------------------------------------------------
    def paso(self):
        """
        Ejecuta un solo paso de la máquina.
        Devuelve True si sigue funcionando, False si se detuvo.
        """
        if self.detener:
            return False  # Ya está detenida

        # Si el cabezal se sale del rango, se agregan símbolos en blanco
        if self.posicion_cabezal < 0:
            self.cinta.insert(0, self.simbolo_blanco)
            self.posicion_cabezal = 0
        elif self.posicion_cabezal >= len(self.cinta):
            self.cinta.append(self.simbolo_blanco)

        # Leer el símbolo actual bajo el cabezal
        simbolo_leido = self.cinta[self.posicion_cabezal]

        # Buscar transición correspondiente
        clave = (self.estado_actual, simbolo_leido)
        if clave not in self.transiciones:
            # No hay transición posible → detener
            self.detener = True
            return False

        # Obtener nueva configuración
        nuevo_estado, nuevo_simbolo, direccion = self.transiciones[clave]

        # Escribir nuevo símbolo en la cinta
        self.cinta[self.posicion_cabezal] = nuevo_simbolo

        # Mover cabezal según la dirección
        if direccion == "R":
            self.posicion_cabezal += 1
            # Si se mueve más allá del final, extender la cinta con blanco
            if self.posicion_cabezal == len(self.cinta):
                self.cinta.append(self.simbolo_blanco)
        elif direccion == "L":
            if self.posicion_cabezal == 0:
                # Si se mueve a la izquierda del inicio, agregar blanco
                self.cinta.insert(0, self.simbolo_blanco)
            else:
                self.posicion_cabezal -= 1

        # Cambiar de estado
        self.estado_actual = nuevo_estado

        # Verificar si estamos en estado de aceptación
        # Se detiene automáticamente si llega a blanco y está en estado aceptado
        if self.estado_actual in self.estados_aceptacion:
            self.aceptada = True
            self.detener = True

        return True  # Todavía hay pasos posibles

    # -------------------------------------------------------------------
    def ejecutar_toda(self, max_pasos=1000):
        """Ejecuta automáticamente hasta detenerse o alcanzar un número máximo de pasos."""
        pasos = 0
        while not self.detener and pasos < max_pasos:
            self.paso()
            pasos += 1
        return self.aceptada

    # -------------------------------------------------------------------
    def mostrar_cinta(self):
        """Devuelve una cadena visual con la posición del cabezal."""
        salida = ""
        for i, simbolo in enumerate(self.cinta):
            if i == self.posicion_cabezal:
                salida += f"[{simbolo}]"
            else:
                salida += f" {simbolo} "
        return salida
