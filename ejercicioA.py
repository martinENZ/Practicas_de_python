#Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.


num1 = int(input("Por favos ingrese el primer numero entero: "))
num2 = int(input("Por favos ingrese el segundo  numero entero: "))

#resultado = num1 / num2


if num1 % num2 == 0: #el simbolo % toma el valor del resto por eso si el resto es igual a cero la divicion es exacta
    print("la divicion es excta.")
else:
    print("la divicion no es exacta. ")


