"""
Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
  ● la suma de ambos números
  ● la resta de ambos números
  ● la multiplicación de ambos números
  ● la división entera de ambos números
  ● el resto 

"""

nro1 = int(input("Ingresa un numero: "))
nro2 = int(input("Ingresa otro numero: "))

# calculadora

suma = nro1 + nro2
resta = nro1 - nro2
multiplicacion = nro1 * nro2
division = nro1 / nro2
resto = nro1 % nro2

print(f"La suma de tus nros es: {suma}, la resta es: {resta}, la multiplicación es: {multiplicacion}, la división es: {division}, y el resto es: {resto}")