#Solicitar 3 numero del usuario y mostrar el menor
a = int(input("primer numero "))
b = int(input("segundo numero "))
c = int(input("tercer numero "))

if a > b:
    mayor = a
else:
    mayor = b
if c > mayor:
    mayor = c

    
numeroMayor = str(mayor)
    
print("el numero mayor es: " + numeroMayor)