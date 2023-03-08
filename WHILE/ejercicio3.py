#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.

contraseña = str(input("ingrese una contraseña: "))
i=0
while contraseña != i:
    i= str(input("ingrese una contraseña: "))
    if contraseña == i:
        print("contraseña correcta")
    else: 
        print("contraseña incorrecta")

 
     
