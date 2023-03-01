#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales.

num1=int(input("ingrese un numero: "))
num2=int(input("ingresenotro numero: "))

if num1<num2:
    print("el primero es menor")
elif num1>num2:
    print("el segundo es menor")
else:
    print("son iguales")
