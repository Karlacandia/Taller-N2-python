''' Una persona no tiene claridad sobre el dispositivo que desea comprar para su 
portátil . La decisión la tomará de acuerdo con una bonificación que recibirá de 
parte de la empresa donde labora. Si recibe menos de $50.000 comprará una 
cámara web. Si recibe entre $50.000 y $200.000 comprará un subwoofer. Si recibe 
más de $200.000 y hasta $500.000 se comprará un DD externo. Si recibe más de 
$500.000 y hasta $1.000.000 se compra una impresora multifuncional. Y si recibe 
más de un $1.000.000 se comprará un proyector.
Realice un algoritmo para ayudarle a esta persona a comprar un dispositivo.'''

Bonificacion = float(input("Ingrese el valor de la Bonificacion recibida: "))
if Bonificacion<50000:
    print (f"La persona comprara una Camara web por que su bonificacion es: {Bonificacion}")
elif Bonificacion >=50000 and Bonificacion<= 200000:
     print (f"La Persona comprara un Subwoofer por que su bonificacion es: {Bonificacion}")
elif Bonificacion > 200000 and Bonificacion<= 500000:
     print (f"La Persona comprara un DD externo por que su bonificacion es: {Bonificacion}")
elif Bonificacion > 500000 and Bonificacion<= 1000000: 
     print (f"La Persona comprara una Impresora multifuncional por que su bonificacion es: {Bonificacion}")
elif Bonificacion > 1000000:
     print (f"La Persona comprara un Proyector por que su bonificacion es: {Bonificacion}")

