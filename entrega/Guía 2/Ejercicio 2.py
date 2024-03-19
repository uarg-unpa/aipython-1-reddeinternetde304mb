edad_1 = int(input("¡Verifique quien es el mayor de dos personas!\nIngrese la edad del primer participante: "))
edad_2 = int(input("Ahora ingrese la edad del segundo participante: "))

if edad_1 > edad_2:
    diferencia = edad_1 - edad_2
    if diferencia == 1:
        print(f"¡El primer participante es mayor! Tienen {diferencia} año de diferencia")
    else:
        print(f"¡El primer participante es mayor! Tienen {diferencia} años de diferencia")
elif edad_1 < edad_2:
    diferencia = edad_2 - edad_1
    if diferencia == 1:
        print(f"¡El segundo participante es mayor! Tienen {diferencia} año de diferencia")
    else:
        print(f"¡El segundo participante es mayor! Tienen {diferencia} años de diferencia")
elif edad_1 == edad_2:
    print(f"Pero...\nPero si tienen la misma edad...\n¿No te diste cuenta?\nDigo, tuviste que escribir {edad_1} y luego {edad_2},\nosea,\n¿escribiste {edad_1} dos veces y no paraste a pensar que tenían la misma edad?\n\n\nTerrible...")