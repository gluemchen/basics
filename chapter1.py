import pygame
from pygame.locals import *

pygame.init()
pygame.quit()

screen = display.set_mode((640, 480), RESIZABLE)

# initialized list of colors
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
background = GRAY
screen.fill(background)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background == RED
            elif event.key == pygame.K_r:
                background == GREEN
        if event.type == pygame.QUIT:
            running = False

pygame.quit()