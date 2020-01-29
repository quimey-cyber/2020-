# funciones
def billetes(b):
    lista=[]
    if b>=500:
        b500=b//500
        b=b-(b500*500)
        lista.append(b500)
    else:
        lista.append(0)
    if b>=100:
        b100=b//100
        b=b-(b100*100)
        lista.append(b100)
    else:
        lista.append(0)
    if b>=50:
        b50=b//50
        b=b-(b50*50)
        lista.append(b50)
    else:
        lista.append(0)
    if b>=20:
        b20=b//20
        b=b-(b20*20)
        lista.append(b20)
    else:
        lista.append(0)
    if b>=10:
        b10=b//10
        b=b-(b10*10)
        lista.append(b10)
    else:
        lista.append(0)
    if b>=5:
        b5=b//5
        b=b-(b5*5)
        lista.append(b5)
    else:
        lista.append(0)
    if b>=1:
        b1=b//1
        b=b-(b1*1)
        lista.append(b1)
    else:
        lista.append(0)
    return lista
        
        
# programa principal
divisas=[500,100,50,20,10,5,1]
"""se le pide al usuario que ingrese el valor de la compra y el abono """
"""controlar  las condiciones pedidas"""
valorcompra=int(input("ingrese el valor de la compra:"))
while valorcompra<0:
    print("error, ingrese el valor compra")
    valorcompra=int(input("ingrese el valor de la compra:"))
pago=int(input("ingrese el pago:"))
while pago<0:
    print("error, ingrese el pago correspondiente")
while valorcompra>pago:
    print("el pago es insuficiente")
    pago=int(input("ingrese el pago:"))
res=pago-valorcompra
print(res)
vuelto= billetes(res)

for i in range(len(divisas)):
    if vuelto[i] >0:
        print( vuelto[i], "billete(s) de", divisas[i])
