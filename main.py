<<<<<<< HEAD
# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
=======
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
>>>>>>> 420598ad598151c24edc91633a5b4a8fdce32352
