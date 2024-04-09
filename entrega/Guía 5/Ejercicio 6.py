datos_personales = ["Nombre", "Edad", "Altura", "Estado Civil", "Dirección"]
datos_personales_usuario = []

print("Porfavor ingrese su Nombre, Edad, Altura, Estado Civil y Dirección")
for i in range(0, 5):
    user_input = input(f"{datos_personales[i]}: ")
    datos_personales_usuario.insert(i, user_input)
print(f"Sus datos son: {datos_personales_usuario}")