#Terminar una iteración - break y continue
num = int(input("Ingrese numero: "))
while num > 0:
    if num %2 == 0:
        print("Finalizando bucle")
        break
    num=int(input())


suma=0
for i in range(1,30):
    print(i)
    if i > 10:
        continue
    suma = suma + 1
print(suma)


#Funciones
def suma(num_1, num_2):
    return(num_1 + num_2)
num_a = int(input("Porfavor ingrese dos números\nNúmero a: "))
num_b = int(input("Número b: "))
print(f"La suma entre {num_a} y {num_b} es {suma(num_a, num_b)}")

def presentación(nombre, apellido, domicilio):
    print(f"Su nombre es {nombre} y su apellido es {apellido}\nSu domicilio es {domicilio}")
#presentación("casa", nombre="Facundo", apellido="Palacios")
# ^^^ Salta error porque "casa", aunque nosotros queremos que sea para la variable domicilio,
#     se asigna a la variable nombre. Los argumentos posicionales deben ir en orden
presentación(nombre="Facundo", domicilio="Casa", apellido="Palacios")
# ^^^ En este caso si funciona porque aunque las cosas se pongan desordenadas,
#     se asignan directamente a la variable

#Funciones - asignar valores por defecto
def suma(num_1=0, num_2=0):
    return(num_1 + num_2)
# ^^^ Si ahora salta un argumento, se asigna automáticamente el valor 0
num_a = int(input("Porfavor ingrese dos números\nNúmero a: "))
num_b = int(input("Número b: "))
print(f"La suma entre {num_a} y {num_b} es {suma(num_a, num_b)}")