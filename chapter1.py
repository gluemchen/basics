"""
Learning some pygame
"""
import pygame

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

pygame.init()
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

RUNNING = True
background = GRAY
while RUNNING:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
            elif event.key == pygame.K_b:
                background = BLUE

    screen.fill(background)
    pygame.display.update()

pygame.quit()
