import pygame
import numpy as np

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0,0,0))
        surface = pygame.Surface((50,50))
        surface.fill((255,255,255))

        pygame.display.flip()
pygame.quit()
