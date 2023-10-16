lista = ["uno","dos","tres","cuatro"]
tupla = (1,2,3,4,5)

hola = ("h","o","l","a")

print(lista[0:3])
print(tupla[0])



lista.insert(3,8)
lista.append("cinco")
lista.extend(hola)


i = len(lista)
print(lista[0:i])
print(tupla[0])

lista.pop(2)

i = len(lista)
print(lista[0:i])

lista.remove('o')


i = len(lista)
print(lista[0:i])