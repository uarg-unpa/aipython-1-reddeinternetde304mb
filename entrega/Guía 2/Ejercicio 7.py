calificación = float(input("Porfavor ingrese su calificación: "))

if calificación >= 80 and calificación <= 100:
    print("Su calificación es: A")
elif calificación >= 70 and calificación <= 79:
    #el ejercicio dice que tiene que ser de 70 a 89, me imagino que fue un error :p
    print("Su calificación es: B")
elif calificación >= 60 and calificación <= 69:
    print("Su calificación es: C")
elif calificación >= 50 and calificación <= 59:
    print("Su calificación es: D")
elif calificación >= 0 and calificación <= 49:
    print("Su calificación es: F")
else:
    print("El número ingresado no es una calificación valida :(")