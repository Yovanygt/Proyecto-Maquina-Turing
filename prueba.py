from turing_machine import TuringMachine

# Ejemplo: máquina que acepta cadenas con número par de 1s
estados = {"q0", "q1"}
alfabeto = {"0", "1"}
transiciones = {
    ("q0", "1"): ("q1", "1", "R"),
    ("q1", "1"): ("q0", "1", "R"),
    ("q0", "0"): ("q0", "0", "R"),
    ("q1", "0"): ("q1", "0", "R")
}
estado_inicial = "q0"
estados_aceptacion = {"q0"}

m = TuringMachine(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion)
m.cargar_cadena("1100")

while m.paso():
    print(m.mostrar_cinta(), "Estado:", m.estado_actual)

print("Resultado:", "ACEPTADA ✅" if m.aceptada else "RECHAZADA ❌")
