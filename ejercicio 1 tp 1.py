# funciones
def mayor(a,b,c):
    """buscar el mayor estrico dentro de tres parametros"""
    mayor=-1
    if a>b:
        if a>c:
            mayor=a
    elif b>a:
        if b>c:
            mayor=b
    if c>a:
        if c>b:
            mayor=c
    return mayor 
            
        
# programa principal
""" pedirle al usuario que ingrese 3 numeros por teclado """
a=int(input("ingrese un numero: "))
while a<0:
    print("ingrese un numero positivo ")
    a=int(input(": "))
b=int(input("ingrese un numero: "))
while b<0:
    print("ingrese un numero positivo ")
    b=int(input(": "))
c=int(input("ingrese un numero: "))
while c<0:
    print("ingrese un numero positivo ")
    c=int(input(": "))
buscarmayor= mayor(a,b,c)
print(buscarmayor)
    print("no existe un numero mayor")           
