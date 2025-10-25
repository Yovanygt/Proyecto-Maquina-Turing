# 🧠 Simulador de Máquina de Turing

---

## 📄 Descripción del Proyecto
Este simulador permite visualizar el funcionamiento de una **Máquina de Turing** paso a paso, mostrando cómo se leen, escriben y procesan las cadenas de entrada.  

Desarrollado en **Python con Tkinter**, el programa incluye:
- Ingreso de cadenas (numéricas o alfabéticas).  
- Cinta visual con cabezal de lectura/escritura.  
- Ejecución paso a paso o completa.  
- Indicador visual de aceptación o rechazo.  

---

## ⚙️ Funcionalidades Principales
1. **Interfaz gráfica interactiva:**
   - Campo de texto para ingresar cadenas.
   - Botones: ejecutar todo, paso a paso y reiniciar.
   - Representación visual del movimiento del cabezal.

2. **Simulación dinámica:**
   - Muestra la evolución de los estados.
   - Indica si la cadena es **aceptada** o **rechazada**.

3. **Compatibilidad de símbolos:**
   - Soporta tanto **números binarios (0 y 1)** como **letras** (`a`, `b`, `c`).
   - Permite definir transiciones personalizadas.

4. **Configuración modular:**
   - Contiene diferentes archivos (`main.py`, `main_abc.py`) que demuestran distintos modelos de máquina.

---

## 🔢 Máquina Binaria – “Número Par de 1’s”

Esta máquina acepta todas las cadenas binarias que contienen un **número par de unos (1’s)**.  
Ejemplo: `00`, `11`, `1010`, `1100`, etc.

| Estado | Símbolo leído | Nuevo estado | Símbolo escrito | Dirección |
|:-------:|:--------------:|:-------------:|:----------------:|:----------:|
| q0 | 1 | q1 | 1 | R |
| q1 | 1 | q0 | 1 | R |
| q0 | 0 | q0 | 0 | R |
| q1 | 0 | q1 | 0 | R |
| q0 | _ | q0 | _ | S |
| q1 | _ | q1 | _ | S |

**Estado inicial:** q0  
**Estado(s) de aceptación:** q0  
**Símbolo en blanco:** `_`

---

### 🧠 Lógica de la Máquina Binaria
La máquina alterna entre dos estados:
- **q0:** cantidad par de unos → estado de aceptación.  
- **q1:** cantidad impar de unos → estado intermedio (no acepta).  

Cada vez que se lee un `1`, la máquina cambia de estado;  
cuando se lee un `0`, el estado no cambia.  
Si la máquina termina en `q0`, la cadena es aceptada.

---

### 💬 Ejemplos de Prueba (Resultados Reales)
| Cadena | Resultado | Explicación |
|:--------|:-----------|:-------------|
| `1` | ❌ Rechazada | Solo un “1” → cantidad impar. |
| `11` | ✅ Aceptada | Dos “1” → cantidad par. |
| `101` | ✅ Aceptada | Dos “1” (al inicio y final) → par. |
| `1100` | ✅ Aceptada | Dos “1” seguidos → par. |

📸 *Resultados comprobados en simulación real (ver imágenes adjuntas).*

---

## 🔤 Máquina Alfabética – “Aceptación Temprana”

Esta versión trabaja con letras (`a`, `b`, `c`).  
Su comportamiento se basa en **aceptar inmediatamente** si se encuentra una `a`, sin importar los símbolos que sigan.  
Si la cadena comienza con `b` o `c`, se rechaza.

| Estado | Símbolo leído | Nuevo estado | Símbolo escrito | Dirección |
|:-------:|:--------------:|:-------------:|:----------------:|:----------:|
| q0 | a | qAcepta | a | S |
| q0 | b | q1 | b | S |
| q0 | c | q1 | c | S |
| q1 | a | q1 | a | S |
| q1 | b | q1 | b | S |
| q1 | c | q1 | c | S |
| q0 | _ | q1 | _ | S |
| q1 | _ | q1 | _ | S |

**Estado inicial:** q0  
**Estado de aceptación:** qAcepta  
**Símbolo en blanco:** `_`

---

### 🧠 Lógica de la Máquina Alfabética
Esta máquina implementa **aceptación temprana**, lo que significa que:
> Si el primer símbolo leído es `a`, la cadena es aceptada inmediatamente.  
> Si empieza con `b` o `c`, pasa a un estado de rechazo sin retorno.

---

### 💬 Ejemplos de Prueba (Resultados Reales)
| Cadena | Resultado | Explicación |
|:--------|:-----------|:-------------|
| `a` | ✅ Aceptada | Detecta `a` al inicio. |
| `b` | ❌ Rechazada | Comienza con `b`, pasa a q1. |
| `ba` | ❌ Rechazada | El primer símbolo fue `b`. |
| `ab` | ✅ Aceptada | Acepta desde la primera lectura. |

📸 *Simulaciones verificadas en ejecución gráfica.*

---

## 🧩 Comparación entre ambas máquinas

| Característica | Máquina Binaria | Máquina Alfabética |
|-----------------|-----------------|--------------------|
| **Entrada** | `0` y `1` | `a`, `b`, `c` |
| **Objetivo** | Aceptar número par de 1’s | Aceptar si detecta “a” |
| **Estados** | q0, q1 | q0, q1, qAcepta |
| **Aceptación** | Requiere recorrido completo | Acepta de forma inmediata |
| **Tipo de control** | Paridad binaria | Lectura temprana |

---

## 💻 Tecnologías Utilizadas
- **Lenguaje:** Python 3.11  
- **Biblioteca:** Tkinter (interfaz gráfica)  
- **IDE:** Visual Studio Code  
- **Control de versiones:** Git + GitHub  

---

## 🚀 Ejecución del Programa

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Yovanygt/Proyecto-Maquina-Turing.git

## Programa funcionando

![enter image description here](https://i.postimg.cc/NFw1m5c1/Imagen-de-Whats-App-2025-10-23-a-las-01-28-28-0696e931.jpg)

![enter image description here](https://i.postimg.cc/d3K8rLYy/Imagen-de-Whats-App-2025-10-23-a-las-01-28-28-0e451886.jpg)

![enter image description here](https://i.postimg.cc/HnCQXVg4/Imagen-de-Whats-App-2025-10-23-a-las-22-47-28-48243717.jpg)

![enter image description here](https://i.postimg.cc/C5VjkzgC/Imagen-de-Whats-App-2025-10-24-a-las-20-30-39-82ac9996.jpg)

![enter image description here](https://i.postimg.cc/Y0w1YhH6/Imagen-de-Whats-App-2025-10-24-a-las-20-30-39-ab0e8118.jpg)

![enter image description here](https://i.postimg.cc/Xq0wdpbd/Imagen-de-Whats-App-2025-10-24-a-las-20-30-39-dfc2ee94.jpg)

