# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print ("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_de_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math

radio_circulo = float(input("Ingrese el radio del circulo: "))
area = (radio_circulo**2) * math.pi 
perimetro = 2 * math.pi * radio_circulo

print(f"El área de la circunfernecia es: {area:.2f}")
print(f"El perímetro de la circunfernecia es: {perimetro:.2f}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas:.2f} hora/s")


# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.


numero1 = float(input("Ingrese primer número distinto de 0: "))

while numero1 == 0:
    print("Error, el número debe ser distinto de 0")
    numero1 = float(input("Ingrese nuevamente primer número distinto de 0: "))

numero2 = float(input("Perfecto, ahora ingrese segundo número distinto de 0: "))        

while numero2 == 0:
        print("Error, el número debe ser distinto de 0")
        numero2 = float(input("Ingrese nuevamente segundo número distinto de 0: "))

if numero1.is_integer:
     numero1 = int(numero1)

if numero2.is_integer:
     numero2 = int(numero2)

print(f"El resultado de la suma de los dos números elegidos es           ----> {numero1} + {numero2} = {numero1 + numero2}")
print(f"El resultado de la resta de los dos números elegidos es          ----> {numero1} - {numero2} = {numero1 - numero2}")
print(f"El resultado de la multiplicación de los dos números elegidos es ----> {numero1} x {numero2} = {numero1 * numero2}")
print(f"El resultado de la división de los dos números elegidos es       ----> {numero1} / {numero2} = {numero1 / numero2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 / (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))

imc = peso / (altura**2)

print(f"Su índice de masa corporal es: {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 * 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temperatura = float(input("Ingrese suna la temperatura en grados celsius: "))

fahrenheit = (9/5 * temperatura) + 32

print(f"{temperatura} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

suma = 0

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

suma = numero1 + numero2 + numero3

print(f"El promedio de los numeros seleccioandos es: {suma/3}")