numero = int(input("Porfavor ingrese un número entero: "))
texto = ""
while numero < 0:
    numero = int(input("El número ingresado debe ser natural\nPorfavor ingrese un número natural: "))

if numero %2 == 0:
    for p in range(0, numero+1, 2):
        texto = f"{p} " + texto
        print(texto)
else:
    for i in range(1, numero+1, 2):
        texto = f"{i} " + texto
        print(texto)