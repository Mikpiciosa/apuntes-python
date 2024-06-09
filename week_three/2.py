"""
Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.

"""

a = input("Ingresa una letra: ")

mi_list = ["a", "e", "i", "o", "u"]

es_vocal = a in mi_list


print(es_vocal)