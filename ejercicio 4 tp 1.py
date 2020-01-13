'''Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba,
como parámetro,la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes.
Realizar también un programa para verificar el comportamiento de la función.
Cantidad de viajes Valor del pasaje:
1 a 20: Averiguar valor actualizado
21 a 30: 20% de descuento sobre tarifa máxima
31 a 40: 30% de descuento sobre tarifa máxima
Más de 40: 40% de descuento sobre tarifa máxima
 En este caso,el valor del boleto sera de $20'''
#funcion
'''controla que el mes se haya ingresado correctamente'''
def control(a):
    cont=0
    for i in range (len(meses)):
        if mes==meses[i]:
            cont=cont+1
    return cont
'''multiplica la cantidad de viajes por el valor del boleto y aplica el descuento si es necesario'''
def calcular(a,b):
    if a>20 and a<31:
        c=(a*20)/100
        total= (a*b)-c
    if a >=31 and a<=40:
        c=(a*30)/100
        total=(a*b)-c
    if a>40:
        c=(a*40)/100
        total=(a*b)-c
    if a<=20:
        total=a*b
    return total
#programa principal
valorpasaje=20
print("valos del boleto:", "$", valorpasaje)
meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio","agosto","septiempre", "octubre", "noviembre", "diciembre"]
mes=str(input("ingrese mes: "))
cantidad=int(input("ingrese cantidad de viajes:"))
while cantidad<=0:
    print("no se realizaron viajes")
    cantidad=int(input("ingrese cantidad de viajes:"))

else:
    controlarmeses= control(mes)
    
    while controlarmeses==0:
        print("el mes ingresado no existe, por favor, ingrese el mes nuevamente")
        mes=str(input("ingrese mes: "))
        controlarmeses= control(mes)
    else:
        total=calcular(cantidad, valorpasaje)
        print("gasto total", mes, "= $", total)
    