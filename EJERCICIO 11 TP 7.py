'''11.Desarrollar una función que devuelva el elemento de valor mínimo de una matriz de M x N.'''
import random
# F U N C I O N E S
def menorValor(matriz,fila=0,menor=100):
    if fila<=len(matriz)-1:
        x=min(matriz[fila])
        if menor>x:
            menor=x
            return menorValor(matriz,fila+1,menor)
        else:
            return menorValor(matriz,fila+1,menor)
    else:
        return menor
def cargarMatriz(matriz):
    f=len(matriz)
    c=len(matriz[0])
    x=random.randint(1,9)
    for f1 in range(f):
        for c1 in range(c):
            matriz[f1][c1]=x
            x=random.randint(1,9)
# P R O G R A M A - P R I N C I P A L
matriz=[[0 for c in range(0,3)]for f in range(0,3)]
cargarMatriz(matriz)
print(matriz)
menor= menorValor(matriz)
print("El elemento de menor valor es: ", menor)