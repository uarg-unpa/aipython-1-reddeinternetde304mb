def is_palindromo(texto):
    if texto.lower() == texto.lower()[::-1]:
        return True
    else:
        return False

user_input = input("Porfavor ingrese una palabra: ")
if is_palindromo(user_input) == True:
    print(f"{user_input} es un palíndromo")
else:
    print(f"{user_input} no es un palíndromo")