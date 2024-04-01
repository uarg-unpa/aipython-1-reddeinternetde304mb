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
            print(f"\nSe han realizado {cambios} cambios a los dados.")
            input("Presione 'Enter' para continuar...")
            print()
        elif eleccion == 2:
            print(f"\nSe han realizado {tiros} tiros.")
            input("Presione 'Enter' para continuar...")
            print()
        elif eleccion == 3:
            print(f"\nLa suma total de todos los dados lanzados es de {grantotal}.")
            input("Presione 'Enter' para continuar...")
            print()
        elif eleccion == 4:
            print(f"\nEl número más bajo salió {cantidadmini} veces.")
            input("Presione 'Enter' para continuar...")
            print()
        elif eleccion == 5:
            print(f"\nEl número más alto salió {cantidadmaxi} veces.")
            input("Presione 'Enter' para continuar...")
            print()
        elif eleccion == 0:
            print("\nVolviendo al inicio...")
            break


def vidente_main(estadistica_num, estadistica_titulos, estadistica_empates, estadistica_jugadoresyganador, estadistica_rondasypuntajes):
    while True:
        eleccion = None
        while type(eleccion) != int:
            print("¿Te sientes con suerte?")
            print("Los espíritus le invitan a introducir la opción que quiera realizar:")
            print("  1: Reglas del juego.")
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
            continue
        elif eleccion == 2:
            print("Jugar...")
            estadisticas = vidente_play(estadistica_num, estadistica_titulos, estadistica_empates)
            estadistica_num = estadisticas[0]
            estadistica_titulos = estadisticas[1]
            estadistica_empates = estadisticas[2]
            #estadistica_jugadoresyganador = [jugadores, [lista_veces_que_cada_jugador_ganó]]
            # ej. estadistica_jugadoresyganador = [2, [3, 5]]
            #estadisticas[3] = [jugadores, quién_ganó (o quiénes, si es que hubo un empate)]
            if estadistica_jugadoresyganador[0] > estadisticas[3][0]:
                estadistica_jugadoresyganador[0] = estadisticas[3][0]
                while estadistica_jugadoresyganador[0] < len(estadistica_jugadoresyganador[1]):
                    estadistica_jugadoresyganador[1].append(0)
            for ganador in estadisticas[3][1]:
                estadistica_jugadoresyganador[1][ganador] += 1
            #estadistica_rondasypuntajes = [[cantidad_rondas, puntaje_minimo, puntaje_maximo], [otra_cantidad_rondas, puntaje_minimo, puntaje_maximo]]
            # ej. estadistica_rondasypuntajes = [[3, 8, 24], [5, 12, 33]]
            #estadisticas[4] = [cantidad_rondas, puntaje_minimo, ganador_puntaje(que vendría a ser el puntaje maximo)]
            if len(estadistica_rondasypuntajes) == 0:
                estadistica_rondasypuntajes.append(estadisticas[4])
            for i in range(0, len(estadistica_rondasypuntajes)):
                if estadisticas[4][0] == estadistica_rondasypuntajes[i][0]:
                    if estadisticas[4][1] < estadistica_rondasypuntajes[i][1]:
                        estadistica_rondasypuntajes[i][1] = estadisticas[4][1]
                    if estadisticas[4][2] > estadistica_rondasypuntajes[i][2]:
                        estadistica_rondasypuntajes[i][2] = estadisticas[4][2]
                else:
                    estadistica_rondasypuntajes.append(estadisticas[4])
            continue
        elif eleccion == 3:
            print("Ver las estadísticas de sus partidas...")
            vidente_estadisticas(estadistica_num, estadistica_titulos, estadistica_empates, estadistica_jugadoresyganador, estadistica_rondasypuntajes)
            continue
        elif eleccion == 0:
            print("Volver al inicio...\nLos espíritus te saludan, desean que la fortuna esté de tu lado...")
            print("Volviendo al inicio...")
            return(estadistica_num, estadistica_titulos, estadistica_empates, estadistica_jugadoresyganador, estadistica_rondasypuntajes)


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


