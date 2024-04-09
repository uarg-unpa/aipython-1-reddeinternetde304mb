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
        #revisa que la elección sea "1" o "2"
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

###Aclaración: le asigno un tipo a las variables porque así me es más facil saber que tipo de dato tengo
### que poner para dados_cantidad y dados_caras. No se si lo vimos, pero lo hice solamente por eso
def tirar_dados(dados_cantidad: int, dados_caras: list):
    resultado_individual = []
    resultado_total = 0
    #Para cada tiro, consigo un numero random desde 1 a la cantidad de cara del dado.
    #Si hay más de un dado, la variable i indicará que cara de dados_caras debe utilizar
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
            #revisa que la elección sea un numero de las opciones ("1", "2", "3", "4", "5" o "0")
            if eleccion in ["1", "2", "3", "4", "5", "0"]:
                eleccion = int(eleccion)
            else:
                print("Su elección no es válida, por favor ingrese solo un número.")
        match eleccion:
            case 1:
                print(f"\nSe han realizado {cambios} cambios a los dados.")
                input("Presione 'Enter' para continuar...")
                print()
            case 2:
                print(f"\nSe han realizado {tiros} tiros.")
                input("Presione 'Enter' para continuar...")
                print()
            case 3:
                print(f"\nLa suma total de todos los dados lanzados es de {grantotal}.")
                input("Presione 'Enter' para continuar...")
                print()
            case 4:
                print(f"\nEl número más bajo salió {cantidadmini} veces.")
                input("Presione 'Enter' para continuar...")
                print()
            case 5:
                print(f"\nEl número más alto salió {cantidadmaxi} veces.")
                input("Presione 'Enter' para continuar...")
                print()
            case 0:
                print("\nVolviendo al inicio...")
                break


def vidente_main(estadistica_partidasjugadas, estadistica_empates, estadistica_num, estadistica_titulos, estadistica_jugadoresyganador, estadistica_rondasypuntajes):
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
            #revisa que la elección sea una de las opciones ("1", "2", "3" o "0")
            if eleccion in ["1", "2", "3", "0"]:
                eleccion = int(eleccion)
            else:
                print("Los espíritus me dicen que su elección no es válida, le imploran que ingrese solo un número.")
        print("\nLos espíritus me dicen que usted ha elegido:", end=" ")
        match eleccion:
            case 1:
                print("Revisar las reglas del juego...\n\n")
                vidente_reglas()
                continue
            case 2:
                print("Jugar...")
                #vidente_play() recibe algunas estadisticas para que modificarlas durante la partida.
                #En general, todas las estadísticas de "El Vidente" provienen de la partida, por lo que
                # el return() de la función es una lista con cada estadística.
                #Los valores del return son luego asignados (sumandolos o haciendoles append a una lista)
                # a los valores de cada estadística individual
                estadisticas = vidente_play(estadistica_empates, estadistica_num, estadistica_titulos)
                estadistica_partidasjugadas += 1
                #estadistica_empates, num y titulos ya fueron modificadas durante vidente_play(),
                # por lo que solo hace falta asignarlas, no sumarlas o appendearlas
                estadistica_empates = estadisticas[0]
                estadistica_num = estadisticas[1]
                estadistica_titulos = estadisticas[2]
                #
                #estadistica_jugadoresyganador = [jugadores, [lista_veces_que_cada_jugador_ganó]]
                # ej. estadistica_jugadoresyganador = [2, [3, 5]]
                #estadisticas[3] = [jugadores, quién_ganó (o quiénes, si es que hubo un empate)]
                #Primero, revisa que la cantidad de jugadores de estadistica_jugadoresyganador sea igual o
                # mayor a la cantidad de jugadores que participaron de la partida.
                # De no ser así, cambia el valor y le agrega 0 a la lista_veces_que_cada_jugador_ganó
                # por cada jugador que hay (osea, si habían 2 jugadores en la lista y pasan a ser 4,
                # agregará 2 veces 0 a la lista, porque 4-2 = 2
                if estadistica_jugadoresyganador[0] < estadisticas[3][0]:
                    estadistica_jugadoresyganador[0] = estadisticas[3][0]
                    while len(estadistica_jugadoresyganador[1]) < estadistica_jugadoresyganador[0]:
                        estadistica_jugadoresyganador[1].append(0)
                #Luego, revisa quien es el ganador (o ganadores) de la partida y le suma 1 a la
                # catidad de veces que ese jugador ganó en la lista_veces_que_cada_jugador_ganó
                for ganador in estadisticas[3][1]:
                    estadistica_jugadoresyganador[1][ganador] += 1
                #
                #estadistica_rondasypuntajes = [[cantidad_rondas, puntaje_minimo, puntaje_maximo], [otra_cantidad_rondas, puntaje_minimo, puntaje_maximo]]
                # ej. estadistica_rondasypuntajes = [[3, 8, 24], [5, 12, 33]]
                #estadisticas[4] = [cantidad_rondas, cantidad_jugadores, puntajes]
                #En este caso solo hay que agregar la estadística de la partida a la estadistica_rondasypuntajes,
                # ya que estadistica_rondasypuntajes simplemente recibe listas con la
                # cantidad de rondas, de jugadores y sus puntajes
                estadistica_rondasypuntajes.append(estadisticas[4])
                continue
            case 3:
                print("Ver las estadísticas de sus partidas...")
                #Revisa que ya se haya jugado una partida (la gran mayoría
                # de estadísticas no tienen sentido si no se ha jugado nunca)
                if estadistica_partidasjugadas < 1:
                    print("Los espíritus se encuentran tristes,")
                    print("pues todavía no se ha jugado ninguna partida.")
                    print("Como no pueden hablarte de estadísticas,")
                    print("te invitan a jugar...")
                    input("Presione 'Enter' para continuar...")
                    print()
                else:
                    vidente_estadisticas(estadistica_partidasjugadas, estadistica_empates, estadistica_num, estadistica_titulos, estadistica_jugadoresyganador, estadistica_rondasypuntajes)
                continue
            case 0:
                print("Volver al inicio...\nLos espíritus te saludan, desean que la fortuna esté de tu lado...")
                print("Volviendo al inicio...")
                return(estadistica_partidasjugadas, estadistica_empates, estadistica_num, estadistica_titulos, estadistica_jugadoresyganador, estadistica_rondasypuntajes)


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
    print("(Los puntajes totales no se revelarán hasta el final de la partida para generar suspenso)")
    print("\n\"Ya estás listo para jugar\n¿Te sientes con suerte?\"\n")
    print("Los espíritus se alejan...")
    input("Presione 'Enter' para volver al menú...")


