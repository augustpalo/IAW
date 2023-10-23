#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por comas.
printme = []
num = int(input("Inserte un numero entero positivo:\n"))
for i in range(1,num+1):
    if (i%2 == 1):
        printme.append(i)
print(', '.join(map(str,printme)))



