edad = int(input("Porfavor ingrese su edad e ingresos mensuales\nEdad: "))
ingresos_mensuales = float(input("Ingresos mensuales: $"))

if edad >= 18 and ingresos_mensuales >= 100000:
    print("Usted debe pagar el impuesto")
else:
    print("Usted no debe pagar el impuesto :D")
