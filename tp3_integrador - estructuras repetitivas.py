# Ejercicio 1— “Caja del Kiosco” Objetivo: Simular una compra con validaciones y cálculo de total. Requisitos:

#   1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).

#   2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while).

#   3. Por cada producto (usar for):
#       o Pedir precio (entero, validar .isdigit()).
#       o Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula).
#       o Si tiene descuento: aplicar 10% al precio de ese producto.

#   4. Al final mostrar:
#       o Total sin descuentos
#       o Total con descuentos
#       o Ahorro total
#       o Promedio por producto (usar float y formatear con :.2f, ejem: 
#           x = 3.14159 
#           print(f"{x:.2f}"))

# Validaciones obligatorias
#   • Sin try/except.
#   • No aceptar vacío en nombre (si queda vacío, es error).
#   • Cantidad > 0 (si ingresa 0, volver a pedir).

# Salida esperada (ejemplo)
#   Cliente: Ana
#   Cantidad de productos: 3
#   Producto 1 - Precio: 100 Descuento (S/N): s
#   Producto 2 - Precio: 50 Descuento (S/N): n
#   Producto 3 - Precio: 200 Descuento (S/N): s
#   Total sin descuentos: $350
#   Total con descuentos: $320.00
#   Ahorro: $30.00
#   Promedio por producto: $106.67



cantidad = 0
precio_producto = 0
precio_descuento = 0
precio_total_con_descuento = 0
precio_total_sin_descuento = 0
ahorro = 0
promedio = 0
productos = []

nombre = input("Ingrese su nombre: ").title()

while not nombre.isalpha():
   
    nombre = input("Error, nombre no valido, ingrese su nombre nuevamente: ").title()

cantidad = input("Ingresar la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Por favor ingresar un valor numerico valido: ")

cantidad = int(cantidad)

for i in range (1,cantidad + 1):
    precio_producto = input(f"Ingrese el precio del producto {i}: ")
    
    while not precio_producto.isdigit() or float(precio_producto) <= 0:
        precio_producto = input(f"Ingrese un precio con caracteres númericos, vuelva a ingresar el precio del producto {i}: ")

    precio_producto = float(precio_producto)    
       
    descuento = input("¿Tiene descuento? Ingresar S si lo tiene, caso contrario N: ").upper()

    while descuento not in ("S", "N"):
        descuento = input("Error, solo se admiten S/N, ingreselo nuevamente ").upper()
           
    precio_producto = float(precio_producto)
    

    if descuento == "S":
        precio_descuento = precio_producto - (precio_producto * 0.1)
    else:
        precio_descuento = precio_producto
    
    precio_total_con_descuento += precio_descuento
    precio_total_sin_descuento += precio_producto

    productos.append((i, precio_producto, descuento)) #agrego una lista paraque salga ordando los productos registrados
  
ahorro = precio_total_sin_descuento - precio_total_con_descuento
promedio = precio_total_con_descuento / cantidad

print(f"\nCliente: {nombre}")
print(f"cantidad de productos: {cantidad}")

for p in productos:
    print(f"Producto {p[0]} - Precio: ${p[1]} Descuento (S/N): {p[2]}")

