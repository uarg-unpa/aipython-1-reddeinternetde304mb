inversión = float(input("Porfavor introduzca los siguientes datos.\nCantidad a invertir: "))
interes_anual = float(input("Interés anual: "))
cantidad_años = int(input("Número de años: "))
#no estoy seguro de cual es el cálculo exactamente, supongo que el interés es un porcentaje de la inversión, y que la inversión se paga una vez al año (?)
capital_obtenido = (interes_anual * inversión) / 100 * cantidad_años

print(f"El capital obtenido de la inversión es ${capital_obtenido}")