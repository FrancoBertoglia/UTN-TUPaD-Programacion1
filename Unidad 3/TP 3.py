#Actividad 1
edad = int(input ("Ingrese su edad: "))
if edad >18: 
        print(" Es mayor de edad")

#Actividad 2
nota = float( input (" Ingrese su nota: "))
if nota >=6: 
    print(" Aprobado")
else: 
     nota <6
     print(" Desaprobado ")

#Actividad 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Actividad 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print(" Es niño ")
elif edad >= 12 and edad <=18:
    print(" Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Actividad 5

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6
import random
import statistics

# Lista de 50 números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular media, mediana y moda
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

# Mostrar la lista y las medidas
print("Lista:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Determinar el sesgo
if media > mediana > moda:
    print("La distribución presenta sesgo positivo.")
elif media < mediana < moda:
    print("La distribución presenta sesgo negativo.")
else:
    print("La distribución no presenta sesgo o es aproximadamente simétrica.")

#Actividad 7
#solicitar palabra o frase al usuario
frase = input ("ingrese una palabra o frase:")
if frase[-1].lower() in "aeiou":
    frase = frase + "!"
print(frase)

#Actividad 8
nombre = input("Ingrese su nombre: ")

print("Seleccione una opción:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")

opcion = int(input("Ingrese una opción (1, 2 o 3): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

#Actvidad 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud <= 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Actvidad 10
hemisferio = input (" Ingresa el hemisferio (N/S): "). upper()

mes = int(input (" Ingrese el mes del año en números (1/12): "))

dia = int(input(" Ingrese el dia: "))

if hemisferio == "S" :
    if ( mes ==12 and dia >= 21) or (mes == 1 or mes ==2) or (mes ==3 and dia <=20):
        print("Verano")
    elif ( mes== 3 and dia >=21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        print ("Otoño")
    elif ( mes== 6 and dia >=21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        print ("Invierno")
    elif ( mes== 9 and dia >=21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        print ("Primavera")
    
elif hemisferio == "N":
     if ( mes ==12 and dia >= 21) or (mes == 1 or mes ==2) or (mes ==3 and dia <=20):
        print("Invierno")
     elif ( mes== 3 and dia >=21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        print ("Primavera")
     elif ( mes== 6 and dia >=21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        print ("Verano")
     elif ( mes== 9 and dia >=21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        print ("Otoño")

else:
    print(" Error, el hemisferio ingresado no es correcto.")