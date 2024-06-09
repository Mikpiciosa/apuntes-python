"""
Obtener una palabra e imprimir los primeros 5 caracteres (pista: slicear la palabra).
"""

def cortarpalabra():
    palabra = input("Ingresa la palabra: ")

    corte = palabra[0:5]

    print(f"Tu palabra es: {palabra}, y se corta en su 5ta letra: {corte}")

cortarpalabra()