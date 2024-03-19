numero = int(input("Porfavor ingrese un número natural: "))
resultado = 0
while numero < 0:
    numero = int(input("El número ingresado debe ser natural\nPorfavor ingrese un número natural: "))

for i in range(1,numero+1):
    if i < numero:
        print(f"{i*2} +", end=" ")
        resultado += i*2
    else:
        resultado += numero*2
        print(f"{numero*2} = {resultado}")