'''Desarrollar una función que reciba tres números enteros positivos y verifique si
corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
según la fecha sea correcta o no.'''

#funcion 
def Positivo(a):
    while a<0:
        a=int(input("ingrese un numero positivo: "))
    return a 
    

def fecha(a,b,c):
    boole=True
    añobi=False
    if c%4 == 0 and (c%100 == 0 and c%400 == 0):
        añobi=True
    if b <= 12 and (a <= 31):
        if (a == 30 and b%2 == 1) or (a == 31 and b%2 == 0):
            boole=False
        if b == 2 and (a >= 28):
            boole=False
        if b == 2 and (añobi==True and a >= 29):
            boole=False
    else:
        boole=False
    return boole

#programa
''' el usuario debe ingresar las fechas por teclado, a continuacion el programa llama a la funcion para controlar que el numero ingresado sea positivo'''
dia=int(input("ingrese el dia: "))
f=Positivo(dia)
mes=int(input("ingrese un mes: "))
g=Positivo(mes)
año=int(input("ingrese año: "))
r=Positivo(año)
''' llamamos a la funcion para controlar la fecha ingresada '''
resultado= fecha(f,g,r)

if resultado == True:
    print(f,"/",g, "/", r, "es una fecha valida")
if resultado == False:
    print(f,"/",g, "/", r, "es una fecha invalida")



