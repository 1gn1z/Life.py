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

# Definir una función para ACTUALIZAR la matriz "GRID" en cada iteración del juego

def update_grid():
    global GRID     # global indica que "GRID" es la misma variable que está fuera de esta función. "GRID" se puede modificar desde esta función
    new_grid = np.zeros(GRID_SIZE)  # Se crea una nueva matriz del mismo tamaño que la matriz original actual.
    
    # Se itera sobre todas las celdas de la matriz GRID
    for i in range(GRID_SIZE[0]):
        for j in range(GRID_SIZE[1]):
            
            # Se calcula el número de vecinos vivos que tiene cada celda
            # Se obtiene una submatriz de 3x3 centrada en la celda actual
            # Se usa max y min para asegurarse de no salirse de los límites de la matriz GRID
            neighbors = np.sum(GRID[max(0, i-1):min(i+2, GRID_SIZE[0]), max(0, j-1):min(j+2, GRID_SIZE[1])]) - GRID[i,j]


            # Se aplican las reglas del juego
                        
            # 1. Si una célula está viva y tiene 2 o 3 vecinos vivos, sobrevive. SI NO (si tiene solo 1 vecino vivo) muere por SOLEDAD.
            # 2. Si una célula está viva y tiene MÁS de 3 vecinos vivos muere por SOBREPOBLACIÓN.
            # 3. Si una célula MUERTA tiene exactamente 3 vecinos vivos revive. SI NO continua muerta.
                        
                        
            # Estas reglas se pueden resumir en 2 condiciones:
                        
            # Si una célula viva tiene 2 o 3 vecinos vivos, sobrevive:
            if GRID[i, j] == 1 and neighbors in (2, 3):
                new_grid[i, j] = 1
                            
            # Si una célula está muerta y tiene exactamente 3 vecinos vivos, revive:
            elif GRID[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    # Se actualiza la matriz GRID con la nueva matriz
    GRID = new_grid



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


# Bucle principal del juego

# Creamos un objeto clock para controlar la velocidad de actualización del juego:
clock = pygame.time.Clock()

# Dentro del bucle
while True:
    # Se actualiza la pantalla y posteriormente se dibuja
    update_grid()
    draw_grid()

    # Actualizar la pantalla 
    pygame.display.update()
    
    # y esperar la siguiente iteración
    clock.tick(FPS)
    # el método tick espera el tiempo suficiente para que el juego se actualice a la velocidad deseada
    

    # Manejar los eventos del usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()