import random

###Aclaración: No vimos isdigit(), así que no lo quise usar
def cambiar_dados():
    dados_cantidad = None 
    while type(dados_cantidad) != int:
        dados_cantidad = input("Ingrese la cantidad de dados que desea tirar: ")
        for d in range(0, len(dados_cantidad)):
            if dados_cantidad[d] not in "1234567890":
                print("No se ha ingresado un número.")
                break
            elif d +1 == len(dados_cantidad):
                dados_cantidad = int(dados_cantidad)
                if dados_cantidad < 1:
                    dados_cantidad = None
                    print("Se necesita que la cantidad de dados sea mayor que 0.")
    eleccion = None
    while type(eleccion) != int:
        print("¿Quiere que todos los dados tengan la misma cantidad de caras, o dados diferentes?")
        print("  1: Dados iguales.")
        print("  2: Dados diferentes.")
        eleccion = input("Usted elige: ")
        if eleccion in ["1", "2"]:
            eleccion = int(eleccion)
        else:
            print("Su elección no es válida, por favor ingrese '1' o '2'.")
    if eleccion == 1:
        dados_caras = []
        while dados_caras == []:
            caras_total = input("Ingrese la cantidad de caras de los dados: ")
            for d in range(0, len(caras_total)):
                if caras_total[d] not in "1234567890":
                    print("No se ha ingresado un número.")
                    break
                elif d +1 == len(caras_total):
                    if int(caras_total) < 1:
                        print("Se necesita que la cantidad de caras de los dados sea mayor que 0.")
                        break
                    for dado in range(0, dados_cantidad):
                        dados_caras.append(int(caras_total))
    elif eleccion == 2:
        dados_caras = []
        for dado in range(1, dados_cantidad + 1):
            while len(dados_caras) < dado:
                caras_individual = input(f"Ingrese la cantidad de caras del dado {dado}: ")
                for d in range(0, len(caras_individual)):
                    if caras_individual[d] not in "1234567890":
                        print("No se ha ingresado un número.")
                        break
                    elif d +1 == len(caras_individual):
                        if int(caras_individual) < 1:
                            print("Se necesita que la cantidad de caras del dado sea mayor que 0.")
                            break
                        dados_caras.append(int(caras_individual))
    return [dados_cantidad, dados_caras]

###Aclaración: le asigno un tipo a las variables porque así me es más facil saber que tipo de dato tengo que poner para dados_cantidad y dados_caras. No se si lo vimos, pero lo hice solamente por eso
def tirar_dados(dados_cantidad: int, dados_caras: list):
    resultado_individual = []
    resultado_total = 0
    while True:
        for i in range(0,dados_cantidad):
            numero = random.randint(1,dados_caras[i])
            resultado_individual.append(numero)
            resultado_total += numero
        return [resultado_individual, resultado_total]


def estadisticas(cambios, tiros, grantotal, cantidadmini, cantidadmaxi):
    while True:
        eleccion = None
        while type(eleccion) != int:
            print("Introduzca qué estadística desea ver:")    
            print("  1: Cantidad de veces que se cambiaron los dados.")
            print("  2: Cantidad de tiros realizados.")
            print("  3: La suma total de todos los dados lanzados.")
            print("  4: Cantidad de veces que salió el número más bajo.")
            print("  5: Cantidad de veces que salió el número más alto.")
            print("  0: Volver al inicio.")
            eleccion = input("Usted elige: ")
            if eleccion in ["1", "2", "3", "4", "5", "0"]:
                eleccion = int(eleccion)
            else:
                print("Su elección no es válida, por favor ingrese solo un número.")
        if eleccion == 1:
            print(f"Se han realizado {cambios} cambios a los dados.\n")
        elif eleccion == 2:
            print(f"Se han realizado {tiros} tiros.\n")
        elif eleccion == 3:
            print(f"La suma total de todos los dados lanzados es de {grantotal}.\n")
        elif eleccion == 4:
            print(f"El número más bajo salió {cantidadmini} veces.\n")
        elif eleccion == 5:
            print(f"El número más alto salió {cantidadmaxi} veces.\n")
        elif eleccion == 0:
            print("Volviendo al inicio...")
            break


