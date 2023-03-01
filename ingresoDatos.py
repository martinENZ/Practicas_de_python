#ingresar datos mediante la funcion input

#nombre = input("Ingrese su nombre: ")

#print("tu nombre es " + nombre)

print ("AHORA SE ARA UN EJERCICIO CON LA FUNCION IF,ELIF,ELSE")

tipoAlgodon = int(input("ingrese tipo de algodon: 1 para Piker y 2 para stripper: "))

if tipoAlgodon == 1:
    print("usted trabajara con piker")
elif tipoAlgodon > 2:
    print("no es la opsion correcta")
else:
    print("usted trabajara con striper")
