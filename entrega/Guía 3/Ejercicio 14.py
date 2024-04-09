num_1 = int(input("Porfavor ingrese dos números enteros\nPrimer número: "))
num_2 = int(input("Segundo número: "))

for i in range(num_1, num_2+1):
    if i%2 == 0:
        print(f"{i}", end=" ")