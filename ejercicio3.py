# leer numero enteros positivos de teclado, hasta que el usuario ingrese el 0. informar cual fue el numero mayor ingresado 


n = int(input("ingrese un numero (cero para salir): "))

m = 0

while n >= 0:
    if n > m:
        m = n
    n = int(input("ingrese un numero (cero para salir): "))

print("el numero mayor ingresado es {}".format(m))