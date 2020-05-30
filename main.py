# Bibliotecas
import pygame
import random as rnd

from pygame.locals import *

# Screen
WIDTH = 450
HEIGHT = 550

# Grid
BORDER = {'h': 30, 'w': 25}

LANE_PADDING = 4
ROWS = 3  # Must be positive
BLOCK = (WIDTH - 2*BORDER['w'] - (ROWS-1)*LANE_PADDING)//ROWS

print (BLOCK)

# Game
DELAY = 300
DELAY_MIN = 75
DELAY_STEP = 100

# Controls
UP, DOWN, LEFT, RIGHT = (0, 2, 1, 3)

# RGB Colors
TEXT = (45, 45, 42)
BACKGROUND = (6, 214, 160)
SNAKE = (45, 45, 42)
GRID = (63, 94, 90)
BAIT = (239, 71, 111)


class Cube(object):
    size = BLOCK//3  # Rectangle size
    border = 3  # Rectangle border
    padding = border + 2  # Rectangle padding
    inner = size - (2*padding)  # Inner rectangle

    @staticmethod
    def draw(surface, x, y, color=GRID):
        pygame.draw.rect(surface, color,
                         (x, y, Cube.size, Cube.size), Cube.border)
        pygame.draw.rect(surface, color,
                         (x + Cube.padding, y + Cube.padding, Cube.inner, Cube.inner))


class Car(object):

    def __init__(self, position, color):
        self.x = position[0]
        self.y = position[1]

        self.color = color

    def move(self, surface, dir_=DOWN, distance=BLOCK):
        if dir_ == UP:
            self.y -= distance
        elif dir_ == DOWN:
            self.y += distance
        elif dir_ == LEFT:
            self.x -= distance
        elif dir_ == RIGHT:
            self.x += distance

    def draw(self, surface):
        # Row 1
        Cube.draw(surface, self.x + BLOCK, self.y, self.color)

        #print(self, self.x + BLOCK, self.y, self.color)

        # Row 2
        '''Cube.draw(surface, self.x, self.y+BLOCK, self.color)
        Cube.draw(surface, self.x+BLOCK, self.y+BLOCK, self.color)
        Cube.draw(surface, self.x+(2*BLOCK), self.y+BLOCK, self.color)
        # Row 3
        Cube.draw(surface, self.x+BLOCK, self.y+(2*BLOCK), self.color)
        # Row 4
        Cube.draw(surface, self.x, self.y+(3*BLOCK), self.color)
        Cube.draw(surface, self.x+BLOCK, self.y+(3*BLOCK), self.color)
        Cube.draw(surface, self.x+(2*BLOCK), self.y+(3*BLOCK), self.color)'''


class Window(object):

    @staticmethod
    def draw(surface, score=0):
        # Background
        surface.fill(BACKGROUND)

        pygame.draw.rect(
            surface, GRID,
            (
                BORDER['w'],
                BORDER['h'],
                WIDTH - 2*BORDER['w'],
                HEIGHT - 2*BORDER['h']
            ), 2
        )

        # Score
        text = Window.font.render(f'PONTOS: {score}', True, TEXT)
        surface.blit(text, (BORDER['w'], BORDER['h'] - 20))


def main():
    # PyGame
    pygame.init()

    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('CarGame')

    Window.font = pygame.font.SysFont('arial', 18)

    print(Cube.size, BLOCK)

    # Auxiliary
    ext = False

    # Game
    score = 0
    delay = DELAY
    collided = False

    # Objects
    cars = []

    def pos(x): return (rnd.randint(5, WIDTH-75), rnd.randint(5, WIDTH-75))
    def color(x): return (rnd.randint(0, 255),
                          rnd.randint(0, 255), rnd.randint(0, 255))

    for i in range(3):
        cars.append(Car(pos(0), color(0)))

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

        Window.draw(surface)

        for c in cars:
            c.draw(surface)
            #c.move(surface)

        # Atualização
        pygame.display.update()

    # Fim do jogo
    pygame.quit()


if __name__ == '__main__':
    main()
