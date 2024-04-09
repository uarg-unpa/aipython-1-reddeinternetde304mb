def cantidad_vocales(texto):
    vocales = 0
    for letra in texto:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vocales += 1
    return vocales

user_input = input("Porfavor ingrese algunos carácteres: ")
print(cantidad_vocales(user_input))