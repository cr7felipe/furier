#Importamos  la libreria  numpy
import math as mt
import numpy as np
#Creamos una funcion para obetenr An con la libreria de Numpy
PI = mt.pi
def obtenerAn (n):
    an = (1-mt.pow(-1,n))/(mt.pow(n,2)*PI)
    return an

#Creamos una funcion para obetenr Bn 
def ObtenerBn (n):
    return 1/n

#Creamos una funcion para obetenr A0 
def ObtenerAo():
    return PI / 2

#Creamos una funcion  que sume An, Bn, Angulo y el limite 
def Suma(limite,x):
    suma=0
    n=1
    while (n<=limite):
        an=obtenerAn(n)
        bn=ObtenerBn(n)
        sen=mt.sin(n*x)
        cos=mt.cos(n*x)

        suma = suma+an*cos+bn*sen
        n=n+1
    return suma

#El angulo se tiene que colocar en radianes 
def SerieF(x, n):
    return ObtenerAo()/2+Suma(n,x)


y = SerieF(-PI, 20)
print("x={},y={}".format(-PI,y))
#print(y)

x =np.arange(-PI,PI,0.5)
print(x)