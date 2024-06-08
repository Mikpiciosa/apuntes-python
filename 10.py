"""
Obtener una palabra e imprimir la cantidad de letras
"""

def obtener_letras():
    palabra = input("Ingresa una palabra aleatoria: ")
    
    longitud = len(palabra)

    lista_letras = list(palabra)

    print(f"La longitud de tu palabra es: {longitud} Y las letras que usaste son: {lista_letras}")

obtener_letras()