#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
imprime = []
for i in range (1,11):
    for j in range(1,11):
        imprime.append(i*j)
    print(str(imprime)+"\n")
    imprime = []

    