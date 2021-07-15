# This module adds system function use
import os

# the pygame module is all one needs for making cool python games
import pygame

# This module adds time related functions
import time

# This variable initializes the horizontal window position
X = 100

# This variable initializes teh vertical window position
Y = 100

os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (X, Y)

pygame.init()
scr = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
x, y = scr.get_size()
title = pygame.display.set_caption("Pygame Window Resizeable")
time.sleep(2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    scr.fill((255, 255, 255))
    pygame.draw.circle(scr, (200, 0, 0), (250, 250), 80)

pygame.display.flip()
pygame.display.quit()
print(x, y)
