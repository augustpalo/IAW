#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla la cuenta atrás desde ese número hasta cero separados por comas.
cuentaAtras = []
num = int(input("Inserte el numero para empezar la cuenta atras\n"))

for i in range(num,0,-1):
    cuentaAtras.append(i)
print(', '.join(map(str,cuentaAtras)))