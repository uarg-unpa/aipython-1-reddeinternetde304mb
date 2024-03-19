def max_numero(num_1=1, num_2=1, num_3=1):
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >= num_3:
        return num_2
    else:
        return num_3

a = int(input("Porfavor ingrese tres números\nPrimer número: "))
b = int(input("Segundo número: "))
c = int(input("Tercer número: "))
print(f"El número más grande es el {max_numero(a, b, c)}")