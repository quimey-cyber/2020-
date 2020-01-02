#funcion 
def asterix(n):
    lista=[]
    a='**********'
    for i in range(n+1):
        lista.append(a)
    return lista

def asterixs(n):
    lista1=[]
    a='**'
    for i in range(n+1):
        lista1.append(a)
        a="{0}**".format(a)
    return lista1

#programa
num=int(input("ingrese la cantidad de filas que desea generar: "))
r= asterix(num)
j=asterixs(num)

for i in range (len(r)):
    print(r[i])
for i in range(len(j)):
    print(j[i])

