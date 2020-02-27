'''10.Escribir una función que sume todos los elementos de una matriz de M x N y devuelva el resultado.'''
import random 
def sumarElementos(matriz,fila=0,columna=0,suma=0):
    if fila <= len(matriz)-1 and columna<= len(matriz[0])-1:
        x=int((matriz[fila][columna]))
        return sumarElementos(matriz,fila,columna+1,suma+x)
    elif columna>len(matriz[0])-1:
        columna=0
        return sumarElementos(matriz,fila+1,columna,suma)
    else:
        return suma
    
def cargarMatriz(matriz):
    f1=len(matriz)
    c1=len(matriz[0])
    x=random.randint(1,9)
    for f in range(f1):
        for c in range(c1):
            matriz[f][c]=x
            x=random.randint(1,9)
            
matriz=[[0 for c in range(0,3)]for f in range(0,3)]
cargarMatriz(matriz)
suma=sumarElementos(matriz)
print(matriz)
print('La suma de todos los elementos es: ', suma)