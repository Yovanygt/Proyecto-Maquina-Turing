# 🧠 Simulador de Máquina de Turing

---

## 📄 Descripción del Proyecto
Este simulador permite a los usuarios experimentar con el funcionamiento de una **Máquina de Turing**, mostrando cómo se procesan las cadenas paso a paso de forma visual y didáctica.  

La aplicación fue desarrollada en **Python con Tkinter** e incluye:
- Ingreso de cadenas de entrada (numéricas o con letras).  
- Visualización de la cinta y el cabezal de lectura/escritura.  
- Ejecución paso a paso o completa.  
- Indicador visual del estado actual y del resultado final (aceptada o rechazada).  

---

## ⚙️ Funcionalidades Principales
1. **Interfaz Gráfica:**
   - Campo de texto para ingresar la cadena a procesar.  
   - Botones de control: ejecutar todo, paso a paso y reiniciar.  
   - Cinta visual con el cabezal de lectura.  

2. **Simulación:**
   - Muestra la evolución de la máquina en tiempo real.  
   - Indica el estado actual y la posición del cabezal.  
   - Determina si la cadena es **aceptada** o **rechazada** según las reglas definidas.  

3. **Compatibilidad de símbolos:**
   - Soporta tanto **números binarios (0 y 1)** como **letras o símbolos personalizados**.  
   - El alfabeto puede incluir caracteres como `a`, `b`, `x`, `y`, etc., siempre que se definan en las reglas de transición.  

4. **Configuración múltiple:**
   - Permite definir y guardar diferentes máquinas en un archivo `ejemplos.json`.  

---

## 🔠 Ejemplo 1 – Máquina que acepta cadenas con número par de 1’s

| Estado | Símbolo leído | Nuevo estado | Símbolo escrito | Dirección |
|:-------:|:--------------:|:-------------:|:----------------:|:----------:|
| q0 | 1 | q1 | 1 | R |
| q1 | 1 | q0 | 1 | R |
| q0 | 0 | q0 | 0 | R |
| q1 | 0 | q1 | 0 | R |
| q0 | _ | q0 | _ | S |
| q1 | _ | q1 | _ | S |

**Estado inicial:** q0  
**Estados de aceptación:** q0  
**Símbolo en blanco:** `_`  

📘 *Esta máquina acepta las cadenas con número par de unos, y rechaza las que tienen un número impar.*  

---

## 🔤 Ejemplo 2 – Máquina que acepta letras y números (terminan en “a” o “1”)

Además del alfabeto binario, el simulador permite usar letras u otros símbolos.  
Por ejemplo, esta máquina **acepta cadenas que terminan en la letra `a` o el número `1`**.

| Estado | Símbolo leído | Nuevo estado | Símbolo escrito | Dirección |
|:-------:|:--------------:|:-------------:|:----------------:|:----------:|
| q0 | a | qAcepta | a | S |
| q0 | 1 | qAcepta | 1 | S |
| q0 | b | qRechaza | b | S |
| q0 | 0 | qRechaza | 0 | S |
| q0 | _ | qRechaza | _ | S |

**Estado inicial:** q0  
**Estados de aceptación:** qAcepta  
**Símbolo en blanco:** `_`  

### 💬 Ejemplos de prueba:
| Cadena | Resultado |
|:--------|:-----------|
| `ab1` | ✅ Aceptada (termina en 1) |
| `ba`  | ✅ Aceptada (termina en a) |
| `b0`  | ❌ Rechazada |
| `bbb` | ❌ Rechazada |

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
