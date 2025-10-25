

class TuringMachine:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion, simbolo_blanco="_"):
        self.estados = estados

        self.alfabeto = alfabeto

        self.transiciones = transiciones

        self.estado_inicial = estado_inicial

        self.estados_aceptacion = estados_aceptacion

        self.simbolo_blanco = simbolo_blanco

        self.resetear()

    # -------------------------------------------------------------------
    def resetear(self):
        self.cinta = []
        self.posicion_cabezal = 0
        self.estado_actual = self.estado_inicial
        self.detener = False
        self.aceptada = False

    # -------------------------------------------------------------------
    def cargar_cadena(self, cadena):
        self.resetear()
        self.cinta = list(cadena)
        if len(self.cinta) == 0:
            self.cinta = [self.simbolo_blanco]
        self.posicion_cabezal = 0

    # -------------------------------------------------------------------
    def paso(self):
  
        if self.detener:
            return False  

     
        if self.posicion_cabezal < 0:
            self.cinta.insert(0, self.simbolo_blanco)
            self.posicion_cabezal = 0
        elif self.posicion_cabezal >= len(self.cinta):
            self.cinta.append(self.simbolo_blanco)

        simbolo_leido = self.cinta[self.posicion_cabezal]

        clave = (self.estado_actual, simbolo_leido)
        if clave not in self.transiciones:
            self.detener = True
            return False

        nuevo_estado, nuevo_simbolo, direccion = self.transiciones[clave]

        self.cinta[self.posicion_cabezal] = nuevo_simbolo

        if direccion == "R":
            self.posicion_cabezal += 1
            if self.posicion_cabezal == len(self.cinta):
                self.cinta.append(self.simbolo_blanco)
        elif direccion == "L":
            if self.posicion_cabezal == 0:
                self.cinta.insert(0, self.simbolo_blanco)
            else:
                self.posicion_cabezal -= 1
        self.estado_actual = nuevo_estado


        if self.estado_actual in self.estados_aceptacion:
            self.aceptada = True
            self.detener = True

        return True 

    # -------------------------------------------------------------------
    def ejecutar_toda(self, max_pasos=1000):
        
        pasos = 0
        while not self.detener and pasos < max_pasos:
            self.paso()
            pasos += 1
        return self.aceptada

    # -------------------------------------------------------------------
    def mostrar_cinta(self):
        
        salida = ""
        for i, simbolo in enumerate(self.cinta):
            if i == self.posicion_cabezal:
                salida += f"[{simbolo}]"
            else:
                salida += f" {simbolo} "
        return salida
