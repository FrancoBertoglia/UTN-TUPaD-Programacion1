# Actividad 1
print ("hola mundo")
#Actividad 2 
nombre = "Marcos"
print (f"hola {nombre}")
#Actividad 3
nombre = " Marcos "
apellido = " Perez "
edad = " 30 años"
vivo = " y vivo en Argentina ."
print (f"Soy" + nombre + apellido + "tengo" + str(edad)+ vivo)

#Actividad 4
radio = float(input("Ingrese el radio del circulo:"))

area = 3.1416 * radio * radio
perimetro = 2 * 3.1416 * radio

print("Área:", area)
print("Perímetro:", perimetro)

#Actividad 5
segundos = float(input("Ingrese una cantidad de segundos: "))

# Convertir a horas
horas = segundos / 3600

# Mostrar resultado
print("Equivale a", horas, "horas")

#Actividad 6
numero = int(input ("ingresa un numero"))

# tabla de multiplicar del numero ingresado
resultadoa = numero * 1
resultadob = numero * 2
resultadoc = numero * 3
resultadod = numero * 4
resultadoe = numero * 5
resultadof = numero * 6
resultadog = numero * 7
resultadoh = numero * 8
resultadoi = numero * 9
resultadoj = numero * 10

print ("el valor final es", resultadoa, resultadob, resultadoc, resultadod, resultadoe, resultadof,resultadog, resultadoh, resultadoi, resultadoj)

#Actividad 7
numero1 = int(input("ingrese el primer numero entero diferente de 0:"))
numero2 = int(input("ingrese el segundo numero entero diferente de 0:"))

#suma
resultado_suma= numero1 + numero2
print("el valor de la suma final es:",resultado_suma)

#division
resultado_division= numero1 / numero2
print ("el valor de la division final es:",resultado_division)

#multipilcacion
resultado_multiplicacion= numero1 * numero2
print ("el resultado de la multiplicacion final es:",resultado_multiplicacion)
#resta
resultado_resta= numero1 - numero2
print("el resultado de la resta final es:",resultado_resta)

#Actividad 8
altura= float(input("ingrese su altura en metros:"))
peso= float(input("ingrese su peso en kg:"))

#indice de masa corporal
indice_de_masa_corporal= peso / (altura * altura)
print("el indice de masa corporal es:",indice_de_masa_corporal)

#Actividad 9
grados_celsius= float(input("ingrese temperatura en grados celsius:"))

temperatura_fahrenheit= 9 / 5 * grados_celsius + 32

print("Su equivalente en grados fahreheir es:",temperatura_fahrenheit)

#Actividad 10

numero_1= float(input("ingrese el primer numero:"))
numero_2= float(input("ingrese el segundo numero:"))
numero_3= float(input("ingrese el tercer numero:"))

promedio= (numero_1+numero_2+numero_3) / 3
print(" El promedio de dichos numeros es:", promedio)
