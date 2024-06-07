"""

Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
mensaje que indique el resultado.

"""

nro = int(input("Ingresa un numero entero: "))

if nro % 2 == 0:
  print(f"Tu numero es un numero par")
else:
  print(f"Tu numero es un numero impar")
