'''Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda'''


listamadre = []
listahijo =[]
s=int(input("continuar.? 0 para salir"))
while s != 0:
    nombre =input("nombre: ");listahijo.append(nombre)
    edad = input("edad: ");listahijo.append(edad)
    sexo = input("sexo: ");listahijo.append(sexo)

    print(listahijo)
    #print("continuar.? 0 para salir")
    listamadre.append([listahijo])
    listahijo=[]
    s = int(input("continuar.? 0 para salir"))
print("*******************lista madre*************")
print(listamadre)
print("*****************************")



for i in range(len(listamadre)):
    print(listamadre[i])
    contacto = (listamadre[i])
    for j in range(len(contacto)):
        print(contacto[j])
    contacto=[]
#print(listamadre[[0]])



