num_a = int(input("Porfavor ingrese dos números\nNumero a: "))
num_b = int(input("Numero b: "))
if num_a < num_b:
    for numero in range(num_a, num_b +1):
        if numero != num_b:
            print(numero, end=" - ")
        else:
            print(numero)
elif num_b < num_a:
    for numero in range(num_b, num_a +1):
        if numero != num_a:
            print(numero, end=" - ")
        else:
            print(numero)
else:
    print(num_a)