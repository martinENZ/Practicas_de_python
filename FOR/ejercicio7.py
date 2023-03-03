#Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).


#f=str(input("ingrese una frase: "))
#vocales ='aeiou'
#a=''
#for x in f:
    #if x in vocales:
        #a += str(x)

#la funcion set() elimina los elemenotos repetidos
#print(set(a))

frase=input("Frase: ")
print("Vocales en la frase:")
for x in "aeiou":
  if x in frase:
    print(x)