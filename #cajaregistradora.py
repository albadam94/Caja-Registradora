#Caja Registradora

from typing import Text


nm=Text(input("Ingrese nombre empleado: "))
print ("Hola "+nm)

ic=int(input("Ingrese cantidad producto: "))

acu=0

for i in range (0,ic,1):
    pro=Text(input("Ingrese producto: "))
    print (pro)
    valor=int(input("Ingrese valor del producto: "))
    print (valor)
    acu= acu+valor
print ("Total a pagar: ",+acu)
billete=int(input("Ingrese denominacion del billete o moneda: "))
total=(billete-acu)  
print ("La devuelta es: ",+total)
print("Gracias por tu compra")






    