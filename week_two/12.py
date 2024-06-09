"""
Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla (pista: usar una función predefinida
de Python).
"""

palabra = input("Ingresa una palabra: ")

quitar = palabra.replace("a", "x")

print(f"Tu palabra sin A es: {quitar}")


