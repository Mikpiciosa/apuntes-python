"""
Crear una función que reciba un entero y que retorne (devuelva) el resto y el cociente
"""

numero = int(input("Ingresa un numero entero: "))

def resto_cociente(num):
    resto = num % 2
    cociente = num / 2
    print(f"Tu numero es: {numero}, realizamos la division, el resultado es: {cociente} y el resto es: {resto}")


resto_cociente(numero)