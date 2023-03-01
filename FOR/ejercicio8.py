#Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase

f=str(input("ingrese una frase: "))
v='aeiou'
num=0
for x in f:
    if x in v:
        num+=1

print("n° de vocales: {}".format(num))