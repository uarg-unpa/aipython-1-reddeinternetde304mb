print("Usando la funcion "+"print()")
print("Usando la funcion print()"*3)

#Argumentos posicionales
print(10, 3.14, "Cadena", True)

edad = int(input("Ingrese su edad: "))
#print("Su edad es " + edad) -> no se puede concatenar un str con un int
print("Su edad es", edad)
print("Su edad es " + str(edad))

#print(f"{}") nos permite poner variables en una str durante la función print
num1 = 4
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} % {num2} = {num1 % num2}")

#Métodos
texto = "EsTo eS Un tExTo mEzClAdO"
#title()
print(texto.title())
#upper() y lower()
print(texto.upper())
print(texto.lower())
#replace(from, to)
print(texto.replace(" ","-"))

#len() da la longitud de la variable con type='int'
print(len(texto))

#Operadores relacionales:
print(2 == 2)
print(1 != 3)
print(4 > 3)
print(3 >= 3)
print(2 < 5)
print(2 <= 2)

#Sentencia if
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Usted es mayor de edad")
print("No me importa tu edad, estoy fuera del bloque if muahaha")

#Sentencia else
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted no es mayor de edad >:(")
print("A mi tampoco me importa tu edad, pero yo no me voy a reir")

calificacion = int(input("Ingrese su calificación: "))
if calificacion >= 90:
    print("Excelente!")
else:
    if calificacion >= 80:
        print("Muy Bien")
    else:
        if calificacion >= 70:
            print("Bien")
        else:
            print("Insuficiente :(")
#Sentencia elif
if calificacion >= 90:
    print("Excelente!")
elif calificacion >= 80:
    print("Muy Bien")
elif calificacion >= 70:
    print("Bien")
else:
    print("Insuficiente :(")

#Match
dia = input("¿Qué día es hoy?: ").title()
match dia:
    case "Lunes":
        print("Hoy es Lunes")
    case "Martes":
        print("Hoy es Martes")
    case "Miercoles":
        print("Hoy es Miercoles")
    case "Jueves":
        print("Hoy es Jueves")
    case "Viernes":
        print("Hoy es Viernes")
    case "Sabado":
        print("Hoy es Sabado")
    case "Domingo":
        print("Hoy es Domingo")
