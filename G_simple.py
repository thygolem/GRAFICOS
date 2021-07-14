# -*- coding: utf-8 -*-

'''

Basado en el código de Iván Rodríguez
https://www.youtube.com/watch?v=MvWCIbpvykE&list=PLG8UtYUFOQj4PwdP1SusjENu-fPOh7bnZ&index=4

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


x_2 = np.array(range(500))*0.1
y_2 = np.zeros(len(x_2))
for j in range(len(x_2)):
    y_2[j] = math.cos(x_2[j])

# Creamos el gráfico
plt.plot(x,y,'y--',x_2,y_2,'c_')

'''
Colores Matplotlib: 'r', 'g', 'b', 'c', 'm' 'y', 'k', 'w'
'''

'''
Tipos de lineas: '-', '--', '-_', ':', '_', 'O', 'v', '^', '<','>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', 'l'
'''


plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

plt.legend(['Seno', 'Coseno'])

plt.title("SENO ex: 1")



plt.ioff()
plt.show()
