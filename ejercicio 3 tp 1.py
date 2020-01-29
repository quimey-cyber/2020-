'''Para un número entero N menor de 100 recibido como parámetro, escribir un programa que utilice una función para devolver la suma de los cuadrados de aquellos
números entre 1 y N que están separados entre si por cuatro unidades. (1**2 + 5**2 +9**2 + 13**2 + …)'''
# funciones
def lista(n):
    lista1=[]
    for i in range(1,n+1,4):
        lista1.append(i**2)
    return lista1
def sumacuadrados(x):
    suma1=0
    for i in range(len(x)):
        suma1=suma1+x[i]
    return suma1
    #programa principal
""" pedirle al ususario que ingrese un numero y controlar que cumpla con la condicion pedida"""
n=int(input("ingrese un numero entero menor a 100: "))
while n>=100:
    print("ingrese un numero menor a 100")
    n=int(input(": "))
"""creamos la lista con los numeros requeridos y los sumamos"""
calcular= lista(n)
cuadrados= sumacuadrados(calcular)
print("la suma total es", cuadrados)
