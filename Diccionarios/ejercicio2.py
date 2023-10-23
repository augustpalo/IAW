""" Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene
<edad> años, vive en <dirección> y su número de teléfono es <teléfono> """
dicc_usuario = {
    "nombre",
    "edad",
    "direccion"
}
dicc_usuario["nombre"] = input("Inserte su nombre")
dicc_usuario["edad"] = input("Inserte su edad")
dicc_usuario["direccion"] = input("Inserte su direccion")

print(dicc_usuario.get("nombre") + "tiene " + dicc_usuario.get("edad") + " años, vive en " 
      + dicc_usuario.get("direccion") + " y su numero de telefono es ")