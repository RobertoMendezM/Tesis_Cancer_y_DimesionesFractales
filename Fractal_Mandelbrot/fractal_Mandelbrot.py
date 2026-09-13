# -*- coding: utf-8 -*-
"""
Fractal (Conjunto) de Mandelbrot

Proyecto: Tesis Maestría 

Notas:
   Para detectar los valores que conforman el conjunto de Mandelbrot M, 
   aplicamos el "algoritmo de escape" con la función f_c(z) = z^2 + c. 
   En este evaluamos recursivamente la expresión z_i+1 = (z_i)^2 + c  
   con z_0 = 0, c compleja, i=0,1,2,... .  
   Si la órbita {z_i} es acotada (i.e. |z_i+1| < 2 ), entonces c pertenece a M,
   si por el contrario en algún momento |z_i+1| > 2 la sucesión diverge y ese
   c no perntenece a M. 
   Para implementar el Algoritmo "tiempo de escape" se usa una forma matricial 
   y una "mascara".

Acciones:
   1.- Obtiene y grafica el fractal de Mandelbrot
   2.- Guarda la imagen del fractal. 

Referencias:
    - Singh  & Raman (2026). Python for Mathematical Thinking, Springer.  
      pag 355
    - Lapidus &  Radunović (2020). \textit{An Invitation to Fractal 
      Geometry Fractal Dimensions, Self-Similarity  and Fractal Curves}, AMS.   
      pag 39  
    
Editor:  Roberto Méndez Méndez 
Creado:  13 Septiembre 2026
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros 
x_lim = [-2, 0.7]
y_lim = [-1.2, 1.2]
puntos = 2000
N_itera = 600
R=2

def mandelbrot(xr, yr, puntos, N_iter):
    if puntos <= 0:
        raise ValueError("puntos debe ser positivo")
    if N_iter <= 0:
        raise ValueError("max_iter debe ser positivo")
    if R <= 0:
        raise ValueError("R debe ser positivo")
        
    x = np.linspace(xr[0], xr[1], puntos)
    y = np.linspace(yr[0], yr[1], puntos)
    
    # Matriz compleja: puntos x puntos
    C = x[:,None] + 1j*y[None,:]
    
    Z = np.zeros_like(C, dtype=complex)
    M = np.full(C.shape , N_iter, dtype=int)
    R2 = R*R
    for n in range(N_iter):
        mask = (Z.real**2 + Z.imag**2) < R2
        
        if not mask.any():
            break
        
        # Forma eficiente para Z[mask] = Z[mask]**2 + C[mask]                  
        np.square(Z, out=Z, where=mask)
        np.add(Z, C, out=Z, where=mask)
        
        escape = mask & ((Z.real**2 + Z.imag**2)>=R2)
        M[escape] = n+1
    return  M

M = mandelbrot(x_lim, y_lim, puntos, N_itera)

# Gráfica 
plt.figure(figsize=(10, 10))
# El conjunto "lleno" son las zonas claras (máximas iteraciones)
plt.imshow(M.T, extent=(x_lim[0], x_lim[1], y_lim[0], y_lim[1]), cmap='Greens',
           origin='lower', interpolation='nearest')
cbar = plt.colorbar(shrink=0.67)
cbar.ax.set_ylabel('Iteraciones antes de |z| > 2', fontsize=14)
plt.title('\n Conjunto de Mandelbrot \n', fontsize=20)
plt.xlabel('Eje Real', fontsize=14)
plt.ylabel('Eje Imaginario',  fontsize=14)

plt.tight_layout()
plt.savefig('fig_Fractal_Mandelbrot.png', dpi=300, bbox_inches='tight',
             pad_inches=0.16)
plt.show()
plt.close()
print("Imagen guardada con éxito como ",
       "'fig_Fractal_Mandelbrot.png'")