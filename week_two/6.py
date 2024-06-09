"""
Crear una función que reciba un número y muestre el anterior y el siguiente

"""



a = int(input("Ingrese un numero: "))

def antseg(num):
    b = num - 1
    c = num + 1
    print(f"Tu numero es {a}, su anterior es {b} y su siguiente es {c}")


antseg(a)
