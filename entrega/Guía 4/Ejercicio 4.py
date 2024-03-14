def tabla_del_x(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

x = int(input("Porfavor ingrese un número: "))
tabla_del_x(x)