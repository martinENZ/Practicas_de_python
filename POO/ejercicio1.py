#como hacer una clase 

class Suma:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def mostrar(self):
        print("numero 1:",self.num1)
        print("numero 2:",self.num2)
    
    def sumar(self):
        s=self.num1 + self.num2
        print("la suma de los numeros ingresados es de: ", s)

    def resta(self):
        print("la resta es de: ", self.num1-self.num2)        

    def multi(self):
        print("la multiplicacion es de: ", (self.num1*self.num2))        


suma1 = Suma(2,2)
suma2 = Suma(7,4)

suma1.mostrar()
suma1.multi()

suma1.sumar()
suma2.resta()