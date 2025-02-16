# Importar las bibliotecas necesarias
import tkinter as tk
from tkinter import messagebox, scrolledtext
from lark import Lark

# Definir la gramática con soporte para números negativos, restas, divisiones y potencias
grammar = """
    start: expresion
    expresion: expresion "+" termino  -> suma
        | expresion "-" termino  -> resta
        | termino
    termino: termino "*" factor  -> multiplicacion
        | termino "/" factor  -> division
        | factor
    factor: factor "^" power  -> potencia
          | power    
    power: NUMBER        -> numero
            | "-" NUMBER        -> negativo
            | "(" expresion ")"  -> parentesis

    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

# Crear el parser
parser = Lark(grammar, parser='lalr')


# Función para analizar una expresión
def parse_expression(expression):
    try:
        # Parsear la expresión
        tree = parser.parse(expression)
        # Devolver el árbol sintáctico en formato legible
        return f"Syntax tree:\n{tree.pretty()}"
    except Exception as e:
        return f"Syntax error: {e}"


# Función para manejar el botón "Analizar"
def analyze_expression():
    # Obtener la expresión ingresada por el usuario
    expression = entry.get()
    if not expression:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una expresión.")
        return

    # Analizar la expresión y mostrar el resultado en el cuadro de texto
    result = parse_expression(expression)
    output_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
    output_text.insert(tk.END, result)  # Insertar el nuevo resultado


# Crear la ventana principal de la GUI
root = tk.Tk()
root.title("Analizador Sintáctico")
root.geometry("500x400")

# Crear y colocar los widgets en la ventana
label = tk.Label(root, text="Ingresa una expresión aritmética:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

analyze_button = tk.Button(root, text="Analizar", command=analyze_expression)
analyze_button.pack(pady=10)

# Crear un cuadro de texto con barra de desplazamiento
output_text = scrolledtext.ScrolledText(root, width=60, height=15, wrap=tk.WORD)
output_text.pack(pady=10)

# Iniciar el bucle principal de la GUI
root.mainloop()