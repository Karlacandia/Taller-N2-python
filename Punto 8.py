''' Leer los tres lados del triángulo (A,B Y C), imprimir el tipo de triangulo teniendo en 
cuenta que es un triángulo equilátero(solo si sus tres lados son iguales) y es un 
triángulo escaleno(si todos los lados son diferentes). Además debe validar que sus 
lados permitan formar un triángulo; la condición es que cada lado tiene que ser 
menos que la suma de los otros dos.'''
A = float(input("Ingrese el lado A del triangulo: "))
B = float(input("Ingrese el lado B del triangulo: "))
C = float(input("Ingrese el lado C del triangulo: "))

if A + B > C and A + C > B and B + C > A:
    if A == B == C:
        print ("El triangulo es equilatero (Todos los lados son iguales).")
    elif A != B and A != C and B != C:
        print ("El triangulo es escaleno (Todos los lados son diferentes).")
    else:
        print ("El triangulo es isosceles (Dos se los lados son iguales).")
else:
    print ("Los lados ingresados no forman un triangulo.")