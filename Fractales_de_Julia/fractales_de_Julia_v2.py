# -*- coding: utf-8 -*-
"""
Fractales de Julia
        "Dentrita", "San Marcos", "Galaxia", "Agujas de Siegel"
    
Proyecto: Tesis Maestría 

Notas:
   Para graficar el conjunto de Julia lleno, aplicamos el "algoritmo de 
   tiempo de escape". En este evaluamos recursivamente z_i+1 = (z_i)^2 + c  
   con z_0 = 0. Si el valor absoluto (módulo) de |z_i+1| es mayor a 2,
   en algún momento, la sucesión diverge. Los puntos 
   acotados son los que conforman al conjunto lleno de Julia.

Referencias:
    - Singh  & Raman (2026). Python for Mathematical Thinking, Springer.
    - Lapidus \&  Radunović (2020). \textit{An Invitation to Fractal 
      Geometry Fractal Dimensions, Self-Similarity  and Fractal Curves}, AMS.   
      pag 39, 41     
    - https://matplotlib.org/stable/users/explain/colors/colormaps.html 

Editor:  Roberto Méndez Méndez 
Creado:  3 Agosto 2026
Editado: 2 Septiembre 2026
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la imagen y del plano complejo
ancho, alto = 800, 600
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
R = 2

# Constantes c y nombres para los conjuntos de Julia 
c = (-1j, -0.75, -0.7 + 0.382j, -0.39054 - 0.58679j, 
                              0.427 - 0.376j, -0.473 - 0.554j)
names = ("Dentrita", "San Marcos", "Galaxia", "Agujas de Siegel", 
                "Disconexo", "Conexo")


# Malla de números complejos (puntos z)
x = np.linspace(x_min, x_max, ancho, endpoint=True)
y = np.linspace(y_min, y_max, alto, endpoint=True)

# Número de Ieraciones Máxima
max_iter = 100


# Crear la figura y la cuadrícula de ejes (2 filas, 2 columnas)
fig, axs = plt.subplots(3, 2, figsize=(8, 8))

j = 0
for i in range(len(c)):
    
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    # Matriz para almacenar el # de iteraciones para que |z| > R 
    imagen = np.zeros(Z.shape)

    # Algoritmo "tiempo de escape" en forma matricial y usando una "mascara"
    for n in range(max_iter):
        # Máscara de los puntos que aún no han escapado
        zona_acotada = np.abs(Z) <= R
        # Aplicar la función f(z) = z^2 + c solo a los puntos acotados
        Z[zona_acotada] = Z[zona_acotada]**2 + c[i]
        # Guardar el número de iteración en las posiciones de puntos acotados
        imagen[zona_acotada] = n
       

    # Graficar el resultado
    # El conjunto "lleno" son las zonas claras (máximas iteraciones)
    im = axs[j, i%2].imshow(imagen, extent=(x_min, x_max, y_min, y_max), 
                                           cmap='turbo', origin='lower')
    cbar = fig.colorbar(im, ax=axs[j, i%2], shrink=1)
    cbar.set_label(f'Iteraciones antes de |z| > {R}')
    axs[j, i%2].set_title(f'{names[i]} \n c = {c[i].real}{c[i].imag:+}j', 
                          fontsize=11)
    axs[j, i%2].set_xlabel('Eje Real', fontsize=11)
    axs[j, i%2].set_ylabel('Eje Imaginario', fontsize=11)
    
    
    if i%2 == 1:
        j = j + 1

plt.tight_layout()
fig.savefig('fig_Fractales_de_Julia_v2.png', dpi=300)
plt.show()
plt.close()
print("Imagen guardada con éxito como 'fig_Fractales_de_Julia_v2.png'")





