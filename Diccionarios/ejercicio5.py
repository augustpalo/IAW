""" Escribir un programa que almacene el diccionario con los créditos de las asignaturas de
un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los
créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus
créditos. Al final debe mostrar también el número total de créditos del curso """

asignaturas = {
    "Matematica" : 6,
    "Fisica" : 4,
    "Quimica" : 5
}

contador = 0

for asgn in asignaturas:
    print((asgn) + " tiene " + str(asignaturas.get(asgn)) + " creditos")
    contador += int(asignaturas.get(asgn))

print("Total de creditos: " + str(contador))