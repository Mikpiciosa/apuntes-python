"""
Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos

"""

numeros = []

for n in range(5):
  numero = int(input(f"Ingresa un numero entero {n+1}: "))
  numeros.append(numero)

promedio = sum(numeros) / len(numeros)

print(f"El promedio de los números ingresados es: {promedio}")
