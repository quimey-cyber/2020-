import random
def ImprimirMatriz(mat, fila=0,columna=0):
    if fila==len(mat)-1 and columna == (len(mat[0])-1):
        print(mat[fila][columna], end=' ')
    elif fila<=(len(mat)-1) and columna <= (len(mat[0])-1):
        print(mat[fila][columna], end=' ')
        return ImprimirMatriz(mat,fila,columna+1)
    else:
        print()
        return ImprimirMatriz(mat,fila+1)
        
mat=[None]*2
for i in range(0,2):
    mat[i]=[None]*3
for j in range(0,2):
    for t in range(0,3):
        mat[j][t]=random.randint(1,9)

ImprimirMatriz(mat)