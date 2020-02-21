# F U N C I O N E S
def gregorianos(a,b,c):
    fecha=False
    lista30=[4,6,9,11]
    lista31=[1,3,5,7,8,10,12]
    if  a<=31 and b in lista31:
        fecha=True
    elif a<=30 and b in lista30:
        fecha=True
    elif a<=29 and  b==2 and (c%4==0 and c%100!=0) or (c%400==0):
        fecha=True
    elif a<=28 and b==2:
        fecha==True
    return fecha
# P R O G R A M A - P R I N C I P A L
dia=int(input('Ingrese un dia: '))
while dia <= 0:
    print('ERROR, el numero no corresponde a un dia')
    dia=int(input('Ingrese un dia: '))
mes=int(input('Ingrese un mes: '))
while mes <= 0:
    print('ERROR, el numero no corresponde a un mes')
    mes=int(input('Ingrese un mes: '))
ano=int(input('Ingrese un anio: '))
while ano <= 0:
    print('ERROR, el numero no corresponde a un ano ')
    ano=int(input('Ingrese un anio: '))
valor=gregorianos(dia,mes,ano)
if valor ==True:
    print('Fecha valida')
else:
    print('Fecha invalida')
