# -*- coding: utf-8 -*-

'''
Iván Rodríguez - 2017
Código generado para el canal de YouTube Piensa 3D
'''

# Importamos los módulos necesarios
import math
import numpy as np
from matplotlib import pyplot as plt

# Generamos los datos para el gráfico
plt.ion()
x = np.array(range(500))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])
plt.plot(x,y)

# Creamos el gráfico
plt.ioff()
plt.show()

