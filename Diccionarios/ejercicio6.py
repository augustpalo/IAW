""" Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
contenido del diccionario. """
persona = {}

loop = True

while loop:
    clave = input("Inserte un dato sobre una persona\n")
    valor = input("Cual es el valor de ese dato\n")
    persona[clave] = valor
    print(persona.items())
    loop = input("Desea insertar otro dato?(y/n)\n") == "y"
