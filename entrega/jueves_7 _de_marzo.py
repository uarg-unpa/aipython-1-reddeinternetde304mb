#Índice:
#" A  I  P  Y  T  H  O  N "
#  0  1  2  3  4  5  6  7
# -8 -7 -6 -5 -4 -3 -2 -1

palabra = "AIPYTHON"
print(palabra[3])
print(palabra[:2])
print(palabra[-3:])
print(palabra[::2])
print(palabra[::-1])

#  palabra[3] = "y"   ->   salta error (inmutabilidad)


#in - not in
if "P" in palabra:
    print(f"P se encuentra en {palabra}")
if "p" not in palabra:
    print(f"p no se encuentra en {palabra}")


#Programa que solicite frase y caracter y haga cosas
frase = input("Porfavor ingrese una frase: ")
caracter = input("Porfavor ingrese un caracter: ")
#buscar primera posición del caracter
posicion = frase.find(caracter)
#find() devuelve -1 cuando no encuentra nada
if posicion != -1:
    print(f"El caracter {caracter} se encuentra en la posición {posicion + 1}")
    #crear una subcadena de la frase que recorte todo lo que haya antes del caracter ingresado
    subcadena = frase[posicion:]
    print(f"Subcadena a partir de la posición {posicion}: {subcadena}")
else:
    print(f"El caracter {caracter} no se encuentra en la frase")


#while - itera las sentencias siempre y cuando la condición se cumpla
contador = 0
while contador <= 10:
    print(contador, end=" - ")
    contador += 1

#for - itera segun una colección
cadena = "AiPython"
for letra in cadena:
    print(letra, end=" - ")

for num in range(10):
    print(num, end=" - ")
    #solo imprime hasta 9, no 10

cadena = "AiPython"
for indice in range(len(cadena)):
    print(cadena[indice], end=" - ")

for _ in range(10):
    print("AiPython", end=" - ")