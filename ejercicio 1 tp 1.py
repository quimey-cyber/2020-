def MayorEstricto(a,b,c):
    mayor=-1
    if a>b:
        if a != c:
            if a>c:
                mayor=a
            else:
                mayor=c
    elif b>a:
        if b!=c:
            if b>c:
                mayor=b
            else:
                mayor=c
    return mayor
num=int(input('Ingrese un numero: '))
while num<=0:
    print('El numero debe ser positivo')
    num=int(input('Ingrese un numero: '))
num1=int(input('Ingrese un numero: '))
while num1<=0:
    print('El numero debe ser positivo')
    num1=int(input('Ingrese un numero: '))
num2=int(input('Ingrese un numero: '))
while num2<=0:
    print('El numero debe ser positivo')
    num2=int(input('Ingrese un numero: '))
funcion=MayorEstricto(num,num1,num2)
if funcion==-1:
    print('No existe el mayor estricto')
else:
    print(funcion)               
