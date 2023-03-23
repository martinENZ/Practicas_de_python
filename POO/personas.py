#definir un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.
#definir los metodos para inizializar sus atributos, imprimirlos y mostrar un mensaje de la nota si aprobo o no.


class Alumno:
    def __init__(self, nombre, nota): # self hace referencia al objeto en si 
        self.nombre = nombre #estos son los atributos que se pasaran por parametros 
        self.nota = nota
    
    def imprimir(self): #creacion del primer metodo que cumple con la funcion de imprimir los nombres
        print("Nombre del alumno: ", self.nombre)
        print("Nota del Alumno: ", self.nota)
    
    def resultado(self):
        if self.nota > 5:
            print("Aprobado")
        else:
            print("desaprobado")


al1 = Alumno("juan",6) # esto es lo que se llama instanciar un objeto 
al2 = Alumno('pedro',3)

al1.saltar = True

al1.imprimir() #mostrar / imprimir un objeto
al1.resultado()
print(al1.nombre)

al2.imprimir()
al2.resultado()

