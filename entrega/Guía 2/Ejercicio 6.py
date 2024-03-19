input_numero = int(input("Porfavor ingrese un número del 1 al 7: "))

if input_numero > 7 or input_numero < 1:
    print("El número ingresado no cumple con los requisitos (debe ser del 1 al 7).")
else:
    match input_numero:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miércoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")