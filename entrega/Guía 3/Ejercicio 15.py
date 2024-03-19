numero = int(input("Porfavor ingrese un número: "))
divisor = 2
numero_limite = int(numero / divisor)
is_primo = False
is_compuesto = False

if numero == 1:
    print(f"El número {numero} no es ni primo ni compuesto")
elif numero < 1:
    print(f"El número {numero} no es natural")
else:
    while is_primo == False and is_compuesto == False:
        if divisor > numero_limite:
            print(f"El número {numero} es primo")
            is_primo = True
        elif numero % divisor != 0:
            divisor += 1
            numero_limite = int(numero / divisor)
        else:
            print(f"El número {numero} es compuesto")
            is_compuesto = True