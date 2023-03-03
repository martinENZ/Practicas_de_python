#Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.


rojo_A = "A"
verde_B= "B"
azul_C= "C"

candidato=input("ingrese una canditato entre las opsiones a votar, a= rojo, b= verde, c=azul ")
print(len(candidato))
if len(candidato) == 1:

    if candidato.upper() == rojo_A:
        print("usted eligio al candidato A del equipo Rojo")
    elif candidato.upper() == verde_B:
        print("usted eligio al candidato B del equipo Verde")
    elif candidato.upper == azul_C:
        print("usted eligio al candidato C del equipo Azul")
    else:
        print("“Opción errónea”.")
else:
    print("“ingresar solo una letra")