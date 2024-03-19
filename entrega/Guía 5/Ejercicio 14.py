def intercalar_listas(lista_1=[], lista_2=[]):
    lista_intercalada = []
    current_index = 0
    while current_index < len(lista_1) and current_index < len(lista_2):
        lista_intercalada.append(lista_1[current_index])
        lista_intercalada.append(lista_2[current_index])
        current_index += 1
    while current_index < len(lista_1):
        lista_intercalada.append(lista_1[current_index])
        current_index += 1
    while current_index < len(lista_2):
        lista_intercalada.append(lista_2[current_index])
        current_index += 1
    return lista_intercalada


numeros_impares = [1,2,3,4,5,6,7,8]
numeros_pares = ["a","e","i","o","u"]
print(intercalar_listas(numeros_impares, numeros_pares))