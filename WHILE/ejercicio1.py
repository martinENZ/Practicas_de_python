#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.


total=0
x = int(input("ingrese numero. precione 0 para sacir: "))
while x != 0:
    total +=x
    x=int(input("numero: "))

print(total)