def vidente_play(estadistica_num, estadistica_titulos, empates):
    #estadistica_num = [1:[predicciones, resultados], 2:[...], 3:[...], ... 10:[...]]  -  (me encantaría usar un diccionario)
    estadistica_num = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    #estadictica_titulos = [burro, fortuna, mago, adivino, vidente]
    estadistica_titulos = [0, 0, 0, 0, 0]
    empates = 0
    eleccion = None
    while type(eleccion) != int:
        print("Para iniciar una partida, elija cuántas rondas desea jugar:")
        print("  1: Partida corta (3 rondas).")
        print("  2: Partida media (5 rondas).")
        print("  3: Partida larga (8 rondas).")
        print("  4: Duelo Histórico (20 rondas).")
        print("  5: Custom.")
        eleccion = input("Usted elige: ")
        if eleccion in ["1", "2", "3", "4", "5"]:
            eleccion = int(eleccion)
        else:
            print("Los espíritus me dicen que su elección no es válida, le imploran que ingrese solo un número.")
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
                    print("No se ha ingresado un número.")
                    break
                elif d +1 == len(rondas):
                    rondas = int(rondas)
                    if rondas < 1:
                        rondas = None
                        print("Se necesita que la cantidad de rondas sea mayor que 0.")
    jugadores = None
    while type(jugadores) != int:
        jugadores = input("Ingrese la cantidad de jugadores (deben ser más de 2): ")
        for d in range(0, len(jugadores)):
            if jugadores[d] not in "1234567890":
                print("No se ha ingresado un número.")
                break
            elif d +1 == len(jugadores):
                jugadores = int(jugadores)
                if jugadores < 2:
                    jugadores = None
                    print("La cantidad de jugadores debe ser mayor que 1.")
    print("\n\nLos espíritus se acercan a ver la partida.")
    print("Antes de comenzar, asignen quién es el jugador 1,")
    print("quién es el 2, y así con el resto.")
    print("Jugar primero no da ventaja, pero si no pueden decidirse,")
    print("el jugador a la izquierda del todo será el 1,")
    print("y el siguiente será el 2, y así hasta llegar a la derecha.")
    input("Una vez se hayan decidido, presionen 'Enter'...")
    ganador = []
    ganador_puntaje = 0
    puntaje_minimo = 0
    puntajes = []
    for jugador in range(0,jugadores):
        puntajes.append(0)
    for ronda in range(1, rondas +1):
        print(f"\n\n\t\tRONDA {ronda}")
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
                            if prediccion_individual == 1:
                                estadistica_num[0][0] += 1
                            elif prediccion_individual == 2:
                                estadistica_num[1][0] += 1
                            elif prediccion_individual == 3:
                                estadistica_num[2][0] += 1
                            elif prediccion_individual == 4:
                                estadistica_num[3][0] += 1
                            elif prediccion_individual == 5:
                                estadistica_num[4][0] += 1
                            elif prediccion_individual == 6:
                                estadistica_num[5][0] += 1
                            elif prediccion_individual == 7:
                                estadistica_num[6][0] += 1
                            elif prediccion_individual == 8:
                                estadistica_num[7][0] += 1
                            elif prediccion_individual == 9:
                                estadistica_num[8][0] += 1
                            elif prediccion_individual == 10:
                                estadistica_num[9][0] += 1
                        else:
                            print("Los espíritus dicen que su predicción no es válida,")
                            print("le imploran que ingrese un número del 1 al 10.")
                    predicciones.append(prediccion_individual)
            print("Ahora que todos los jugadores hicieron sus predicciones,")
            print(f"el jugador {tirador + 1} tirará los dados...")
            temporal = tirar_dados(1, [10])
            resultado = temporal[1]
            if resultado == 1:
                estadistica_num[0][1] += 1
            elif resultado == 2:
                estadistica_num[1][1] += 1
            elif resultado == 3:
                estadistica_num[2][1] += 1
            elif resultado == 4:
                estadistica_num[3][1] += 1
            elif resultado == 5:
                estadistica_num[4][1] += 1
            elif resultado == 6:
                estadistica_num[5][1] += 1
            elif resultado == 7:
                estadistica_num[6][1] += 1
            elif resultado == 8:
                estadistica_num[7][1] += 1
            elif resultado == 9:
                estadistica_num[8][1] += 1
            elif resultado == 10:
                estadistica_num[9][1] += 1
            print(f"El dado ha caído en...\n\t ¡{resultado}!")
            input("Presione 'Enter' para continuar...")
            for jugador in range(0, jugadores):
                if tirador == jugador:
                    pass
                else:
                    puntaje_individual = resultado - predicciones[jugador]
                    print(f"\nEl jugador {jugador + 1} predijo el numero {predicciones[jugador]}.")
                    if puntaje_individual >= 5 or puntaje_individual <= -5:
                        print("BURRO - su predicción se encuentra a más de 5 de distancia.")
                        print(f"El jugador {jugador + 1} obtiene 1 punto.")
                        puntajes[jugador] += 1
                        estadistica_titulos[0] += 1
                        input("Presione 'Enter' para continuar...")
                    elif puntaje_individual in [3, 4, -3, -4]:
                        print("FORTUNA - su predicción se encuentra a 3 o 4 de distancia.")
                        print(f"El jugador {jugador + 1} obtiene 2 puntos.")
                        puntajes[jugador] += 2
                        estadistica_titulos[1] += 1
                        input("Presione 'Enter' para continuar...")
                    elif puntaje_individual in [2, -2]:
                        print("MAGO - su predicción se encuentra a 2 de distancia.")
                        print(f"El jugador {jugador + 1} obtiene 4 puntos.")
                        puntajes[jugador] += 4
                        estadistica_titulos[2] += 1
                        input("Presione 'Enter' para continuar...")
                    elif puntaje_individual in [1, -1]:
                        print("ADIVINO - su predicción se encuentra a 1 de distancia.")
                        print(f"El jugador {jugador + 1} obtiene 8 puntos.")
                        puntajes[jugador] += 8
                        estadistica_titulos[3] += 1
                        input("Presione 'Enter' para continuar...")
                    elif puntaje_individual == 0:
                        print("¡VIDENTE! - su predicción es correcta.")
                        print(f"El jugador {jugador + 1} obtiene 20 puntos.")
                        puntajes[jugador] += 20
                        estadistica_titulos[4] += 1
                        input("Presione 'Enter' para continuar...")
    print("\n\nY así, acabó la partida.")
    print("Los espiritus revolotean, ansiosos por revelar los puntajes...")
    puntaje_minimo = puntajes[0]
    for jugador in range(0, jugadores):
        print(f"El jugador {jugador + 1} obtuvo {puntajes[jugador]} puntos")
        if puntajes[jugador] > ganador_puntaje:
            ganador = [jugador]
            ganador_puntaje = puntajes[jugador]
        elif puntajes[jugador] == ganador_puntaje:
            ganador.append(jugador)
        if puntajes[jugador] < puntaje_minimo:
            puntaje_minimo = puntajes[jugador]
        input("Presione 'Enter' para continuar...")
    if len(ganador) == 1:
        print(f"Por lo tanto... ¡El jugador {int(ganador[0] + 1)} gana con {ganador_puntaje} puntos!¡Felicitaciones!\n\n")
    elif len(ganador) > 1:
        ganadores_string = []
        for i in ganador:
            ganadores_string.append(i+1)
        ganadores_string = str(ganadores_string)[1:-1].replace(",", " y")
        print("Por lo tanto... Oh... ¡Qué cosa tan inusual!")
        print(f"¡Ha habido un empate!¡Un empate entre {len(ganador)}!")
        print(f"¡Los ganadores han sido los jugadores {ganadores_string} con {ganador_puntaje} puntos!¡Felicitaciones!\n\n")
        empates += 1
    input("Presione 'Enter' para volver al menú...")
    return [estadistica_num, estadistica_titulos, empates, [jugadores, ganador], [rondas, puntaje_minimo, ganador_puntaje]]


