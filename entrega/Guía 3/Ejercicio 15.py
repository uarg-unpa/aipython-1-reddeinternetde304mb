numero = int(input("Porfavor ingrese un número: "))
divisor = 2
numero_limite = int(numero / divisor)
is_primo = False
is_compuesto = False

while is_primo == True or is_compuesto == True:
    if divisor > numero_limite:
        print(f"{numero} es primo")
        is_primo = True
    if numero % divisor != 0:
        divisor += 1
        numero_limite = int(numero / divisor)
    else:
        print(f"{numero} es compuesto")
        is_compuesto = True