# Bibliotecas
import pygame
import random as rnd

from pygame.locals import *

# Screen
WIDTH = 500
HEIGHT = 500

# Grid
BORDER = 50
ROWS = 10
BLOCK = (WIDTH - 2*BORDER)//ROWS

# Game                                                                                                                                                                          
DELAY = 250
DELAY_MIN = 75
DELAY_STEP = 100

# RGB Colors
TEXT = (45, 45, 42)
BACKGROUND = (6, 214, 160)
SNAKE = (45, 45, 42)
GRID = (63, 94, 90)
BAIT = (239, 71, 111)


def main():
    # PyGame
    pygame.init()

    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('CarGame')

    # Auxiliary
    ext = False

    # Game
    score = 0
    delay = DELAY
    collided = False

    # Objects


    # Main loop
    while not ext:
        # Delay
        pygame.time.delay(max(DELAY_MIN, delay))

        # Eventos
        events = pygame.event.get()

        for e in events:
            # Evento de clique no X da janela
            if e.type == QUIT:
                ext = True

        # Atualização
        pygame.display.update()

    # Fim do jogo
    pygame.quit()


if __name__ == '__main__':
    main()
