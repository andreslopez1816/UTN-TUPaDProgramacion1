# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad en números: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int (input("ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:

#   • Niño/a: menor de 12 años.
#   • Adolescente: mayor o igual que 12 años y menor que 18 años.
#   • Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#   • Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad en números: "))

if edad < 12:
    print ("Usted es un Niño/a")
elif 12 <= edad < 18:
    print ("Usted es un Adolecente")
elif 30 <= edad < 30:
    print ("Usted es un Aduto/a joven")
else:
    print ("Usted es un Aduto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input ("ingrese una contraseña entre 8 y 14 caracteres: ")

if 8 <= len(contraseña) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:

#   • Menor que 150 kWh: “Consumo bajo”.
#   • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
#   • Mayor que 300 kWh: “Consumo alto”.

# Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga: “Considere medidas de ahorro energético”. El programa debe imprimir por pantalla la categoría correspondiente.

consumo_energetico = float(input("ingrese su consumo energetico en kWh: "))

if consumo_energetico < 150:
    print("Consumo bajo")
elif 150 <= consumo_energetico <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

texto = input("Ingrese una frase o palabra: ")

ultimo_caracter = texto[-1].lower()

if ultimo_caracter == "a":
    print(texto + "!")
elif ultimo_caracter == "e":
    print(texto + "!")
elif ultimo_caracter == "i":
    print(texto + "!")
elif ultimo_caracter == "o":
    print(texto + "!")
elif ultimo_caracter == "u":
    print(texto + "!")
else:
    print(texto)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:

#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

# El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input ("ingrese su nomobre: ")

opcion = int (input("\nIngrese la opcion segun como quiere que se guarde su numbre:\n\n" 
                    
"1. Si quiere su nombre en mayúsculas.\n" 
"2. Si quiere su nombre en minúsculas\n" 
"3. Si quiere su nombre con la primera letra mayúscula\n\n"))

if opcion == 1:
    nombre = nombre.upper()
    print (nombre)
elif opcion == 2:
    nombre = nombre.lower()
    print(nombre)
elif opcion == 3:
        nombre = nombre.title()
        print(nombre)
else:
    print("No es una opción valida")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:

#   • Menor que 3: "Muy leve" (imperceptible).
#   • Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#   • Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#   • Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#   • Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#   • Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = float(input("Ingresar el valor de la magnitud del terromoto: "))

if 0 <= magnitud_terremoto < 3:
    print ("Muy leve (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 3 <= magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 3 <= magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
else:
    print("Valor no valido, ingrese un número positivo que corresponda con la escala de medicion de la magnitud de un terremoto")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año :

#                                                                     Hemisferio norte              Hemisferio sur             
#   • Desde 21 de diciembre hasta 20 de marzo (incluidos)        ---->   Invierno             ---->      Verano
#   • Desde 21 de marzo hasta 20 de junio (incluidos)            ---->   Primavera            ---->      Otoño
#   • Desde 21 de junio hasta 20 de septiembre (incluidos)       ---->   Verano               ---->      Invierno
#   • Desde 21 de septiembre hasta 20 de diciembre (incluidos)   ---->   Otoño                ---->      Primavera

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisferio = input("Ingrese en que hemuisfeiro se encuentra:\n\n"
                       "N = Si se encuentra en el Hemisferio norte\n"
                       "S = Si se encuentra en el Hemisferio sur\n\n").lower()

mes = int(input("\nMes (1-12): "))
dia = int(input("\nDía (1-31): "))

if hemisferio == "n":
    if (1 <= mes <= 2) or (mes == 12 and dia >= 21) or (mes == 3 and dia <=20):
        print("\nUsted se encuentra en Invierno")
    elif (4 <= mes <= 5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <=20):
        print("\nUsted se encuentra en Primavera")
    elif (7 <= mes <= 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <=20):
        print("\nUsted se encuentra en Verano")
    else:
        print("\nUsted se encuentra en Otoño")

if hemisferio == "s":
    if (1 <= mes <= 2) or (mes == 12 and dia >= 21) or (mes == 3 and dia <=20):
        print("\nUsted se encuentra en Verano")
    elif (4 <= mes <= 5) or (mes == 3 and dia >= 21) or (mes == 6 and dia <=20):
        print("\nUsted se encuentra en Otoño")
    elif (7 <= mes <= 8) or (mes == 6 and dia >= 21) or (mes == 9 and dia <=20):
        print("\nUsted se encuentra en Invierno")
    else:
        print("\nUsted se encuentra en Primavera")
