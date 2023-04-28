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
