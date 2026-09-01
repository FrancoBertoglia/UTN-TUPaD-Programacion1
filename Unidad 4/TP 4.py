#Actividad 1
for i in range(101):
    print(i)

#Actividad 2
numero = int(input("Ingrese un número entero: "))

cantidad_digitos = len(str(abs(numero)))

print("La cantidad de dígitos es:", cantidad_digitos)

#Actvidad 3
inicio = int(input("Ingrese el primer valor: "))
fin = int(input("Ingrese el segundo valor: "))

suma = 0

for i in range(inicio + 1, fin):
    suma += i

print("La suma de los números comprendidos entre ambos valores es:", suma)

#Actividad 4

suma = 0

numero = int(input("Ingrese un número entero (0 para finalizar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro número entero (0 para finalizar): "))

print("La suma total es:", suma)

#Actividad 5
import random

numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    numero = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

    if numero == numero_secreto:
        print("¡Felicitaciones! Has adivinado el número.")
        print("Cantidad de intentos:", intentos)
        break
    else:
        print("Incorrecto. Intenta nuevamente.")

#Actividad 6


for numero in range(100, -1, -2):
    print(numero)

#Actividad 7
numero = int(input("Ingrese un número entero positivo: "))

suma = 0

for i in range(numero + 1):
    suma += i

print("La suma total es:", suma)

#Actividad 8
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#Actividad 9
suma = 0

for i in range(100):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

media = suma / 100

print("La media de los 100 números es:", media)

#Actividad 10

numero = input("Ingrese un número: ")

invertido = numero[::-1]

print("Número invertido:", invertido)