def vidente_main():
    while True:
        eleccion = None
        while type(eleccion) != int:
            print("¿Te sientes con suerte?")
            print("Los espíritus le invitan a introducir la opción que quiera realizar:")
            print("  1: Reglas del Juego.")
            print("  2: Jugar.")
            print("  3: Ver estadísticas de juego.")
            print("  0: Volver al inicio.")
            eleccion = input("Usted elige: ")
            if eleccion in ["1", "2", "3", "0"]:
                eleccion = int(eleccion)
            else:
                print("Los espíritus me dicen que su elección no es válida, le imploran que ingrese solo un número.")
        print("\nLos espíritus me dicen que usted ha elegido:", end=" ")
        if eleccion == 1:
            print("Revisar las reglas del juego...\n\n")
            vidente_reglas()
        elif eleccion == 2:
            print("Jugar...")
            vidente_play()
        elif eleccion == 3:
            print("Ver las estadísticas de sus partidas.")
        elif eleccion == 0:
            print("Volver al inicio\nLos espíritus te saludan, desean que la fortuna esté de tu lado...")
            print("Volviendo al inicio...")
            break


def vidente_reglas():
    print("Los espíritus se acercan, sientes que quieren compartir algo contigo...")
    print("\"'El Vidente' es un juego de dados jugado por magos, adivinos y clarividentes.")
    print("Apostaban para ver quién era el mejor prediciendo el futuro.")
    print("Podían jugarlo varias personas a la vez, y por varias rondas.")
    print("La partida más larga registrada fue entre dos poderosos videntes,")
    print("María Simma, con tan solo unos 23 años de edad,")
    print("y el propio espíritu de Nostradamus, que había muerto siglos antes.\"")
    input("Presione 'Enter' para continuar...")
    print("\n\"Las reglas son simples, pues se juega con un solo dado de 10 caras.")
    print("Un jugador debe tirar el dado, y el resto deben intentar adivinar,")
    print("con la mayor exactitud posible, en qué cara caerá.")
    print("Si están a 5 números o más de distancia, obtendrán 1 punto, 'Burro'.")
    print("Si están a 3 o 4 números de distancia, obtendrán 2 puntos, 'Fortuna'.")
    print("Si están a 2 números de distancia, obtendrán 4 puntos, 'Hechicero'.")
    print("Si están a 1 número de distancia, obtendrán 8 puntos, 'Adivino'.")
    print("Y, por último, si predicen exactamente en qué cara caerá el dado,")
    print("obtendrán 20 puntos, un puntaje digno de un verdadero 'VIDENTE'.\"")
    input("Presione 'Enter' para continuar...")
    print("\n\"Al final del juego se sumarán los puntajes obtenidos en cada ronda,")
    print("y el jugador con el puntaje más alto será coronado 'Mejor Vidente' de la mesa.\"")
    print("\n\"Ya estás listo para jugar\n¿Te sientes con suerte?\"\n")
    print("Los espíritus se alejan...")
    input("Presione 'Enter' para volver al menú...")


def vidente_play():
    eleccion = None
    rondas = 5
    while type(eleccion) != int:
        print("Para iniciar una partida, elija cuántas rondas desea jugar:")
        print("  1: Partida corta (3 rondas)")
        print("  2: Partida media (5 rondas)")
        print("  3: Partida larga (8 rondas)")
        print("  4: Duelo Histórico (20 rondas)")
        print("  5: Custom")
        eleccion = input("Usted elige: ")
        if eleccion in ["1", "2", "3", "4", "5"]:
            eleccion = int(eleccion)
        else:
            print("Los espíritus me dicen que su elección no es válida, le imploran que ingrese solo un número")
    if eleccion == 1:
        rondas = 3
    elif eleccion == 2:
        rondas = 5
    elif eleccion == 3:
        rondas = 8
    elif eleccion == 4:
        rondas = 20
    elif eleccion == 5:
        rondas = None
        while type(rondas) != int:
            rondas = input("Ingrese la cantidad de rondas que desea jugar: ")
            for d in range(0, len(rondas)):
                if rondas[d] not in "1234567890":
                    print("No se ha ingresado un número")
                    break
                elif d +1 == len(rondas):
                    rondas = int(rondas)
    jugadores = None
    while type(jugadores) != int:
        jugadores = input("Ingrese la cantidad de jugadores (deben ser más de 2): ")
        for d in range(0, len(jugadores)):
            if jugadores[d] not in "1234567890":
                print("No se ha ingresado un número")
                break
            elif d +1 == len(jugadores):
                jugadores = int(jugadores)
                if jugadores < 2:
                    print(f"La cantidad de jugadores debe ser mayor que 1 (usted ingresó {jugadores})")
                    jugadores = None
    vidente_gameloop(rondas, jugadores)


