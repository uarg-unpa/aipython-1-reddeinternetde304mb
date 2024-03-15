def calcular_promedio(numeros):
    len_numeros = len(numeros)
    promedio = 0
    for numero in numeros:
        promedio += numero
    promedio = promedio / len_numeros
    return promedio

notas_2023 = [7,6,8,7,7,8,9,8,10,7,11,3]
print(calcular_promedio(notas_2023))