# EJERCICIO 1
"""1) Crear una lista con las notas de 10 estudiantes.
● Mostrar la lista completa.
● Calcular y mostrar el promedio.
● Indicar la nota más alta y la más baja."""

lista = []
pos_max =[]
pos_min =[]

# Lo hago para 10 estudiantes
for i in range(10):                                                             
    nota = float(input(f"Ingresar la nota del estudiante Nº {i + 1}: "))
    lista.append(nota)     # Que cada nota se vaya agregando a la lista

# Calculo promedio, la nota máxima y la mínima de la lista
promedio = sum(lista) / len(lista)                                            
maxima = max(lista)
minima = min(lista)

# Si bien no lo pide.. para verificar, agrego la o las posiciones de la lista en donde aparecen las notas más altas y más bajas
for i in range(len(lista)):
    if lista[i] == maxima:
        pos_max.append(i)
    if lista[i] == minima:
        pos_min.append(i)

# Muestro resultados
print(f"Promedio: {promedio:.2f}")                                              
print(f"Nota más alta: {maxima:.2f} en la/s posicion/es {pos_max} ")
print(f"Nota más baja: {minima:.2f} en la/s posicion/es {pos_min}")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 2

"""2) Pedir al usuario que cargue 5 productos en una lista.
● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
● Preguntar al usuario qué producto desea eliminar y actualizar la lista."""

lista = []
eliminar = ""

# Lo hago para 5 productos
for i in range(5):
    productos = input(f"Ingresar producto Nº {i + 1}: ")
    lista.append(productos)
    lista_ordenada = sorted(lista)                    # Ordeno la lista ingresada

while True:

    eliminar = input("Desea eliminar un producto agregado S/N: ").upper()
    
    if eliminar == "S":
        eliminar_producto = input("Ingrese producto desea eliminar: ")
        
        if eliminar_producto in lista_ordenada:              # Busca en lista si se encuentra el nombre del producto ingresado en la linea de codigo anterior
            
            while eliminar_producto in lista_ordenada:       # Uso while para que borre toodos los registros repetidos ingresados
            
                lista_ordenada.remove(eliminar_producto)     # Si lo encuentra, lo elimina
            
            print("Lista actualizada")
        
        else:
            print("no se encuentra el producto en la lista")
    
    elif eliminar == "N":
        break

    else:
        print("opcion invalida")

print(lista_ordenada)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 3

"""3) Generar una lista con 15 números enteros al azar entre 1 y 100.
● Crear una lista con los pares y otra con los impares.
● Mostrar cuántos números tiene cada lista."""

import random

lista = []
lista_pares = []
lista_impares = []


for i in range(15):
    numeros_randoms = random.randint(1, 100)
    lista.append(numeros_randoms)
    if numeros_randoms % 2 == 0:
        lista_pares.append(numeros_randoms)
    else:
        lista_impares.append(numeros_randoms)

print(f"los numeros pares generados son los siguientes: {lista_pares} y son {len(lista_pares)}")
print(f"los numeros impares generados son los siguientes: {lista_impares} y son {len(lista_impares)}")
print()
print(f"Lista completa: {lista}")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 4

"""4) Dada una lista con valores repetidos:
● Crear una nueva lista sin elementos repetidos.
● Mostrar el resultado."""

lista = [2, 4 , 6 , 2 , 4 , 6 , 9]
lista_sin_repetidos = []

for numero in lista:
    if numero not in lista_sin_repetidos:
        lista_sin_repetidos.append(numero)

# Lo que hago aca es recorrer uno a uno cada valor de la lista original, y lo va agregando a la nueva lista (lista_sin_repetidos).
# Cuando encuentre un valor que ya agrego anteriormete, simplemente no entra al if, por lo tanto no lo agrega (append)

print(lista_sin_repetidos)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 5

"""5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
● Mostrar la lista final actualizada."""

lista = ['Nestor', 'José', 'Laura', 'Flavia', 'Andrés', 'Agustina', 'Matias', 'Nora']
lista_final = lista.copy()  # Agrego una copia de la lista para poder mostrar al final la original y la que resulta como lista final