print(f"Total sin descuentos: ${precio_total_sin_descuento}")
print(f"Total con descuentos: ${precio_total_con_descuento}")
print(f"Ahorro: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Ejercicio 2 — “Acceso al Campus y Menú Seguro” Objetivo: Login con intentos + menú de acciones con validación estricta. Requisitos:
#   1. Definir credenciales fijas en el código:
#       o usuario correcto: "alumno"
#       o clave correcta: "python123"
#   2. Permitir máximo 3 intentos para ingresar usuario y clave.
#   3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
#   4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
#       1. Ver estado de inscripción (mostrar “Inscripto”)
#       2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
#       3. Mostrar mensaje motivacional (1 frase)
#       4. Salir
#       5. Validación del menú:
#           o Debe ser número (.isdigit())
#           o Debe estar entre 1 y 4
#       Cambio de clave
#           • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.

# Salida esperada
# Intento 1/3 - Usuario: alumno
# Clave: xxx
# Error: credenciales inválidas.
# Intento 2/3 - Usuario: alumno
# Clave: python123
# Acceso concedido.
# 1) Estado 2) Cambiar clave 3) Mensaje 4) Salir
# Opción: a
# Error: ingrese un número válido.
# Opción: 5
# Error: opción fuera de rango.

usuario_correcto = "alumno"
clave_correcta = "python123"

acceso = False

for i in range (3):
    
    print(f"Intento {i+1}/3")
    usuario = input("Ingresar el nombre de usuario: ")
    clave = input("ingresar clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")

        acceso = True

        while acceso == True:
        
            print("1) Estado\n" \
            "2) Cambiar clave\n" \
            "3) Mensaje\n" \
            "4) Salir \n")

            opcion = input("Opcion: ")
        
            while not opcion.isdigit() or not (1 <= int(opcion) <=4):
                opcion = input("Error: ingrese un número válido: ")
        
            opcion = int(opcion)

            if opcion == 1:
                print ("Inscripto")
        
            elif opcion == 2:
                nueva_clave = input("ingresar nueva (minimo 6 digitos): ")
                confirmacion_nueva_clave = input("repetir nueva clave: ")
            
                while nueva_clave != confirmacion_nueva_clave or 1 <= len(nueva_clave) < 6:
                    print("\nLas claves debe coincidir y ser de 6 digitos")
                    nueva_clave = input("ingresar nueva clave de 6 digitos: ")
                    confirmacion_nueva_clave = input("repetir nueva clave de 6 digitos: ")              
           
                clave_correcta = nueva_clave
            
                print ("Se modifico la contraseña")
        
            elif opcion == 3:
                print("Cree en que puedes hacerlo y ya estarás a mitad de camino")
        
            elif opcion == 4:
                print("Adios")                
                break
        break
    else:
        print("Error en el ingreso de las credenciales")

if acceso == False:
    print("Cuenta bloqueada")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” Contexto: Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos:

# • Lunes: 4 turnos
# • Martes: 3 turnos

# Reglas
#   1. Pedir nombre del operador (solo letras).
#   2. Menú repetitivo hasta salir:
#       1. Reservar turno
#       2. Cancelar turno (por nombre)
#       3. Ver agenda del día
#       4. Ver resumen general
#       5. Cerrar sistema
#   3. Reservar:
#       o Elegir día (1=Lunes, 2=Martes).
#       o Pedir nombre del paciente (solo letras).
#       o Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
#       o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
#   4. Cancelar:
#       o Elegir día.
#       o Pedir nombre del paciente (solo letras).
#       o Si existe, cancelar y dejar el espacio vacío ("").
#   5. Ver agenda del día:
#       o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
#   6. Resumen general:
#       o Turnos ocupados y disponibles por día.
#       o Día con más turnos (o empate).
# Restricciones
#   • ❌ No listas, no diccionarios, no sets, no tuplas.
#   • ✅ Se permite usar "" como “vacío”.
#   • ✅ Validaciones con .isalpha() y .isdigit() (sin try/except).

menu = False

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
cantidad_turnos = 0
cantidad_turnos_lunes = 0
cantidad_turnos_martes = 0

nombre_operario = input("Ingrese su nombre del operador").title()

while not nombre_operario.isalpha():
    nombre_operario = input("Nombre incorrecto. Ingrese un nombre de operador valiodo nuevamente: ").title()

menu = True

while menu == True:
    print(f"Bienvenido {nombre_operario}, seleccione una de las siguientes opciones: ")
    
    print("\n1.Reservar turno\n"
       "2. Cancelar turno (por nombre)\n"
       "3. Ver agenda del día\n"
       "4. Ver resumen general\n"
       "5. Cerrar sistema\n)")
    
    opcion = input("Opción: ")

    while not opcion.isdigit() or not (1 <= int(opcion) <=5):
        
        print("Error. Ingresar una opción valida")
        print("\n1.Reservar turno\n"
       "2. Cancelar turno (por nombre)\n"
       "3. Ver agenda del día\n"
       "4. Ver resumen general\n"
       "5. Cerrar sistema\n)")
        
        opcion = input("Opción: ")
    
    opcion = int(opcion)

        
    match opcion:
        case 1: #Reservar turno
           
            print("\n1 = Lunes\n"
            "2 = Martes")
            
            eleccion = input("Elección: ")
            
            while not eleccion.isdigit() or not (1 <= int(eleccion) <=2):
                print("Error, selecciones una opcion valida:")
                print("\n1 = Lunes\n"
                "2 = Martes")
                eleccion = input("Elección: ")
           
            eleccion = int(eleccion)

            nombre_paciente = input("Ingrese su nombre del paciente: ").title()

            while not nombre_paciente.isalpha():
                nombre_paciente = input("Nombre incorrecto. Ingrese un nombre de paciente valiodo nuevamente: ").title()
            
            if eleccion == 1:
                if (nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4):
                    print ("El paciente ya tiene turno")
                elif lunes1 == "":
                    lunes1 = nombre_paciente
                    cantidad_turnos_lunes += 1 
                elif lunes2 == "":
                    lunes2 = nombre_paciente
                    cantidad_turnos_lunes += 1             
                elif lunes3 == "":
                    lunes3 = nombre_paciente 
                    cantidad_turnos_lunes += 1            
                elif lunes4 == "":
                    lunes4 = nombre_paciente
                    cantidad_turnos_lunes += 1 
                else:
                    print("No hay turnos disponibles") 
                    
            
            elif eleccion == 2:
                if (nombre_paciente == martes1 or nombre_paciente == martes2):
                    print ("El paciente ya tiene turno")
                elif martes1 == "":
                    martes1 = nombre_paciente
                    cantidad_turnos_martes += 1
                elif martes2 == "":
                    martes2 = nombre_paciente 
                    cantidad_turnos_martes += 1
                else:
                    print("No hay turnos disponibles") 
                  
            
        case 2: # Cancelar turno
            
            eleccion = input("Elección: ")
            
            while not eleccion.isdigit() or not (1 <= int(eleccion) <=2):
                print("Error, selecciones una opcion valida:")
                print("\n1 = Lunes\n"
                "2 = Martes")
                eleccion = input("Elección: ")
            
            eleccion = int(eleccion)

            if eleccion == 1:

                nombre_paciente = input("Ingrese su nombre del paciente: ").title()

                while not nombre_paciente.isalpha():
                    nombre_paciente = input("Nombre incorrecto. Ingrese un nombre de paciente valiodo nuevamente: ").title()
            
                if nombre_paciente == lunes1:
                    print ("Turno Cancelado")
                    lunes1 = ""
                    cantidad_turnos_lunes -= 1

                elif nombre_paciente == lunes2:
                    print ("Turno Cancelado")
                    lunes2 = ""
                    cantidad_turnos_lunes -= 1
                elif nombre_paciente == lunes3:
                    print ("Turno Cancelado")
                    lunes3 = ""
                    cantidad_turnos_lunes -= 1
                elif nombre_paciente == lunes4:
                    print ("Turno Cancelado")
                    lunes4 = ""
                    cantidad_turnos_lunes -= 1
                else:
                    print("ningun paciente con ese nombre")
                              
                

            elif eleccion == 2:
                
                nombre_paciente = input("Ingrese su nombre del paciente: ").title()

                while not nombre_paciente.isalpha():
                    nombre_paciente = input("Nombre incorrecto. Ingrese un nombre de paciente valiodo nuevamente: ").title()
            
                if nombre_paciente == martes1:
                    print ("Turno Cancelado")
                    martes1 = ""
                    cantidad_turnos_martes -= 1
                elif nombre_paciente == martes2:
                    print ("Turno Cancelado")
                    martes2 = ""
                    cantidad_turnos_martes -= 1
                else:
                    print("ningun paciente con ese nombre")     

        case 3: #Ver agenda del día
            eleccion = input("Elección: ")
            
            while not eleccion.isdigit() or not (1 <= int(eleccion) <=2):
                print("Error, selecciones una opcion valida:")
                print("\n1 = Lunes\n"
                "2 = Martes")
                eleccion = input("Elección: ")
            
            eleccion = int(eleccion)

            if eleccion == 1:
                
                print(f"Turno 1: {lunes1 if lunes1 != '' else 'Libre'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else 'Libre'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else 'Libre'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else 'Libre'}")
            
            if eleccion == 2:
                print(f"Turno 1: {martes1 if martes1 != '' else 'Libre'}")
                print(f"Turno 2: {martes2 if martes2 != '' else 'Libre'}")


        case 4: # Ver resumen
               
            print("Resumen de lo ingresado:\n"
                  f"Cantidad de turnos asignados para el lunes: {cantidad_turnos_lunes}"
                  f"Cantidad de turnos asignados para el martes: {cantidad_turnos_martes}"
                  f"Total de tunos: {cantidad_turnos_lunes + cantidad_turnos_martes}")
            
            if cantidad_turnos_lunes > cantidad_turnos_martes:
                print(f"El dia con mayor cantidad de turnos es el Lunes con {cantidad_turnos_lunes - cantidad_turnos_martes} más.")
            elif cantidad_turnos_lunes < cantidad_turnos_martes:
                print(f"El dia con mayor cantidad de turnos es el Martes con {cantidad_turnos_martes - cantidad_turnos_lunes} más.")
            else:
                print(f"Existen la misma cantidad de turnos, es un empate con: {cantidad_turnos_lunes} cada uno.")
        
        case 5: # Salir del sistema
            print("Adios")
            menu = False
            
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Ejercicio 4 — “Escape Room: La Bóveda” Historia: Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados. Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.

# Variables iniciales (NO se piden por teclado)
#   • energia = 100
#   • tiempo = 12
#   • cerraduras_abiertas = 0
#   • alarma = False
#   • codigo_parcial = ""

# Validaciones obligatorias
#   • No usar try/except
#   • Pedir nombre del agente y validar con .isalpha() en un while.
#   • Validar opciones del menú y cualquier número pedido con .isdigit() en un while.
#   • El juego debe funcionar con estructuras secuenciales, condicionales y repetitivas (puede usar funciones propias del lenguaje como .lower(), len(), formateo, etc.).

# Regla anti-spam (muy importante): Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al iniciar:
#   ✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces:
#   • se cobra el costo normal (-20 energía, -2 tiempo),
#   • NO abre cerradura, y se activa la alarma automáticamente (alarma = True) porque “la cerradura se trabó”.

# Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”. Menú de acciones (se repite mientras el juego siga). El juego continúa mientras:
#   • energia > 0, tiempo > 0, cerraduras_abiertas < 3
#   • y no esté bloqueado por alarma.

# En cada turno mostrar el estado y el siguiente menú:
#   1. Forzar cerradura (costo: -20 energía, -2 tiempo)
#   o Si la energía está por debajo de 40, hay “riesgo de alarma”:
#   ▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True.
#   o Si no hay alarma, abre 1 cerradura.
#   o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre.

# 2. Hackear panel (costo: -10 energía, -3 tiempo)
#   o Debe usar un for de 4 pasos mostrando progreso.
#   o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”).
#   o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan.

# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra) Regla de bloqueo por alarma:
#   • Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema se bloquea y se pierde.
# Condiciones de fin
#   • Si cerraduras_abiertas == 3 → VICTORIA
#   • Si energia <= 0 o tiempo <= 0 → DERROTA
#   • Si se bloquea por alarma → DERROTA (bloqueo)


# --- VARIABLES INICIALES ---                      
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_continuo = 0

agente = input("Ingrese su nombre de agente: ").title()
while not agente.isalpha():
    agente = input("Nombre incorrecto. Ingrese un nombre válido: ").title()

print(f"\nBienvenido agente {agente}. ¡Comienza la misión!\n")

# Juego principal
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} | Alarma: {alarma}")
    
    print("\n1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")

    opcion = input("Elegir acción: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 3):
        opcion = input("Error. Ingrese opción válida (1-3): ")
    
    opcion = int(opcion)

    # OPCIÓN 1: FORZAR
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_continuo += 1

        # Regla anti-spam
        if forzar_continuo == 3:
            alarma = True
            print("¡La cerradura se trabó! Se activó la alarma.")
        else:
            if energia < 40:
                riesgo = input("Riesgo de alarma. Elegir número 1-3: ")
                while not riesgo.isdigit() or not (1 <= int(riesgo) <= 3):
                    riesgo = input("Error. Elegir número 1-3: ")
                
                if int(riesgo) == 3:
                    alarma = True
                    print("¡Se activó la alarma!")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

    # OPCIÓN 2: HACKEAR
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_continuo = 0

        print("Hackeando...")
        for i in range(4):
            print(f"Paso {i+1}")
            codigo_parcial += "A"

        print(f"Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Cerradura abierta automáticamente!")

    # OPCIÓN 3: DESCANSAR
    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        forzar_continuo = 0

        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma te afectó (-10 energía extra)")
        else:
            print("Descansaste y recuperaste energía")

    # BLOQUEO POR ALARMA
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡El sistema se bloqueó por la alarma!")
        break

# RESULTADO FINAL
print("\n--- FIN DEL JUEGO ---")

if cerraduras_abiertas == 3:
    print("¡Ganaste! Abriste la bóveda.")
elif alarma and tiempo <= 3:
    print("Perdiste: el sistema se bloqueó por la alarma.")
elif energia <= 0 or tiempo <= 0:
    print("Perdiste: sin energía o sin tiempo.")
elif alarma:
    print("Perdiste: se activó la alarma.")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            
"""Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

1. Descripción del Escenario: Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El
objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo. Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de 
control (if/elif/else), ciclos (while y for) y validación de datos estricta.

2. Requerimientos Técnicos

A. Tipos de Datos
Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:
• • String: Para el nombre del jugador.
• • Int: Para los Puntos de Vida (HP) y cantidad de pociones.
• • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5)
• • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.

B. Reglas de Validación (¡Importante!)
• • No está permitido usar bloques try / except.
• • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.
• • Para validar números, debes usar el método .isdigit() dentro de un ciclo while.

3. Flujo del Programa
Paso 1: Configuración del Personaje
El programa inicia pidiendo el nombre del Gladiador.
• • Validación: El nombre solo puede contener letras. Si el usuario ingresa números, símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a preguntar hasta que sea válido.
Paso 2: Inicialización de Estadísticas 
El programa debe definir las variables iniciales (sin preguntar al usuario):
• • Vida del Gladiador: 100 (int)
• • Vida del Enemigo: 100 (int)
• • Pociones de Vida: 3 (int)
• • Daño base "Ataque Pesado": 15 (int)
• • Daño base del enemigo: 12 (int)
• • Turno Gladiador : True (booleano)
Paso 3: El Ciclo de Combate
El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 puntos de vida.
Turno del Jugador:
Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 opciones:
1. Ataque Pesado
2. Ráfaga Veloz (Requiere uso de for)
3. Curar
• Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo ingresado sea un número (.isdigit()).
2. Verificar que el número sea 1, 2 o 3.

o Si falla alguna validación, mostrar mensaje de error y volver a pedir. Lógica de las Acciones:
Acción A: Ataque Pesado (Opción 1)
• • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).
• • Resta el daño a la vida del enemigo.
• • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
Acción B: Ráfaga Veloz (Opción 2)
• • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.
• • El bucle debe repetirse 3 veces (usando range).
• • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.
• 2. Muestra el mensaje: " > Golpe conectado por 5 de daño".
•
Acción C: Curar (Opción 3) 
• • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.
• • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el enemigo ataca igual).
Turno del Enemigo:
Justo después de tu acción, el enemigo ataca automáticamente.
• • Resta el daño base del enemigo (12) a tu vida.
• • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"

Paso 4: Fin del Juego
Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:
• • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."
• • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."

4. Ejemplo de Ejecución (Consola)
Plaintext
--- BIENVENIDO A LA ARENA ---
Nombre del Gladiador: Leonidas1
Error: Solo se permiten letras.
Nombre del Gladiador: Leonidas
=== INICIO DEL COMBATE ===
Leonidas (HP: 100) vs Enemigo (HP: 100) | Pociones: 3
Elige acción:
1. Ataque Pesado
2. Ráfaga Veloz
3. Curar
Opción: A
Error: Ingrese un número válido.
Opción: 2
>> ¡Inicias una ráfaga de golpes!
> Golpe conectado por 5 de daño
> Golpe conectado por 5 de daño
> Golpe conectado por 5 de daño
>> ¡El enemigo contraataca por 12 puntos!
=== NUEVO TURNO ===
Leonidas (HP: 88) vs Enemigo (HP: 85) | Pociones: 3"""


print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ").title()
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").title()

# --- VARIABLES INICIALES ---
vida_jugador = 100
vida_enemigo = 100
pociones = 3

danio_jugador = 15
danio_enemigo = 12

turno_jugador = True

print("\n=== INICIO DEL COMBATE ===")

# --- COMBATE ---
while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    #TURNO DEL JUGADOR
    print("\nElige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 3):
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    
    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_jugador * 1.5
            print("¡Golpe crítico!")
        else:
            danio = danio_jugador

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} de daño!")

    
    elif opcion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print("Te curaste 30 puntos de vida")
        else:
            print("¡No quedan pociones!")

    
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

    print("=== NUEVO TURNO ===")

# --- FIN DEL JUEGO ---
print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")               
            
            






    
        

