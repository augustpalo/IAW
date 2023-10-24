""" Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del
mes. """

meses = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}

fecha = input("Inserte una fecha en formato dd/mm/aaaa:\n\t")
dia = fecha[0:2]
mes = int(fecha[3:5])
año = fecha[6:10]

print(dia + " de " + str(meses.get(mes)) + " de " + año)

