
from nomina import Nomina
import pandas as pd 
nominas = []

while True:
    print("1. Ingresarnomina")
    print("2. Salir")

    opcion = input("Ingrese la opcion: ")

    if opcion == '1':
        renglon = []
        n = Nomina()
        salario = float(input("Ingrese el sueldo basico: "))
        diasL = float(input("Ingrese los dias liquidados: "))
        n.setSalarioBasico(salario)
        n.setDiasLiquidados(diasL)

        renglon.append({'variable': 'Salario Basico', 'Resultado': n.getSalarioBasico()})
        renglon.append({'variable': 'Dias Liquidados', 'Resultado': n.getDiasLiquidados()})
        renglon.append({'variable': 'Salario Devengado', 'Resultado': n.salarioDevengado()})
        renglon.append({'variable': 'Auxilio Transporte', 'Resultado': n.auxilioTransporte()})
        renglon.append({'variable': 'Total Devengado', 'Resultado': n.totalDevengado()})
        nominas.append(renglon)

    elif opcion == '2':
        print("Saliendo")
        break


# Escribir un Archivo plano
f = open('nominas.txt', 'w')
for i in nominas:
    f.write('****************************')
    for j in i:
        f.write(str(j) + "\n")
f.close()


