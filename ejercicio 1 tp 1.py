def numeros(a,b,c):
    mayor=0
    if a>b:
        mayor=a
        if a>c:
            mayor=a
        if a<c:
            mayor=c
        if a==c:
            mayor=-1
    else:
        mayor=b
        if b>a:
            mayor=b
            if b<c:
                mayor=c
            if b==c:
                mayor=-1
        else:
            mayor=-1
    return mayor 
        
    
#programa principal
num=int(input("ingrese un numero:"))
while num<0:
    print("no es un numero positivo")
    num=int(input("ingrese un numero:"))
num1=int(input("ingrese un numero:"))
while num1<0:
    print("no es un numero positivo")
    num1=int(input("ingrese un numero:"))
num2=int(input("ingrese un numero:"))
while num2<0:
    print("no es un numero positivo")
    num2=int(input("ingrese un numero:"))
    
    
funcion= numeros(num,num1,num2)
if  funcion != -1:
    print("'el numero mayor es,", funcion)
else:
    print("no existe un numero mayor")           