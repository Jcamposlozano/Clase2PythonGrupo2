from Indicadores import *

valor = float(input("Ingrese un valor en dolare: "))


i = Indicadores()
resultado = float(i.indicadoresEconomicos()) * valor

print (resultado)