def vidente_play(estadistica_empates, estadistica_num, estadistica_titulos):
    #estadistica_num = [1:[predicciones, resultados], 2:[...], 3:[...], ... 10:[...]]  -  (me encantaría usar un diccionario)
    #estadictica_titulos = [burro, fortuna, hechicero, adivino, vidente]
    eleccion = None
    while type(eleccion) != int:
        print("Para iniciar una partida, elija cuántas rondas desea jugar:")
        print("  1: Partida corta (3 rondas).")
        print("  2: Partida media (5 rondas).")
        print("  3: Partida larga (8 rondas).")
        print("  4: Duelo Histórico (20 rondas).")
        print("  5: Custom.")
        eleccion = input("Usted elige: ")
        #revisa que eleccion sea una de las opciones ("1", "2", "3", "4" o "5")
        if eleccion in ["1", "2", "3", "4", "5"]:
            eleccion = int(eleccion)
        else:
            print("Los espíritus me dicen que su elección no es válida, le imploran que ingrese solo un número.")
    match eleccion:
        case 1:
            rondas = 3
        case 2:
            rondas = 5
        case 3:
            rondas = 8
        case 4:
            rondas = 20
        case 5:
            rondas = None
            while type(rondas) != int:
                rondas = input("Ingrese la cantidad de rondas que desea jugar: ")
                #Esto es como un isdigit(), revisa cada carácter del input para ver que todos sean números,
                # y cuando llega al último carácter, si todos eran números, lo pasa a int y sigue adelante
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
        jugadores = input("Ingrese la cantidad de jugadores (deben ser 2 o más): ")
        #Funciona igual que el for loop anterior
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
    puntajes = []
    #Primero agrega un 0 por cada jugador a la variable puntajes
    for jugador in range(0,jugadores):
        puntajes.append(0)
    #Aquí comienza el loop de la partida, loopea cada ronda, y luego cada jugador,
    # cosa que en todas las rondas todos los jugadores tiren los dados
    for ronda in range(1, rondas +1):
        print(f"\n\n\t\tRONDA {ronda}")
        for tirador in range(0, jugadores):
            print(f"\n\nTurno del jugador {tirador + 1} de tirar los dados")
            predicciones = []
            #Aquí cada jugador realiza la predicción de qué número va a salir
            for jugador in range(0, jugadores):
                if tirador == jugador:
                    #Si el jugador es el tirador, no se debe hacer predicción
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
            #asigna una variable resultado al resultado_total de tirar_dados()
            resultado = temporal[1]
            #Esto es para las estadísticas de los números
            match resultado:
                case 1:
                    estadistica_num[0][1] += 1
                case 2:
                    estadistica_num[1][1] += 1
                case 3:
                    estadistica_num[2][1] += 1
                case 4:
                    estadistica_num[3][1] += 1
                case 5:
                    estadistica_num[4][1] += 1
                case 6:
                    estadistica_num[5][1] += 1
                case 7:
                    estadistica_num[6][1] += 1
                case 8:
                    estadistica_num[7][1] += 1
                case 9:
                    estadistica_num[8][1] += 1
                case 10:
                    estadistica_num[9][1] += 1
            print(f"El dado ha caído en...\n\t ¡{resultado}!")
            input("Presione 'Enter' para continuar...")
            #Aquí, compara las predicciones con el resultado y calcula los puntajes de cada jugador
            for jugador in range(0, jugadores):
                if tirador == jugador:
                    #Si el jugador es el tirador, no se debe calcular puntaje
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
                        print("HECHICERO - su predicción se encuentra a 2 de distancia.")
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
    #Luego de todas las rondas, calcula quién ganó
    print("\n\nY así, acabó la partida.")
    print("Los espiritus revolotean, ansiosos por revelar los puntajes...")
    input("Presione 'Enter' para continuar...")
    ganador = []
    ganador_puntaje = 0
    #Revisa si el puntaje de cada jugador es mayor que el del ganador.
    # Para el primer jugador, con que su puntaje sea mayor que 0, ya se lo coloca como ganador.
    # Luego, compara el puntaje de los demas jugadores con el de ese primer jugador, y si alguno lo
    # sobrepasa, pasará a ser el ganador y ganador_puntaje se actualiza.
    # Así, ganador y ganador_puntaje terminan teniendo la información del jugador con el mayor puntaje
    #Además, si hay dos jugadores con el puntaje más alto, al final la variable ganador tendrá más de un ítem,
    # por lo que el programa reconocerá a 2 ganadores (o los que sea), es decir, habrá un empate
    for jugador in range(0, jugadores):
        print(f"\nEl jugador {jugador + 1} obtuvo {puntajes[jugador]} puntos")
        if puntajes[jugador] > ganador_puntaje:
            ganador = [jugador]
            ganador_puntaje = puntajes[jugador]
        elif puntajes[jugador] == ganador_puntaje:
            ganador.append(jugador)
        input("Presione 'Enter' para continuar...")
    #Revisa que haya un solo ganador, o más de 1, en cuyo caso habrá un empate
    if len(ganador) == 1:
        print(f"\nPor lo tanto... ¡El jugador {ganador[0] + 1} gana con {ganador_puntaje} puntos!¡Felicitaciones!\n\n")
    elif len(ganador) > 1:
        #ganadores_string es tan solo una string formateada que nombra a los ganadores
        ganadores_string = []
        for i in ganador:
            ganadores_string.append(i+1)
        ganadores_string = str(ganadores_string)[1:-1].replace(",", " y")
        print("\nPor lo tanto... Oh... ¡Qué cosa tan inusual!")
        print(f"¡Ha habido un empate!¡Un empate entre {len(ganador)}!")
        print(f"¡Los ganadores han sido los jugadores {ganadores_string} con {ganador_puntaje} puntos!¡Felicitaciones!\n\n")
        estadistica_empates += 1
    input("Presione 'Enter' para volver al menú...")
    #Al final, vidente_play() usa un return() para devolver una lista con valores que serán utilizados 
    # para actualizar las estadísticas
    return [estadistica_empates, estadistica_num, estadistica_titulos, [jugadores, ganador], [rondas, jugadores, puntajes]]


