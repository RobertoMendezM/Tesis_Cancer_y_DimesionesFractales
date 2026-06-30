# -*- coding: utf-8 -*-
"""
Fractal (Conjunto) de Julia

Proyecto: Tesis Maestría 

Notas:
   Para graficar el conjunto de Julia lleno, aplicamos el "algoritmo de 
   tiempo de escape". En este evaluamos recursivamente z_i+1 = (z_i)^2 + c  
   con z_0 = 0. Si el valor absoluto (módulo) de |z_i+1| es mayor a 2,
   en algún momento, la sucesión diverge. Los puntos 
   acotados son los que conforman al conjunto lleno de Julia.

Acciones:
   Guarda el Fractal en Alta Definición (HD). Para obtener una imagen nítida 
   con calidad de fondo de pantalla, aumente la resolución a 3000x3000 píxeles
   (ancho, alto = 3000, 3000) y ajuste los puntos por pulgada (dpi=300) 
   al guardar el archivo. 

Referencias:
    - Singh  & Raman (2026). Python for Mathematical Thinking, Springer.    
    - https://matplotlib.org/stable/users/explain/colors/colormaps.html
    - Gemini

Editor:  Roberto Méndez Méndez
Creado:  24 Junio 2026
Editado: 30 Junio 2026
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la imagen y del plano complejo
ancho, alto = 800, 600
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
R = 2

# Malla de números complejos (puntos z)
x = np.linspace(x_min, x_max, ancho, endpoint=True)
y = np.linspace(y_min, y_max, alto, endpoint=True)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Constante c para el conjunto de Julia ( Conejo de Douady)
c = -0.123 + 0.745j

# Número de Ieraciones Máxima
max_iter = 100

# Matriz para almacenar el # de iteraciones para que |z| > R 
imagen = np.zeros(Z.shape)

# Algoritmo "tiempo de escape" en forma matricial y usando una "mascara"
for n in range(max_iter):
    # Máscara de los puntos que aún no han escapado
    zona_acotada = np.abs(Z) <= R
    # Aplicar la función f(z) = z^2 + c solo a los puntos acotados
    Z[zona_acotada] = Z[zona_acotada]**2 + c
    # Guardar el número de iteración en las posiciones de puntos acotados
    imagen[zona_acotada] = n

# Graficar el resultado
plt.figure(figsize=(8, 8))
# El conjunto "lleno" son las zonas claras (máximas iteraciones)
plt.imshow(imagen, extent=(x_min, x_max, y_min, y_max), cmap='inferno', origin='lower')
plt.colorbar(label=f'Iteraciones antes de |z| > {R}')
plt.title(f'Conjunto de Julial lleno "Conejo de Douady", c = {c.real}+{c.imag}j')
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# Código para guardar la figura en un archivo
plt.figure(figsize=(10, 10))
plt.imshow(imagen, extent=(x_min, x_max, y_min, y_max), cmap='OrRd', origin='lower')
plt.axis('off') 
# Guarda la imagen  en alta definición sin bordes blancos
plt.savefig('julia_hd_Conejo de Douady.png', dpi=300, bbox_inches='tight', pad_inches=0)
plt.close()
print("Imagen guardada con éxito como 'julia_hd_Conejo de Douady.png'")
