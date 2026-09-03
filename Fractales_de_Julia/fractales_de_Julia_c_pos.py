# -*- coding: utf-8 -*-
"""
Fractales de Julia con c = a + bj   a >= 0 y b >= 0 
    
Proyecto: Tesis Maestría 

Objetivo: Ver formas de Conjuntos de Julia con c = a + bj   a >= 0 y b >= 0 

Referencias:
    * Web: https://paulbourke.net/fractals/juliaset/
    - Singh  & Raman (2026). Python for Mathematical Thinking, Springer.    
    - https://matplotlib.org/stable/users/explain/colors/colormaps.html
    * Web: https://blbadger.github.io/julia-sets.html

Editor:  Roberto Méndez Méndez
Creado:  3 Agosto 2026
Editado: 2 Septiembre 2026
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la imagen y del plano complejo
ancho, alto = 1500, 1500
x_min, x_max = -1.3, 1.3
y_min, y_max = -1.3, 1.3
R = 2

# Constantes c 
c = ( 0.8j, 0.37 + 0.1j, 0.355 + 0.355j, 0.35 + 0.1j, 0.75, 0.3j )

# Malla de números complejos (puntos z)
x = np.linspace(x_min, x_max, ancho, endpoint=True)
y = np.linspace(y_min, y_max, alto, endpoint=True)

# Número de Ieraciones Máxima
max_iter = 300


# Crear la figura y la cuadrícula de ejes (2 filas, 2 columnas)
fig, axs = plt.subplots(3, 2, figsize=(8, 8))

j = 0 # índice de renglón

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
                                           cmap='GnBu', origin='lower')
    cbar = fig.colorbar(im, ax=axs[j, i%2], shrink=1)
    cbar.set_label(f'Iteraciones antes de |z| > {R}')
    axs[j, i%2].set_title(f'c = {c[i].real}{c[i].imag:+}j', 
                          fontsize=10)
    axs[j, i%2].set_xlabel('Eje Real', fontsize=10)
    axs[j, i%2].set_ylabel('Eje Imaginario', fontsize=10)
    
    if i%2 == 1:
        j = j + 1

plt.tight_layout()
fig.savefig('fig_Fractales_de_Julia_c_pos.png', dpi=400)
plt.show()
plt.close()
print("Imagen guardada con éxito como 'fig_Fractales_de_Julia_c_pos.png'")






