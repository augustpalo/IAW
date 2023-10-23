""" Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del
mes. """

meses = {
    1 : "Enero",
    2 : "Febrero",
    3 : "Marzo",
    4: "Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}

dia = input("Inserte una fecha en formato dd/mm/aaaa\ndd:\t")
mes = input("mm:\t")
while mes not in meses:
    mes = input("Valor no valido. Prueba de nuevo\nmm:\t")
año = input("aaaa:\t")

print(dia + " de " + meses.get(mes) + " de " + año)

