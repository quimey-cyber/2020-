'''Para un número entero N menor de 100 recibido como parámetro, escribir un programa que utilice una función para devolver la suma de los cuadrados de aquellos
números entre 1 y N que están separados entre si por cuatro unidades. (1**2 + 5**2 +9**2 + 13**2 + …)'''
#funciones 
def secuencianumerica(a):
    lista=[]
    for i in range (1,a+1,4):
        lista.append((i**2))
    return lista

def suma(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma
#programa principal 
num=int(input("ingrese un numero: "))
while num<1 or num>100:
    print("el numero no cumple con la condicion pedida")
    num=int(input("ingrese un numero"))
p= secuencianumerica(num)
r=suma(p)
print("la suma total es", r)