"""
Learning some pygame
"""
from turtle import speed
import pygame
from pygame.locals import *

pygame.
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
RUNNING = True
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
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()

# uninitialize all imported pygame modules
pygame.quit()
