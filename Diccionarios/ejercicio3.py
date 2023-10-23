""" Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
mensaje informando de ello. """

fruta = {
    "Platano" : 1.35,
    "Manzana" : 0.8,
    "Pera" : 0.85,
    "Naranja" : 0.7
}

in_fruta = input("Inserte la fruta que desee comprar:\n")
in_kg = int(input("Inserte el numero de kilos de la fruta que desee comprar:\n"))

if in_fruta in fruta:
    print(str(round(fruta.get(in_fruta)*in_kg,2)) + "€")

else:
    print("Fruta no disponible.")