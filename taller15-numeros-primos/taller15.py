#Ejercico A
import random

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Genera números aleatorios entre 1 y 100 hasta encontrar uno primo
while True:
    numero = random.randint(1, 100)
    if es_primo(numero):
        break

print(f"Número aleatorio primo generado: {numero}")


#Ejercicio B
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita el valor de N al usuario
n = int(input("Ingrese un número entero N: "))

print(f"Números primos hasta {n}:")
for i in range(2, n + 1):
    if es_primo(i):
        print(i, end=" ")