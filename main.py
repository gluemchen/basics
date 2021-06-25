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
scr = pygame.display.set_mode((600, 50))
title = pygame.display.set_caption("Pygame Window")
time.sleep(2)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.display.flip()