def vidente_estadisticas(partidasjugadas, empates, numeros, titulos, jugadoresyganador, rondasypuntajes):
    while True:
        eleccion = None
        while type(eleccion) != int:
            print("Los espíritus le invitan a introducir qué estadística desea ver:")    
            print("  1: Cantidad de partidas jugadas.")
            print("  2: Cantidad de empates.")
            print("  3: Información de cada número.")
            print("  4: Cantidad de veces que se recibió cada título (burro, vidente, etc).")
            print("  5: Cantidad de veces que ganó cada jugador.")
            print("  6: Los puntajes de cada partida.")
            print("  0: Volver al menú.")
            eleccion = input("Usted elige: ")
            #revisa que eleccion sea alguna de las opciones ("1", "2", "3", "4", "5", "6" o "0")
            if eleccion in ["1", "2", "3", "4", "5", "6", "0"]:
                eleccion = int(eleccion)
            else:
                print("Su elección no es válida, por favor ingrese solo un número.")
        match eleccion:
            case 1:
                if partidasjugadas == 1:
                    print(f"\nLos espíritus revolotean,\npues han presenciado {partidasjugadas} partida.")
                else:
                    print(f"\nLos espíritus revolotean,\npues han presenciado {partidasjugadas} partidas.")
                input("Presione 'Enter' para continuar...")
                print()
            case 2:
                if empates == 0:
                    print(f"\nLos espíritus dicen que han ocurrido\nun total de {empates} empates. Era de esperar.")
                elif empates == 1:
                    print(f"\nLos espíritus dicen que han ocurrido\nun total de {empates} empate. Wow, qué extraño.")
                else:
                    print(f"\nLos espíritus dicen que han ocurrido\nun total de {empates} empates. ¡Wow, más de 1!.")    
                input("Presione 'Enter' para continuar...")
                print()
            case 3:
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
            case 4:
                print("\nLos espíritus mostrarán para tí\nla cantidad de veces que se recibió cada título:")
                print(f"     BURRO | {titulos[0]}")
                print(f"   FORTUNA | {titulos[1]}")
                print(f" HECHICERO | {titulos[2]}")
                print(f"   ADIVINO | {titulos[3]}")
                print(f"   VIDENTE | {titulos[4]}")
                input("Presione 'Enter' para continuar...")
                print()
            case 5:
                print("\nLos espíritus saben quiénes han ganado y quiénes han perdido...")
                for jugador in range(0, jugadoresyganador[0]):
                    if jugadoresyganador[1][jugador] < 1:
                        print(f" El jugador {jugador +1} no ha ganado por ahora.")
                    elif jugadoresyganador[1][jugador] == 1:
                        print(f" El jugador {jugador +1} ha ganado {jugadoresyganador[1][jugador]} vez.")
                    else:
                        print(f" El jugador {jugador +1} ha ganado {jugadoresyganador[1][jugador]} veces.")
                input("Presione 'Enter' para continuar...")
                print()
            case 6:
                print("\nLos espítirus recuerdan los puntajes de cada partida...")
                for i in range(0, len(rondasypuntajes)):
                    print(f" En la partida {i+1}, con {rondasypuntajes[i][0]} rondas y {rondasypuntajes[i][1]} jugadores, los puntajes fueron:")
                    for j in range(0, len(rondasypuntajes[i][2])):
                        if rondasypuntajes[i][2][j] == 1:
                            print(f"  El jugador {j +1} obtuvo {rondasypuntajes[i][2][j]} punto")
                        else:
                            print(f"  El jugador {j +1} obtuvo {rondasypuntajes[i][2][j]} puntos")
                    input("Presione 'Enter' para continuar...")
                    print()
            case 0:
                print("\nVolviendo al menú...")
                break


