def fahrenheit_to_celsius(temperatura):
    return (temperatura - 32) * 5/9

user_input = int(input("Porfavor ingrese una temperatura en °F (solo ingrese el número): "))
print(f"La temperatura en °C es de {fahrenheit_to_celsius(user_input)}")