while True:

    # Incorporo un menú de navegación para que el usuario defina que quiere hacer

    print('¿Qué desea hacer ahora\n' \
    '1 - Agregar un estudiante\n' \
    '2 - Eliminar uno existente\n' \
    '3 - Continuar y mostrar la lista')

    opcion = int(input("Opcion: "))

    match opcion:
        case 1:     # Agregar estudiante a la lista
            agregar_estudiante = input("Nombre estudiante a agregar: ")
            
            if agregar_estudiante not in lista: # Esto simplemente para no agregar duplicados
                lista_final.append(agregar_estudiante)
                print(f"{agregar_estudiante} ah sido agregado a la lista")
            else:
                print(f"{agregar_estudiante} ya se encontraba en la lista")

        case 2:     # Eliminar estudiante de la lista
            eliminar_estudiante = input("Nombre estudiante a eliminar: ")

            if eliminar_estudiante in lista:
                lista_final.remove(eliminar_estudiante)
                print(f"{eliminar_estudiante} ah sido quitado de la lista")
            
            else:
                print(f"No se encuentra {eliminar_estudiante} en la lista")
        
        case 3:     # Salir del While true
            break
        
        case _:
            print("Opcion no valida, ingrese una correcta")

print(lista)
print(lista_final)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 6

"""6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
(el último pasa a ser el primero)."""

lista = [1, 2, 3, 4, 5, 6, 7]

lista_nueva = []
lista_nueva.append(lista[-1])       # Con esto a la nueva lista, defino como primer elemento de la lista nueva el ultimo de la lista original

for i in range(len(lista) - 1):     # Ya aca guarda uno a uno pero movidos a la derecha  
    lista_nueva.append(lista[i])

print(lista_nueva)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 7

"""7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de
una semana.
● Calcular el promedio de las mínimas y el de las máximas.
● Mostrar en qué día se registró la mayor amplitud térmica."""

matriz = [
    [15, 20],
    [20, 22],
    [12, 15],
    [15, 18],
    [20, 28],
    [25, 30],
    [28, 29],
]

# Promedios
suma_min = 0
suma_max = 0
for temperatura in matriz:
    suma_min += temperatura[0]
    suma_max += temperatura[1]

prom_min = suma_min / len(matriz)
prom_max = suma_max / len(matriz)

# Mayor amplitud
amplitud_maxima = 0
dia = 0
for i in range(len(matriz)):
    dato_provisorio = matriz[i][1] - matriz[i][0]
    if dato_provisorio > amplitud_maxima:
        amplitud_maxima = dato_provisorio
        dia = i + 1

# Resultados
print(f"Promedio mínimas: {prom_min:.2f}")
print(f"Promedio máximas: {prom_max:.2f}")
print(f"Mayor amplitud: {amplitud_maxima} °C")
print(f"Ocurrió en el día: {dia}")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 8

"""8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
● Mostrar el promedio de cada estudiante.
● Mostrar el promedio de cada materia."""

matriz = [
    [7, 8, 10],
    [8, 6, 7],
    [2, 5, 4],
    [7, 7, 6],
    [9, 10, 10],
]

for i, estudiante in enumerate(matriz, start=1):                    # utilizo enumerate para recorrer toda la matriz y tener el valor del indice tambien y que arranque en 1
    prom_estudiante = sum(estudiante) / len(estudiante)
    print(f"Promedio del estudiante {i}: {prom_estudiante:.2f}")    # valor del promedio a 2 decimales

num_materias = len(matriz[0])

for j in range(num_materias):
    suma_materia = 0
    for i in range(len(matriz)):
        suma_materia += matriz[i][j]
    prom_materia = suma_materia / len(matriz)
    print(f"Promedio de la materia {j+1}: {prom_materia:.2f}")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 9

"""9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
● Inicializarlo con guiones "-" representando casillas vacías.
● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
● Mostrar el tablero después de cada jugada."""

# Inicializar tablero 3x3
tateti = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Contador de turnos para saber cuándo termina
turnos = 0
turno_jugador = "X"

# Bucle principal
while turnos < 9:  # máximo 9 turnos en Ta-Te-Ti
    print(f"\nTurno del jugador {turno_jugador}:")
    
    # Pedir fila y columna
    fila = int(input("Fila (1-3): "))
    columna = int(input("Columna (1-3): "))
    
    # Resto 1 porque los índices empiezan en 0
    fila_idx = fila - 1
    columna_idx = columna - 1
    
    # Verifico que la casilla esté libre
    if tateti[fila_idx][columna_idx] == "-":
        tateti[fila_idx][columna_idx] = turno_jugador
        turnos += 1
    else:
        print("Casilla ocupada, elige otra.")
        continue  # vuelve a pedir fila y columna
    
    # Muestro tablero
    for fila_tateti in tateti:
        for casilla in fila_tateti:
            print(casilla, end=" ")
        print()
    
    # Se cambia el turno
    if turno_jugador == "X":
        turno_jugador = "O"
    else:
        turno_jugador = "X"

