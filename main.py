# Importar la biblioteca Lark
from lark import Lark

# Definir la gramática
grammar = """
    start: expr
    expr: expr "+" term  -> suma
        | expr "-" term  -> resta
        | term
    term: term "*" factor  -> multiplicacion
        | term "/" factor  -> division
        | factor
    factor: factor "^" power  -> power
          | power    
    power: NUMBER        -> numero
            | "-" NUMBER        -> negativo
            | "(" expr ")"  -> parentesis

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
        # Mostrar el árbol sintáctico
        print("Árbol sintáctico:")
        print(tree.pretty())
    except Exception as e:
        print(f"Error de sintaxis: {e}")

# Probar el analizador
expresion_usuario = input("Ingresa una expresión aritmética (por ejemplo, 3 + 5 * (2 + 1)): ")
print(f"Analizando la expresión: {expresion_usuario}")
parse_expression(expresion_usuario)