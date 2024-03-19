peso_kg = float(input("Porfavor introduzca su peso en kg (ej. 65.8): "))
altura_metros = float(input("Porfavor introduzca su estatura en metros (ej. 182.9): "))

imc = peso_kg / altura_metros**2

print(f"Tu índice de masa corporal es: {imc}")