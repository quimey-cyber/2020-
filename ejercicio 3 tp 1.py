def calcular(numero):
    suma=0
    for i in range(1,numero,4):
        suma+=(i**2)
    return suma
numero=int(input('Ingrese un numero MENOR a 100: '))
while numero>=100:
    numero=int(input('Ingrese un numero MENOR a 100: '))
resultado= calcular(numero)
print(resultado)
