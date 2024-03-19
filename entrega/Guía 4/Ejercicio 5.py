def check_par_impar(numero):
    if numero%2 == 0:
        return f"El número {numero} es par"
    else:
        return f"El número {numero} es impar"

num = int(input("Porfavor ingrese un número: "))
print(check_par_impar(num))