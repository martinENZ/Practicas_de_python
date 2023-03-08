#Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

def año_bisiesto(año):
    if (año % 4) == 0:
        if (año % 100) == 0:
            if (año % 400) == 0:
                print("Este año es un año BISIESTO")
            else:
                print("Este año NO es un año BISIESTO")   
        else:
            print("Este año es un año BISIESTO")
    else:
        print("Este año NO es un año BISIESTO")        

#print(año_bisiesto(2000))   
año_bisiesto(1992) 
año_bisiesto(2000)
año_bisiesto(1900)