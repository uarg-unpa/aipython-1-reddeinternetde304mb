edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted tiene edad suficiente para conducir")
else:
    print(f"Usted no tiene edad suficiente para conducir, le faltan {18 - edad} años")