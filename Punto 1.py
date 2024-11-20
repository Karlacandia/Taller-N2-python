''' Hacer un programa para un laboratorio de Quimica, que lea un simbolo quimico e imprimir
a que elemento al cual corresponde.'''
simbolo= input ("Digite el simbolo en mayuscula: ")
simbolo1=simbolo.upper()
if simbolo1=="H":
    print ("El elemento es Hidrogeno ")
elif simbolo1 == "O":
    print ("El elemento es Oxigeno")
elif simbolo1 == "N":
    print ("El elemento es Nitrogeno")
else:
    print("Elemento NO encontrado")