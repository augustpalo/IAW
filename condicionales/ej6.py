#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
a = int(input("Inserte un numero:\n"))

esPar = a%2 == 0

if esPar:
    print("El numero es par")
else:
    print("El numero es impar")



