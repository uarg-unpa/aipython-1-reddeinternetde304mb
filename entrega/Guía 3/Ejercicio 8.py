numero_input = 0
while numero_input < 3:
    numero_input = int(input("Porfavor ingrese un número mayor a 3: "))
    if numero_input < 3:
        print("El numero ingresado no es mayor a 3 :(")
for numero in range(1, numero_input +1, 2):
    print(numero)