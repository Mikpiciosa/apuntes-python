"""
Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
el usuario en el año ingresado.

"""

a = int(input("¿Cual es tu año de nacimiento?: "))
b = int(input("Decime un año cualquiera: "))

result_negative = b - a


if a < b:
  print(f"Ingresaste el año: {b} y tu edad en ese año seria: {result_negative}")
else:
  print(f"Ingresaste el año: {b} y no podemos calcular tu edad en ese año, ya que no existias")

