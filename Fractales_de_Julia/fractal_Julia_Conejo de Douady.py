# -*- coding: utf-8 -*-
"""
Fractal (Conjunto) de Julia

Proyecto: Tesis Maestría 

Notas:
   Para detectar los valores que conforman el conjunto de Julia K(f_c) lleno, 
   aplicamos el "algoritmo de  tiempo de escape". En este evaluamos 
   recursivamente la expresión z_i+1 = (z_i)^2 + c, con  i=0,1,2,..; z_0 un 
   complejo y c un complejo constante. Si la sucesión {z_n} converge (i.e. el 
    |z_i+1| < 2 )  entonces z_0 esta en K(f_c), si por el contrario en algún 
   momento |z_i+1| > 2 la sucesión diverge y ese z_0 no perntenece a K(f_c). 
   Para implementar el Algoritmo "tiempo de escape" se usa una forma matricial 
   y una "mascara".

Acciones:
   1.- Obtiene y grafica el fractal de Julia 
   2.- Guarda el Fractal en Alta Definición (HD). Para obtener una imagen nítida 
   con calidad de fondo de pantalla, aumente la resolución a 3000x3000 píxeles
   (ancho, alto = 3000, 3000) y ajuste los puntos por pulgada (dpi=300). 

Referencias:
    - Singh  & Raman (2026). Python for Mathematical Thinking, Springer.  
      pag 358
    - Lapidus \&  Radunović (2020). \textit{An Invitation to Fractal 
      Geometry Fractal Dimensions, Self-Similarity  and Fractal Curves}, AMS.   
      pag 39  
    
Editor:  Roberto Méndez Méndez / Gemini
Creado:  24 Junio 2026
Editado: 12 Septiembre 2026
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros 
ancho, alto = 800, 600
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
R = 2

# Malla de números complejos (puntos z)
x = np.linspace(x_min, x_max, ancho)
y = np.linspace(y_min, y_max, alto)
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

# GRÁFICA
plt.figure(figsize=(10, 10))
# El conjunto "lleno" son las zonas claras (máximas iteraciones)
plt.imshow(imagen, extent=(x_min, x_max, y_min, y_max), cmap='OrRd',
           origin='lower')
cbar = plt.colorbar(shrink=0.75)
cbar.ax.set_ylabel(f'Iteraciones antes de |z| > {R}', fontsize=14)
plt.title(f'Conjunto de Julia "Conejo de Douady" \n c = {c.real}{c.imag:+}j',
          fontsize=15)
plt.xlabel('Eje Real', fontsize=14)
plt.ylabel('Eje Imaginario',  fontsize=14)

plt.tight_layout()
plt.savefig('fig_Fractal_Julia_Conejo_de_Douady.png', dpi=300)
plt.show()
plt.close()
print("Imagen guardada con éxito como ",
       "'fig_Fractal_Julia_Conejo_de_Douady.png'")


