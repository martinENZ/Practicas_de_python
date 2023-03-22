#realizar un programa en el que ingrese un numero entero y lo combierta en romano.


class Romanos:
    def __init__(self,numero):
        self.numero = int(input("ingrese un numero menor al 100: "))
    
    uni=["I","II","III","IV","V","VI","VII","VIII","IX"]

    dec=["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    listaDecimal=[]

    def identificar(self):
        if n <= 9:
   #print("numero ingresado es una unidad")
            print(uni[n-1])   
        elif n == 10:
            print(dec[0]) 
        elif n >= 11 and n<=99:
            #print("numero ingresado es una decena")   
            while n > 0:
                #print(n % 10)
                listaDecimal.append(n % 10)

                n = n // 10
            #print(listaDecimal)
            #print(list(reversed(listaDecimal)))
            listaOrdenada = list(reversed(listaDecimal))
            #print("lista ordenada: ",listaOrdenada)
            #print("elemento 0: ",listaOrdenada[0])

            #print("elemento 1: ",listaOrdenada[1])
            if listaOrdenada[0] == 1:
               #print(uni[listaOrdenada[0]-1])
                print("numero romano es:",dec[listaOrdenada[0]      -1],uni[listaOrdenada[1]-1])
        else:
            print("numero incorrecto")