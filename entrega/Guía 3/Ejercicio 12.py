numero = int(input("Porfavor ingrese un número natural: "))
resultado = 0
while numero <= 0:
    numero = int(input("El número ingresado debe ser natural\nPorfavor ingrese un número natural: "))

for i in range(1,numero+1):
    if i < numero:
        print(f"{i} +", end=" ")
        resultado += i
    else:
        resultado += numero
        print(f"{numero} = {resultado}")