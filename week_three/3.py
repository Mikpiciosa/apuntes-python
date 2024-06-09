"""
Repetir pero para la expresión que permite saber si un número es par y menor a 10

"""

a = int(input("Ingresa un numero: "))

if a % 2 == 0:
    print("Es par")
else:
    print("Es impar")


if a < 10:
    print("Es menor a 10")
else:
    print("Es mayor a 10")
