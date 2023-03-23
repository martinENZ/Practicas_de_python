#realizar un programa en el que ingrese un numero entero y lo combierta en romano.


class Romanos:
    def __init__(self):
        self.numero = numero=int(input("ingrese un numero menor al 100: "))

    def identificar(self):

        uni=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        dec=["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        listaDecimal=[]

        if self.numero <= 9:
            print(uni[self.numero-1])   
        elif self.numero >= 10 and self.numero<=99:
              
            while self.numero > 0:
                listaDecimal.append(self.numero % 10)
                self.numero = self.numero // 10

            listaOrdenada = list(reversed(listaDecimal))
            print(listaOrdenada)
            primerNumero = listaOrdenada[0]
            segundoNumero = listaOrdenada[1]
            print("numero romano: ",dec[primerNumero-1],uni[segundoNumero])
                
        else:
            print("numero incorrecto")




prueba=Romanos()

prueba.identificar()