# las listas son una estructura de datos que nos permiten almacenar distintos datos
#estas son estructuras dinamicas que pueden mutar

from ctypes.wintypes import PINT


lis = [ "dato", 1 , True , 12,34]
print(lis)

print(lis[0])
lis[2]="hola"

print(lis[2])
lis.append("agregado")

print(lis)

print(lis.index("agregado"))