#Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, imprimir “coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si no es así, imprimir “no hay coincidencia”.

nom1= input("ingrese un nombre ")
nom2= input("ingrese un nombre ")

pos_final_nom1=len(nom1)-1
pos_final_nom2=len(nom2)-1

if nom1[0] == nom2[0] or nom1[pos_final_nom1] == nom2[pos_final_nom2]:
    print("coincidencia")
else:
    print("no hay coincidencia")

#print(nom2[0])
#print(nom2[pos_final_nom2])

#len cuenta cuantos caracteres hay en una palabra

