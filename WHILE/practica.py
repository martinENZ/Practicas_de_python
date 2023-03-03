mayor=0
n=int(input("Número positivo:"))
while n >= 1:
   if n>mayor:
       mayor=n
   n=int(input("Número positivo:"))
print("Mayor número ingresado:", mayor)