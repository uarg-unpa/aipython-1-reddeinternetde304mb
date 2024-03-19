#Listas:
nombres = ["Facundo", "Franco", "Fernanda", "Fabiana"]
#Mostrar la lista:
print(f"La lista es {nombres}")
#mostrar cada elemento de la lista:
for i in range(len(nombres)):
    print(nombres[i])
for nombre in nombres:
    print(nombre)
#acceder a elementos específicos:
primer_nombre = nombres[0]
print(f"El primer elemento de la lista es {primer_nombre}")
#Crear una lista con valores iniciales utilizando list()
nombres = list(["Facundo", "Franco", "Fernanda", "Fabiana", "Fulano"])
print(nombres)
#Metodo append() agrega algo al final de la lista
nombres.append("Francisco")
print(nombres)
#Metodo insert() agrega algo en un índice específico
nombres.insert(0, "Federico")
print(nombres)
#Mutabilidad:
id1 = id(nombres)
nombres[3] = "Fernando"
print(nombres)
id2 = id(nombres)
print(id1, id2, sep="\n")
if id1 == id2:
    print("Es Mutable")
#Rebanadas:
print(nombres[:3])