def vidente_gameloop(rondas, jugadores):
    print("\n\nLos espíritus se acercan a ver la partida")
    print("Antes de comenzar, asignen cuál jugador es el 1,")
    print("cuál es el 2, y así con el resto.")
    print("Jugar primero o último da igual, pero si no pueden decidirse,")
    print("El jugador a la izquierda del todo será el 1")
    print("y el siguiente será el 2, y así hasta llegar a la derecha")
    input("Una vez se hayan decidido, presionen 'Enter'...")
    ganador = [0]
    ganador_puntaje = 0
    puntajes = []
    for jugador in range(0,jugadores):
        puntajes.append(0)
    for ronda in range(0, rondas):
        print(f"\n\n\t\tRONDA {ronda + 1}")
        for tirador in range(0, jugadores):
            print(f"\n\nTurno del jugador {tirador + 1} de tirar los dados")
            predicciones = []
            for jugador in range(0, jugadores):
                if tirador == jugador:
                    predicciones.append("tirador")
                else:
                    prediccion_individual = None
                    while type(prediccion_individual) != int:
                        print(f"Jugador {jugador + 1}, realice su predicción.")
                        prediccion_individual = input("Elija un número del 1 al 10: ")
                        if prediccion_individual in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                            prediccion_individual = int(prediccion_individual)
                        else:
                            print("Los espíritus dicen que su predicción no es válida,")
                            print("le imploran que ingrese un número del 1 al 10")
                    predicciones.append(prediccion_individual)
            print("Ahora que todos los jugadores hicieron sus predicciones,")
            print(f"el jugador {tirador + 1} tirará los dados")
            temporal = tirar_dados(1, [10])
            resultado = temporal[1]
            print(f"El dado ha caído en...\n\t ¡{resultado}!")
            input("Presione 'Enter' para continuar...")
            for jugador in range(0, jugadores):
                if tirador == jugador:
                    pass
                else:
                    puntaje_individual = resultado - predicciones[jugador]
                    print(f"\nEl jugador {jugador + 1} predijo el numero {predicciones[jugador]}")
                    if puntaje_individual >= 5 or puntaje_individual <= -5:
                        print("BURRO - su predicción se encuentra a más de 5 de distancia")
                        print(f"El jugador {jugador + 1} obtiene 1 punto")
                        puntajes[jugador] = puntajes[jugador] + 1
                        input("Presione 'Enter' para continuar...")
                    elif puntaje_individual in [3, 4, -3, -4]:
                        print("FORTUNA - su predicción se encuentra a 3 o 4 de distancia")
                        print(f"El jugador {jugador + 1} obtiene 2 puntos")
                        puntajes[jugador] = puntajes[jugador] + 2
                        input("Presione 'Enter' para continuar...")
                    elif puntaje_individual in [2, -2]:
                        print("MAGO - su predicción se encuentra a 2 de distancia")
                        print(f"El jugador {jugador + 1} obtiene 4 puntos")
                        puntajes[jugador] = puntajes[jugador] + 4
                        input("Presione 'Enter' para continuar...")
                    elif puntaje_individual in [1, -1]:
                        print("ADIVINO - su predicción se encuentra a 1 de distancia")
                        print(f"El jugador {jugador + 1} obtiene 8 puntos")
                        puntajes[jugador] = puntajes[jugador] + 8
                        input("Presione 'Enter' para continuar...")
                    elif puntaje_individual == 0:
                        print("¡VIDENTE! - su predicción es correcta")
                        print(f"El jugador {jugador + 1} obtiene 20 puntos")
                        puntajes[jugador] = puntajes[jugador] + 20
                        input("Presione 'Enter' para continuar...")
    print("\n\nY así, acabó la partida")
    print("Los espiritus revolotean, ansiosos por revelar los puntajes")
    for jugador in range(0, jugadores):
        print(f"El jugador {jugador + 1} obtuvo {puntajes[jugador]} puntos")
        if puntajes[jugador] > ganador_puntaje:
            ganador = [jugador]
            ganador_puntaje = puntajes[jugador]
        elif puntajes[jugador] == ganador_puntaje:
            ganador.append(jugador)
    if len(ganador) == 1:
        print(f"Por lo tanto... ¡El jugador {int(ganador[0] + 1)} gana con {ganador_puntaje} puntos!\n\n")
    elif len(ganador) > 1:
        ganadores = []
        for i in ganador:
            ganadores.append(i+1)
        ganadores = str(ganadores)[1:-1].replace(",", " y")
        print("Por lo tanto... Oh... ¡Qué cosa tan inusual!")
        print("¡Ha habido un empate!")
        print(f"¡Los ganadores han sido los jugadores {ganadores} con {ganador_puntaje} puntos!\n\n")
    input("Presione 'Enter' para volver al menu...")


