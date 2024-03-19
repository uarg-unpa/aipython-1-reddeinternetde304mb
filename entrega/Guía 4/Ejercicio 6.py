def calcular_factorial(numero):
    resultado = numero
    for i in range(1,numero):
        resultado = resultado * i
    return resultado

num = int(input("Porfavor ingrese un número: "))
print(calcular_factorial(num))