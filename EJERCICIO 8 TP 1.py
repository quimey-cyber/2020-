# funciones
def concatenar(n):
    """realizar una lista con el valor concatenado"""
    lista=[]
    n=str(n)
    for i in range(4):
        lista.append(n)
        n=n+lista[0]
    """pasar los elementos de la lista de texto a valores numericos"""
    for i in range(len(lista)):
        lista[i]=int(lista[i])
    return lista
def sumar(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i]
    return suma 
#programa principal
n=int(input("ingrese un numero del 1 al 9: "))
while n<0 and n>=10:
    print("el numero ingresado no cumple con la condicion pedida")
    n=int(input("ingrese un numero del 1 al 9: "))
concatex= concatenar(n)
suma1=sumar(concatex)
print(suma1)
