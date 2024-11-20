''' Desarrolle un algoritmo que permita leer una nota entre 0.0y 5.0. Imprimir su nota 
cualitativa equivalente. Teniendo en cuenta la siguiente tabla.'''
Nota = float(input("Ingrese una nota entre  0.0 y 5.0.: "))
if 4.6 <= Nota <= 5.0:
    print ("La nota cualitativa es: Excelente")
elif 3.6 <= Nota <= 4.6:
     print ("La nota cualitativa es: Buena")
elif 3.0 <= Nota <= 3.6:
    print ("La nota cualitativa es: Aceptable") 
elif 2.0 <= Nota <= 3.0:
    print ("La nota cualitativa es: Insuficiente") 
elif 0.0 <= Nota <= 2.0:
    print ("La nota cualitativa es: Deficiente") 
else :
    print ("Nota invalida debe estar entre 0.0 y 5.0 ")

