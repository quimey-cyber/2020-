# FUNCIONES
# creamos una lista con numeros al azar
import random
def crearlista():
    lista=[]
    j=random.randint(10,99)
 
    for i in range(j):
        numero=random.randint(1000,9999)
        lista.append(numero)
    return lista
# eleminamos el elemento que nos pide el usuario si este existe en la lista
def eliminar(lista, numero):
    while numero in lista:
        lista.remove(numero)
    return lista
# determinamos si la lista es capicua        
def listacapicua(lista):
    capicua=True
    a=0
    b=len(lista)-1
    while a<b:
        if lista[a] != lista[b]:
            capicua= False
            break
        a=a+1
        b=b-1
    return capicua
        
# PROGRAMA PRINCIPAL

#creamos la lista
lista=crearlista()
print(lista)
# sumamos todos los elementos
suma=sum(lista)
print("la suma de los elementos es",suma)
# eliminamos el numero que solicita el usuario
numero=int(input("ingrese un numero para eliminar de la lista:"))
elimix=eliminar(lista, numero)
print(elimix)
# determinamos si una lista es capicua o no 
lista3=[3,2,1,2,3]
lista_capicua=listacapicua(lista3)
if lista_capicua == True:
    print("lista capicua")
else:
    print("la lista no es capicua")