def main():
    dados_cantidad = 1
    dados_caras = [6]
    estadistica_tiros = 0
    estadistica_cambios = 0
    estadistica_grantotal = 0
    estadistica_cantidadmini = 0
    estadistica_cantidadmaxi = 0
    while True:
        print(f"\nEl siguiente tiro será:\n  Cantidad de Dados: {dados_cantidad}\n  Cara de los dados: {str(dados_caras)[1:-1]}\n")
        eleccion = None
        while type(eleccion) != int:
            print("Introduzca la opción que quiera realizar:")
            print("  1: Cambiar los dados")
            print("  2: Hacer un tiro")
            print("  3: Ver estadísticas")
            print("  4: Jugar 'El Vidente'")
            print("  0: Salir del programa")
            eleccion = input("Usted elige: ")
            if eleccion in ["1", "2", "3", "4", "0"]:
                eleccion = int(eleccion)
            else:
                print("Su elección no es válida, por favor ingrese solo un número")
        print("\nUsted ha elegido:", end=" ")
        if eleccion == 1:
            print("Cambiar los dados")
            estadistica_cambios += 1
            cambios = cambiar_dados()
            dados_cantidad = cambios[0]
            dados_caras = cambios[1]
            continue
        elif eleccion == 2:
            print("Hacer un tiro")
            while True:
                estadistica_tiros += 1
                temporal = tirar_dados(dados_cantidad, dados_caras)
                resultado_individual = temporal[0]
                resultado_total = temporal[1]
                estadistica_grantotal += resultado_total
                for resultado in resultado_individual:
                    if resultado == 1:
                        estadistica_cantidadmini += 1
                    if resultado == dados_caras[0]:
                        estadistica_cantidadmaxi += 1
                print(f"El resultado de los dados es: {str(resultado_individual)[1:-1]}\nEl total de los dados es: {resultado_total}")
                volver_a_tirar = input("Quiere realizar otro tiro? (SI/NO): ")
                while volver_a_tirar.upper() not in ["SI", "S", "Y", "NO", "N"]:
                    volver_a_tirar = input("No se ha ingresado una respuesta válida\nQuiere realizar otro tiro? (SI/NO): ")
                if volver_a_tirar.upper() in ["SI", "S", "Y"]:
                    print("\nRealizando otro tiro...")
                    continue
                elif volver_a_tirar.upper() in ["NO", "N"]:
                    break
            continue
        elif eleccion == 3:
            print("Ver estadísticas")
            estadisticas(estadistica_cambios, estadistica_tiros, estadistica_grantotal, estadistica_cantidadmini, estadistica_cantidadmaxi)
        elif eleccion == 4:
            print("Jugar 'El Vidente'")
            print("\n\nEntrando a...\n EL VIDENTE\n\n")
            input("Presione 'Enter' para iniciar...")
            vidente_main()
        elif eleccion == 0:
            print("Salir del programa\n\n")
            break


print("\n\nBIENVENIDO A SIMULADOR DADOS 2024\n\n")
input("Presione 'Enter' para iniciar...")
print()
main()
print("SALIENDO DEL SIMULADOR DADOS 2024\n       Nos vemos pronto ;)\n\n")
input("Presione 'Enter' para salir...")