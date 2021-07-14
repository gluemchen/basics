"""
Learning some pygame
"""
<<<<<<< HEAD
# Here i import all the modules that i need
import pygame
import pygame.image
import pygame.display
import pygame.event
import pygame.draw

from turtle import speed
=======

import pygame
import pygame.event
import pygame.display
import pygame.rect
import pygame.image
import pygame.draw
>>>>>>> 0693770479e2c8bf5f90956d110ccdf0a4f07f76
from pygame.locals import *
from turtle import speed

# resoloution
size = 1024, 768
width, height = size

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

# Keys paired to colors
key_dict = {
    K_k: BLACK,
    K_r: RED,
    K_g: GREEN,
    K_b: BLUE,
    K_y: YELLOW,
    K_c: CYAN,
    K_m: MAGENTA,
    K_w: WHITE,
}

# initialize all imported pygame modules
pygame.init()

# initializing a resizable screen
screen = pygame.display.set_mode((size), RESIZABLE)

# By default Programm is always running
RUNNING = True

# Default fill color of screen range
background = GRAY

ball = pygame.image.load("intro_ball.gif")
rect = ball.get_rect()
speed = [2, 2]

while RUNNING:
    for event in pygame.event.get():
        print(key_dict)
        print(event)
        rect = rect.move(speed)

        if event.type == QUIT:
            RUNNING = False
        if event.type == MOUSEBUTTONDOWN:
            print(event)
        if event.type == MOUSEBUTTONDOWN:
            print(event)
        if event.type == MOUSEMOTION:
            print(event)
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                caption = "Background Color = " + str(background)
                pygame.display.set_caption(caption)
        if rect.left < 0 or rect.right > width:
            speed[0] = -speed[0]
        if rect.top < 0 or rect.bottom > height:
            speed[1] = -speed[1]

    screen.fill(background)
<<<<<<< HEAD
    pygame.draw.rect(screen, BLUE, (50, 20, 120, 100), 1, 3)
    pygame.draw.ellipse(screen, BLUE, (100, 60, 120, 100), 1)
    pygame.draw.rect(screen, BLUE, (150, 100, 120, 100), 1, -1, 3)
    pygame.draw.ellipse(screen, BLUE, (200, 140, 120, 100), 2)
    pygame.draw.rect(screen, BLUE, (250, 180, 120, 100), 1, -1, -1, 3)
    pygame.draw.ellipse(screen, BLUE, (300, 220, 120, 100), 3)
    pygame.draw.rect(screen, BLUE, (350, 260, 120, 100), 1, -1, -1, -1, 3)
    pygame.draw.ellipse(screen, BLUE, (400, 300, 120, 100), 4)
    pygame.draw.rect(screen, BLUE, (450, 340, 120, 100), 1, -1, -1, -1, -1, 3)
    pygame.draw.ellipse(screen, RED, rect, 1)
=======
    pygame.draw.rect(screen, RED, (50, 20, 120, 100))
    pygame.draw.rect(screen, RED, rect, 1)
>>>>>>> 0693770479e2c8bf5f90956d110ccdf0a4f07f76
    screen.blit(ball, rect)
    pygame.display.update()

# uninitialize all imported pygame modules
pygame.quit()
