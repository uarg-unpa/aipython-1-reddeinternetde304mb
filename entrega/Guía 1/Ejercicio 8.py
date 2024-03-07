import math
#ya se que esto no lo vimos, pero bueno me parecia mejor que usar 3.14

base = int(input("Porfavor ingrese la longitud de la base del rectangulo: "))
altura = int(input("Porfavor ingrese la longitud de la altura del rectangulo: "))

perimetro_rectangulo = base*2 + altura*2
area_rectangulo = base * altura
print("El perimetro del rectangulo es", perimetro_rectangulo)
print("El área del rectángulo es", area_rectangulo)



radio = int(input("Porfavor ingrese la longitud del radio de la circunferencia: "))
perimetro_circunferencia = math.pi * radio*2
area_circunferencia = math.pi * radio**2
print("El perimetro de la circunferencia es", perimetro_circunferencia)
print("El área de la circunferencia es", area_circunferencia)