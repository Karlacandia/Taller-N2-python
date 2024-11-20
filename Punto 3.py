''' Calcule el promedio de goles anotados por un jugador en cuatro encuentros, solo 
si la suma de estos es mayor a 10; de lo contrario imprimir “No se puede determinar 
el promedio”. '''
Partido1= int (input ("Ingrese el numero de goles del partido 1: "))
Partido2= int (input ("Ingrese el numero de goles del partido 2: ")) 
Partido3= int (input ("Ingrese el numero de goles del partido 3: "))
Partido4= int (input ("Ingrese el numero de goles del partido 4: "))

suma_goles= Partido1 + Partido2 + Partido3 + Partido4 

if suma_goles > 10:
    promedio = suma_goles / 4 
    print (f"El promedio de goles es: {promedio}")
else: 
    print ("No se puede determinar el promedio")