def main():
    #defino una cantidad de dados y caras desde el principio
    dados_cantidad = 1
    dados_caras = [6]
    #defino estadísticas, las que dicen "vidente" son para el juego del mismo nombre
    estadistica_tiros = 0
    estadistica_cambios = 0
    estadistica_grantotal = 0
    estadistica_cantidadmini = 0
    estadistica_cantidadmaxi = 0
    estadistica_vidente_partidasjugadas = 0
    estadistica_vidente_empates = 0
    #estadistica_vidente_num = [num_1:[predicciones, resultados], num_2:[...], num_3:[...], ..., num_10:[predicciones, resultados]]
    estadistica_vidente_num = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    #estadictica_vidente_titulos = [cantidad_burro, cantidad_fortuna, cantidad_hechicero, cantidad_adivino, cantidad_vidente]
    estadistica_vidente_titulos = [0, 0, 0, 0, 0]
    #estadistica_vidente_jugadoresyganador = [jugadores, [lista_veces_que_cada_jugador_ganó]]
    estadistica_vidente_jugadoresyganador = [2, [0, 0]]
    #estadistica_vidente_rondasypuntajes = [[cantidad_rondas, cantidad_jugadores, puntajes], [cantidad_rondas_deotrapartida, cantidad_jugadores_deotrapartida, puntajes_deotrapartida]]
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
            #revisa que la elección sea una de las opciones dadas ("1", "2", "3", "4" o "0")
            if eleccion in ["1", "2", "3", "4", "0"]:
                eleccion = int(eleccion)
            else:
                print("Su elección no es válida, por favor ingrese solo un número.")
        print("\nUsted ha elegido:", end=" ")
        match eleccion:
            case 1:
                print("Cambiar los dados.")
                estadistica_cambios += 1
                cambios = cambiar_dados()
                #asignar los valores nuevos de caras y cantidad
                dados_cantidad = cambios[0]
                dados_caras = cambios[1]
                continue
            case 2:
                print("Hacer un tiro.")
                while True:
                    estadistica_tiros += 1
                    #temporal == [resultado_individual, resultado_total]
                    temporal = tirar_dados(dados_cantidad, dados_caras)
                    resultado_individual = temporal[0]
                    resultado_total = temporal[1]
                    #cambio 2 estadísticas: grantotal, que es el maximo de todos los resultados de dados tirados...
                    estadistica_grantotal += resultado_total
                    #y cantidadmini y maxi, que miden cuantas veces salió el dado más bajo (1) y más alto
                    for r in range(0, len(resultado_individual)):
                        if resultado_individual[r] == 1:
                            estadistica_cantidadmini += 1
                        if resultado_individual[r] == dados_caras[r]:
                            estadistica_cantidadmaxi += 1
                    print(f"El resultado de los dados es: {str(resultado_individual)[1:-1]}.\nEl total de los dados es: {resultado_total}.")
                    #pregunta si se quiere volver a realizar un tiro
                    volver_a_tirar = input("Quiere realizar otro tiro? (SI/NO): ")
                    #revisa si el input es correcto o se escribió cualquier cosa
                    while volver_a_tirar.upper() not in ["SI", "S", "Y", "NO", "N"]:
                        volver_a_tirar = input("No se ha ingresado una respuesta válida\nQuiere realizar otro tiro? (SI/NO): ")
                    if volver_a_tirar.upper() in ["SI", "S", "Y"]:
                        print("\nRealizando otro tiro...")
                        continue
                    elif volver_a_tirar.upper() in ["NO", "N"]:
                        break
                continue
            case 3:
                print("Ver estadísticas.")
                estadisticas(estadistica_cambios, estadistica_tiros, estadistica_grantotal, estadistica_cantidadmini, estadistica_cantidadmaxi)
                continue
            case 4:
                print("Jugar 'El Vidente'.")
                print("\n\nEntrando a...\n EL VIDENTE\n\n")
                input("Presione 'Enter' para iniciar...")
                #Para manejar las estadísticas en "El Vidente", le envío cada estadística a la función,
                #y al final de la misma hay un return que las devuelve con las estadísticas actualizadas.
                #Así, uno puede salir de El Vidente, volver a entrar, y las estadísticas se mantendrán
                estadisticas_vidente = vidente_main(estadistica_vidente_partidasjugadas, estadistica_vidente_empates, estadistica_vidente_num, estadistica_vidente_titulos, estadistica_vidente_jugadoresyganador, estadistica_vidente_rondasypuntajes)
                #ahora, utiliza cada estadística del return de la función vidente_main() para asignarlas a las estadísticas de main()
                estadistica_vidente_partidasjugadas = estadisticas_vidente[0]
                estadistica_vidente_empates = estadisticas_vidente[1]
                estadistica_vidente_num = estadisticas_vidente[2]
                estadistica_vidente_titulos = estadisticas_vidente[3]
                estadistica_vidente_jugadoresyganador = estadisticas_vidente[4]
                estadistica_vidente_rondasypuntajes = estadisticas_vidente[5]
                continue
            case 0:
                print("Salir del programa.\n\n")
                break


print("\n\nBIENVENIDO A SIMULADOR DADOS 2024\n\n")
input("Presione 'Enter' para iniciar...")
print()
main()
print("SALIENDO DEL SIMULADOR DADOS 2024\n       Nos vemos pronto ;)\n\n")
input("Presione 'Enter' para salir...")