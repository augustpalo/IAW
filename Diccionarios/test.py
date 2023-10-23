mi_diccionario = {
    "nombre" : "August",
    "curso" : "2ºASIR",
    "Asignaturas" : ["HDC","ASO","ASGBD","SRI","IAW","SAD","Empresa"]
    }

#Modifica valor de la clave
mi_diccionario["nombre"] = "August Horacio"
#Añade clave y valor nuevo
mi_diccionario["apellido"] = "Paloluoma"
#Borra clave
del mi_diccionario["curso"]
#Usa "in" para verificar si existe una clave en el diccionario
if "curso" not in mi_diccionario:
    print ("clave curso no existente")
#Numero de claves en el diccionario
len(mi_diccionario)
#Imprime todos los valores
print(mi_diccionario.values)
#imprime todos las claves
print(mi_diccionario.keys)
#devuelve una tupla del diccionario
print(mi_diccionario.items)
#Imprime el valor una clave concreta
print(mi_diccionario.get("apellido"))
#Imprime todas las claves del diccionario
print(mi_diccionario)

