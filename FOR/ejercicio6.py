#Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados

n=int(input("ingrese un numero: "))

s=0
for i in range (n):

    num=int(input("ingrese un numero para sumar"))
    s+=num
    
#print("la suma de los n° ingresados es de", s)
print("la suma de los n° ingresados es de {}".format(s))