print("\nEl tablero está lleno. Fin del juego.")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 10

"""10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
● Mostrar el total vendido por cada producto.
● Mostrar el día con mayores ventas totales.
● Indicar cuál fue el producto más vendido en la semana."""

matriz = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

cantidad_productos = 4
cantidad_dias = 7

# Ingreso de datos
for i in range(cantidad_dias):
    print(f"Ingrese las ventas del día Nº {i+1}")
    for j in range(cantidad_productos):
        venta = int(input(f"Cantidad de ventas del producto {j+1}: "))
        matriz[j][i] = venta

# Valores vendidos por producto
print("\nTotal vendido por producto:")
for i, total_producto in enumerate(matriz, start=1):
    suma_prod = sum(total_producto)
    print(f"Producto {i}: {suma_prod} ventas")

# Día con mayores ventas
max_ventas_dia = 0
dia_mayor = 0

for j in range(cantidad_dias):
    suma_dia = 0
    for i in range(cantidad_productos):
        suma_dia += matriz[i][j]
    if suma_dia > max_ventas_dia:
        max_ventas_dia = suma_dia
        dia_mayor = j + 1

# Producto más vendido
max_producto = 0
producto_mas_vendido = 0

for i, total_producto in enumerate(matriz, start=1):
    suma_prod = sum(total_producto)
    if suma_prod > max_producto:
        max_producto = suma_prod
        producto_mas_vendido = i

# Resultados
print(f"\nEl día con mayores ventas totales fue el día {dia_mayor} con {max_ventas_dia} ventas.")
print(f"El producto más vendido en la semana fue el producto Nº {producto_mas_vendido} con {max_producto} ventas.")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 11

"""11) Crear una lista con los nombres de 10 estudiantes.
● Solicitar al usuario que ingrese un nombre a buscar.
● Indicar si el nombre se encuentra en la lista.
● Mostrar la posición en la que aparece.
● Si no se encuentra, informar que no está en la lista."""

lista = ['Nestor', 'José', 'Laura', 'Flavia', 'Andrés', 'Agustina', 'Matias', 'Nora', 'Santiago', 'Josefina']

nombre = input("Ingrese su nombre: ")
pos = 0

if nombre not in lista:
    print("No se encuentra en la lista")

else:
    if nombre in lista:
        pos = lista.index(nombre)           #Utilizo index para que me de directamente la posicion del nombre en la lista

    print(f"Se ah encontrado a {nombre}, y se encuentra en la posicion {pos} dentro de la lista")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 12

"""12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
● Mostrar la lista original.
● Mostrar la lista ordenada de menor a mayor.
● Mostrar la lista ordenada de mayor a menor.
● Investigar el uso de sorted() y del parámetro reverse."""

lista = []
numero = 0
cantidad_numeros = 0

# Por las dudas, valido que siempre ingresen numeros enteros
while cantidad_numeros < 8:     
    numero = input(f"Ingrese un número entero Nº{cantidad_numeros + 1} : ")
    
    if numero.isdigit():
        numero = int(numero)
        lista.append(numero)
        cantidad_numeros += 1   # hago el incremento para que una vez ingresados los 8 digitos salga del while
        continue                # continue para que me vuelva a pedir un nuevo numero
    else:
        print("Error, ingrese un número entero válido")


print(f"la lista original es: {lista}")

print(f"Ordenada de menor a mayor: {sorted(lista)}")                # Ordeno la lista de menor a mayor con sorted(lista)
print(f"Ordenada de mayor a menor: {sorted(lista, reverse=True)}")  # Ordeno la lista de mayor a menor con sorted(reverse=True)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# EJERCICIO 13

"""13) Dada la siguiente lista de puntajes de un videojuego:
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
● Mostrar el puntaje más alto y el más bajo.
● Mostrar la lista ordenada de mayor a menor (ranking).
● Indicar en qué posición del ranking se encuentra el puntaje 990."""

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

maximo = max(puntajes)                                                      # Busco el máximo en lista con max ()
minimo = min(puntajes)                                                      # Busco el mínimo en lista con min ()

ranking = sorted(puntajes, reverse=True)                                    # Para no alterar la originar, creo una nueva lista con el orden de ranking de mayor a menor
indice = ranking.index(990)                                                 # Busco el indice la tabla ordenada

print(f"El puntaje máximo es {maximo}")
print(f"El puntaje mínimo es {minimo}")
print(f"La lista de puntajes original es {puntajes}")
print(f"La lista de puntajes ordenada de mayor a menor es {ranking}")
print(f"El puntaje 990, se encuenta en el indice: {indice}")