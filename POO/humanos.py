class Humano:
    def __init__(self,sex,altura,edad):
        self.sex = sex
        self.altura = altura
        self.edad = edad
    
    def tipo_sex(self):
        if str(self.sex) == "mujer":
            print("el individuo es de genero Femenino")
        else:
            print("el individuo es de genero Masculino")
    
    def altura_pro(self):
        if int(self.altura) > 160:
            print("la estatura supera el promedio")
        else:
            print("la estatura no supera el promedio")
    def adul(self):
        if int(self.edad) >= 18:
            print("Esta persona es mayor de edad")
        else:
            print("Esta persona es menor de edad")
            
p1 = Humano("mujer", 155, 16)
p2 = Humano("hombre", 180, 20)

p1.altura_pro()
p1.tipo_sex()
p1.adul()

print(dir(p1))
print(vars(p2)) #la funcion vars(muestra todos los atributos de un objeto)

p2.altura_pro()
p2.tipo_sex()
p2.adul()
#print(saludo())