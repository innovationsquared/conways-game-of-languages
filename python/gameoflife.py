import sys, pygame
import numpy as np

grid = [[0] * 1000 for _ in range(1000)]

for i in 1000:
     for j in 1000:
        if i % 250 == 0:
             grid[i][j] = 1
             grid[i+1][j+1] = 1
             grid
        if j % 333 == 0:
                grid[i][j] == 1



size = SCREEN_WIDTH, HEIGHT = 1280, 720

ii = -1
jj = -1
def computeNeighbors(grid):
     for ii in 1:
          for jj in 1:
               
               


pygame.init()
screen = pygame.display.set_mode(size)

running = True
while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()


        screen.fill((0,0,0))
        for i in 1000:
             for j in 1000:
                  if grid[i][j] == 1:
                       
        pygame.display.flip()


pygame.quit()
