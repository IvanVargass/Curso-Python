# Poner a prueba la Ley de los Grandes Números para N números
# aletaorios de la distribución normal con medio = 0, stdev = 1
#
# Crear un script en Python que cuente cuántas veces cae un número de
# estos entre -1 y 1 y divide por la cantidad total de observaciones
#
# Sabes que E(X) = 68.2%

import numpy as np 
from numpy.random import randn

obs = int(input("Ingrese el número de observaciones: "))
cont = 0

for i in randn(obs):
    if i >= -1 and i <=1 :
        cont = cont + 1

media = (cont/obs)*100
print("La media es: " ,media)

