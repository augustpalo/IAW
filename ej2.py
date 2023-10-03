#Solicitar dos numeros al usuario y devolver el menor de los dos
a = int(input("Introduzca el primer numero: "))
b = int(input("Introduzca el segundo numero: "))

menor = a
if (a > b):
    menor = b
print(menor)