edad = int(input("Porfavor ingrese su edad: "))
if edad < 4:
    print("Usted puede entrar gratis. ¡Diviertase!")
elif edad >= 4 and edad <= 18:
    print("Usted debe pagar $5")
else:
    print("Usted debe pagar $10")