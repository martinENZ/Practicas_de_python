#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.

n = int(input("ingrese un numero: "))
suma = 0

while n != 0:
    
    if n > 0:
        suma += n
    
    n = int(input("ingrese un numero: "))
    

print(suma)


