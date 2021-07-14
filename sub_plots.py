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
plt.subplot(221) # Dos filas por dos columnas en la posición 1
plt.plot(x,y,'--')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Representacion de funciones 1")
plt.subplot(222) # Dos filas por dos columnas en la posición 2
plt.plot(x_2,y_2,'*')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Representacion de funciones 2")
plt.subplot(223) # Dos filas por dos columnas en la posición 3
plt.plot(x,y,'o')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Representacion de funciones 3 ")
plt.subplot(224) # Dos filas por dos columnas en la posición 4
plt.plot(x_2,y_2,'-')
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Representacion de funciones 4")



plt.ioff()
plt.show()
