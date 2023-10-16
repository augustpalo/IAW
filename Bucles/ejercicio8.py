#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
#muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Introduzca una frase: ")
letra = input("Introduzca una letra: ")
contador = 0

for i in range(len(frase)):
    if (frase[i] == letra):
        contador += 1

print(contador)