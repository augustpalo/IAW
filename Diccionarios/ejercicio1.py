""" Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
'Yen':'Y'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de
aviso si la divisa no está en el diccionario. """
divisas = {
    "Euro" : "€",
    "Dollar" : "$",
    "Yen" : "Y"
}
divisa = str(input("Inserte una divisa:\n"))
if divisa in divisas:
    print(divisas.get(divisa))
else:
    print("Divisa no reconocida")