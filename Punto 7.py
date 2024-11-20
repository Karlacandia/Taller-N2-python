''' En las pruebas de ICFES, se presentan dos tipos de prueba: Una de aptitud 
matemática y otra de lenguaje. Leer los puntajes obtenidos por un estudiante en 
cada prueba e imprimir en cual obtuvo mayor puntaje. Tenga en cuenta que 
ambos puntajes podrían ser iguales'''
puntaje_matematicas=float(input("Ingrese el puntaje obtenido en la prueba de matematicas: "))
puntaje_lenguaje=float(input("Ingrese el puntaje obtenido en la prueba de lenguaje: "))
if puntaje_matematicas > puntaje_lenguaje:
    print ("El estudiante tuvo mayor puntaje en matematicas.")
elif puntaje_lenguaje > puntaje_matematicas:
    print ("El estudiante tuvo mayor puntaje en lenguaje.")
else:
    print ("El estudiante obtuvo puntajes iguales en ambas pruebas.")