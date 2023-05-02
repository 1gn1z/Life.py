# Importamos las librerias necesarias:

import pygame
import numpy as np
# "np" es un alias, para no tener que escribir numpy.funcion | es mejor np.funcion


# Definir los colores que se usarán en el juego (valores RGB)
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Dimensiones de la ventana del juego y velocidad actualización
WINDOW_SIZE = (500, 500)    # píxeles
FPS = 60                    # 60 cuadros por segundo

# Inicializar la ventana de Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE) # la pantalla se muestra con el tamaño indicado
pygame.display.set_caption("Life by BytePunk")

# Creación de matriz (50x50) de 0's y 1's aleatorios para representar las celdas
GRID_SIZE = (50, 50)
GRID = np.random.randint(2, size=GRID_SIZE)


# Definir una función para dibujar la matriz GRID en la pantalla
def draw_grid():
    for i in range(GRID_SIZE[0]):       # itera por el primer valor de GRID_SIZE (50), es decir, itera por las FILAS
        for j in range(GRID_SIZE[1]):   # itera por el segundo valor de GRID_SIZE (50), es decir, itera por las COLUMNAS

            # el color es blanco si la coordenada (i, j) vale 1, osea si la celula esta viva, de lo contrario negro (muerta)
            color = WHITE if GRID[i, j] == 1 else BLACK
            
            # Por cada iteración va dibujando un cuadrado de 10 píxeles
            pygame.draw.rect(screen, color, (i*10, j*10, 10, 10))
            
            # Lo mismo que el anterior pero este dibuja un CONTORNO gris de 1 píxel (último argumento)
            pygame.draw.rect(screen, GRAY, (i*10, j*10, 10, 10), 1)
            
            
# La función draw.rect toma 4 argumentos (último opcional)  

# 1. superficie donde se dibujará el rectangulo ("screen" en este caso)
# 2. color del rectangulo
# 3. TUPLA que contiene las coordenadas X y Y y el tamaño del rectangulo (en este caso 10 píxeles)
# 4. Opcional. ancho del borde del rectangulo (en este caso gris, 1 píxel)
# pygame.draw.rect(screen, GRAY, (i*10, j*10, 10, 10), 1)

# Bucle infinito para pruebas
while True:
    pass

draw_grid()