def vidente_estadisticas(numeros, titulos, empates, jugadoresyganador, rondasypuntajes):
    while True:
        eleccion = None
        while type(eleccion) != int:
            print("Los espíritus le invitan a introducir qué estadística desea ver:")    
            print("  1: Información de cada número.")
            print("  2: Cantidad de veces que se recibió cada título (burro, vidente, etc).")
            print("  3: Cantidad de empates.")
            print("  4: Cantidad de veces que ganó cada jugador.")
            print("  5: Los puntajes más bajos y más altos.")
            print("  0: Volver al inicio.")
            eleccion = input("Usted elige: ")
            if eleccion in ["1", "2", "3", "4", "5", "0"]:
                eleccion = int(eleccion)
            else:
                print("Su elección no es válida, por favor ingrese solo un número.")
        if eleccion == 1:
            print("\nLos espíritus mostrarán para tí\nla información de cada número del dado:")
            print( " Num|Predicciones       |Resultados     |")
            print( " ---|-------------------|---------------|")
            print(f"  1 |  {numeros[0][0]}\t\t|  {numeros[0][1]}\t\t|")
            print(f"  2 |  {numeros[1][0]}\t\t|  {numeros[1][1]}\t\t|")
            print(f"  3 |  {numeros[2][0]}\t\t|  {numeros[2][1]}\t\t|")
            print(f"  4 |  {numeros[3][0]}\t\t|  {numeros[3][1]}\t\t|")
            print(f"  5 |  {numeros[4][0]}\t\t|  {numeros[4][1]}\t\t|")
            print(f"  6 |  {numeros[5][0]}\t\t|  {numeros[5][1]}\t\t|")
            print(f"  7 |  {numeros[6][0]}\t\t|  {numeros[6][1]}\t\t|")
            print(f"  8 |  {numeros[7][0]}\t\t|  {numeros[7][1]}\t\t|")
            print(f"  9 |  {numeros[8][0]}\t\t|  {numeros[8][1]}\t\t|")
            print(f" 10 |  {numeros[9][0]}\t\t|  {numeros[9][1]}\t\t|")
            print("(Predicciones: cantidad de veces que un jugador predijo ese número, haya acertado o no).")
            print("(Resultados: cantidad de veces que ese número salió como resultado de un tiro).")
            input("Presione 'Enter' para continuar...")
            print()
        elif eleccion == 2:
            print("\nLos espíritus mostrarán para tí\nla cantidad de veces que se recibió cada título:")
            print(f" BURRO:   {titulos[0]}")
            print(f" FORTUNA: {titulos[1]}")
            print(f" MAGO:    {titulos[2]}")
            print(f" ADIVINO: {titulos[3]}")
            print(f" VIDENTE: {titulos[4]}")
            input("Presione 'Enter' para continuar...")
            print()
        elif eleccion == 3:
            if empates == 0:
                print(f"\nLos espíritus dicen que han ocurrido\nun total de {empates} empates. Era de esperar.")
                input("Presione 'Enter' para continuar...")
                print()
            else:
                print(f"\nLos espíritus dicen que han ocurrido\nun total de {empates} empates. Wow, qué extraño.")
                input("Presione 'Enter' para continuar...")
                print()
        elif eleccion == 4:
            print("\nLos espíritus saben quiénes han ganado y quiénes han perdido...")
            for jugador in range(0, jugadoresyganador[0]):
                print(f" El jugador {jugador +1} ha ganado {jugadoresyganador[1][jugador]} veces.")
            input("Presione 'Enter' para continuar...")
            print()
        elif eleccion == 5:
            print("\nLos espítirus saben los peores y mejores puntajes...")
            for info_ronda in rondasypuntajes:
                print(f" Con {info_ronda[0]} rondas, el puntaje más bajo fue {info_ronda[1]}, y el más alto fue {info_ronda[2]}.")
                print("(Tenga en cuenta que, con menos jugadores, menores puntajes, y con más jugadores, mayores puntajes).")
                #####Quizá modificarlo para que tenga en cuenta la cantidad de jugadores también, y no solo las rondas
                input("Presione 'Enter' para continuar...")
                print()
        elif eleccion == 0:
            print("\nVolviendo al menú...")
            break


