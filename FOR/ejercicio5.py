#Requerir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos entre el ingresado por el usuario y uno menos del doble del mismo.

num = int(input("ingrese un numero entero positivo "))

for x in range(num, num*5):
    print(x)
