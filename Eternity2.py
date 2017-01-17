#!/usr/bin/env python3

import pygame, pygame.locals, pygame.image
import sys

pygame.init()
pygame.display.set_caption('Eternity2')

image = pygame.image.load(" ".join(sys.argv[1:]))
screen = pygame.display.set_mode((image.get_width(), image.get_height()), pygame.NOFRAME)
screen.blit(image.convert(), (0,0))

pygame.display.flip()
while True:
    # if pygame.event.wait().type in (pygame.locals.QUIT, pygame.locals.KEYDOWN, pygame.locals.MOUSEBUTTONDOWN):
    if pygame.event.wait().type in (pygame.locals.QUIT, pygame.locals.MOUSEBUTTONDOWN):
        break
