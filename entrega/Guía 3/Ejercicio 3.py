numero_while = 10
while numero_while > -1:
    if numero_while != 0:
        print(numero_while, end=" - ")
    else:
        print(numero_while)
    numero_while = numero_while -1

for numero_for in range(10,-1,-1):
    if numero_for != 0:
        print(numero_for, end=" - ")
    else:
        print(numero_for)