def main():
    dados_cantidad = 1
    dados_caras = [6]
    estadistica_tiros = 0
    estadistica_cambios = 0
    estadistica_grantotal = 0
    estadistica_cantidadmini = 0
    estadistica_cantidadmaxi = 0
    #estadistica_vidente_num = [1:[predicciones, resultados], 2:[...], 3:[...], ..., 10:[predicciones, resultados]]
    estadistica_vidente_num = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    #estadictica_vidente_titulos = [burro, fortuna, mago, adivino, vidente]
    estadistica_vidente_titulos = [0, 0, 0, 0, 0]
    estadistica_vidente_empates = 0
    #estadistica_vidente_jugadoresyganador = [jugadores, [lista_veces_que_cada_jugador_ganó]]
    estadistica_vidente_jugadoresyganador = [2, [0, 0]]
    #estadistica_vidente_rondasypuntajes = [[cantidad_rondas, puntaje_minimo, puntaje_maximo], [otra_cantidad_rondas, puntaje_minimo, puntaje_maximo]]
    estadistica_vidente_rondasypuntajes = []
    while True:
        print(f"\nEl siguiente tiro será:\n  Cantidad de Dados: {dados_cantidad}\n  Cara de los dados: {str(dados_caras)[1:-1]}\n")
        eleccion = None
        while type(eleccion) != int:
            print("Introduzca la opción que quiera realizar:")
            print("  1: Cambiar los dados.")
            print("  2: Hacer un tiro.")
            print("  3: Ver estadísticas.")
            print("  4: Jugar 'El Vidente'.")
            print("  0: Salir del programa.")
            eleccion = input("Usted elige: ")
            if eleccion in ["1", "2", "3", "4", "0"]:
                eleccion = int(eleccion)
            else:
                print("Su elección no es válida, por favor ingrese solo un número.")
        print("\nUsted ha elegido:", end=" ")
        if eleccion == 1:
            print("Cambiar los dados.")
            estadistica_cambios += 1
            cambios = cambiar_dados()
            dados_cantidad = cambios[0]
            dados_caras = cambios[1]
            continue
        elif eleccion == 2:
            print("Hacer un tiro.")
            while True:
                estadistica_tiros += 1
                temporal = tirar_dados(dados_cantidad, dados_caras)
                resultado_individual = temporal[0]
                resultado_total = temporal[1]
                estadistica_grantotal += resultado_total
                for r in range(0, len(resultado_individual)):
                    if resultado_individual[r] == 1:
                        estadistica_cantidadmini += 1
                    if resultado_individual[r] == dados_caras[r]:
                        estadistica_cantidadmaxi += 1
                print(f"El resultado de los dados es: {str(resultado_individual)[1:-1]}.\nEl total de los dados es: {resultado_total}.")
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
            print("Ver estadísticas.")
            estadisticas(estadistica_cambios, estadistica_tiros, estadistica_grantotal, estadistica_cantidadmini, estadistica_cantidadmaxi)
            continue
        elif eleccion == 4:
            print("Jugar 'El Vidente'.")
            print("\n\nEntrando a...\n EL VIDENTE\n\n")
            input("Presione 'Enter' para iniciar...")
            estadisticas_vidente = vidente_main(estadistica_vidente_num, estadistica_vidente_titulos, estadistica_vidente_empates, estadistica_vidente_jugadoresyganador, estadistica_vidente_rondasypuntajes)
            estadistica_vidente_num = estadisticas_vidente[0]
            estadistica_vidente_titulos = estadisticas_vidente[1]
            estadistica_vidente_empates = estadisticas_vidente[2]
            estadistica_vidente_jugadoresyganador = estadisticas_vidente[3]
            estadistica_vidente_rondasypuntajes = estadisticas_vidente[4]
            continue
        elif eleccion == 0:
            print("Salir del programa.\n\n")
            break


print("\n\nBIENVENIDO A SIMULADOR DADOS 2024\n\n")
input("Presione 'Enter' para iniciar...")
print()
main()
print("SALIENDO DEL SIMULADOR DADOS 2024\n       Nos vemos pronto ;)\n\n")
input("Presione 'Enter' para salir...")