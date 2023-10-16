#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.
capital = int(input("Inserte la cantidad a invertir: "))
interesAnum = int(input("Inserte el interes anual (%)"))
años = int(input("Inserte el numero de años que desee invertir"))

interes = capital * interesAnum / 100
for i in range(1,años+1):
    capital += interes
    print("Año " + str(i) + ". Capital obtenido: " + str(capital))
