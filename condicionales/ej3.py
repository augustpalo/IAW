#Solicitar dos numeros al usuario y devolver el menor de los dos. Considerar el caso en el que sean iguales
a = int(input("Introduzca el primer numero: "))
b = int(input("Introduzca el segundo numero: "))

menor = a
if (a > b):
    menor = b
elif (a == b):
    menor = "Son iguales"

print(menor)