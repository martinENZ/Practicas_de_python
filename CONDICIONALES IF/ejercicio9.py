#Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.


#año = int(input("ingrese un año: "))
año= 1940
biciesto = (año % 4)


print(biciesto)

if  biciesto == 0: 
    paso100 = (año // 4)
    print (paso100)

    if (paso100 % 100) != 0:
        print(paso100%100)
    

