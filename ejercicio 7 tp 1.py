'''Desarrollar una función que reciba como parámetros dos números enteros y devuelva el número que resulte de concatenar ambos valores'''
#funcion
def concatenar(a,b):
    a1= str(a)
    b1=str(b)
    c=a1+b1
    return c
#programa principal
num1=int(input("ingrese un numero: "))
num2=int(input("ingrese un numero: "))
g=concatenar(num1,num2)
print(g)