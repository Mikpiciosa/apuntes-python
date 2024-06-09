"""
Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
usuario, y no solo para 100?.

"""

a = int(input("Ingresa un numero: "))
b = int(input("Ingresa otro numero: "))
c = int(input("Ingresa un limite: "))

suma = a + b

def resultado_generalizado():
    if suma >= c:
        print(f"La suma de tus numeros es: {suma}, y el limite es: {c}, el resultado es mayor!")
    elif suma < c:
        resta = c - suma
        print(f"La suma de tus numeros es: {suma}, y el limite es: {c}, el resultado es menor! por ende, para llegar al limite propuesto te falta: {resta}")

resultado_generalizado()