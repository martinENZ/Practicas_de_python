#Encriptar un mensaje usando el metodo de la "la cifra de cesar", que consiste en correr cada letra -considerando la posicion de cada una en el alfabeto- una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra "Hola" se transforma en "JQNC". Si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra "a".

#http://patriciaemiguel.com/ejercicios/python/2019/10/19/ejercicio-python-for.html

alfabeto = "abcdefghijklmnñopqrstuvwxyz"
corrimiento= 2
mensaje=input("mensaje a encriptar")
encriptado=""

for x in mensaje:
    if x.lower() in alfabeto:
        indice = alfabeto.