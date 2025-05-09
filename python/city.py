from const import *
import pygame
import random
#initialize 100x100 array for 10x10 cubes
#0 for dead, 1 for alive (All dead at start)
class City:
    def initializeCity(self):
        self.city = [[0 for i in range(NUM_CUBES)] for j in range(NUM_CUBES)]
        for i in range(10000):
             self.city[random.randrange(0,NUM_CUBES - 1)][random.randrange(0,NUM_CUBES - 1)] = 1
        return self.city

    # for row in city: 
    #         print(row)


    def drawScreen(self, surface, arr):
            for row in range(NUM_CUBES):
                    for col in range(NUM_CUBES):
                        if arr[row][col] == 1:
                              pygame.draw.rect(surface, (255,255,0), (SQ_SIZE * col, SQ_SIZE * row, SQ_SIZE, SQ_SIZE))

    def checkNeighbors(self, arr, row, col):
        counter = 0
        #check neighbors
        # (-1,-1),(-1,0),(-1,1)
        # (0,-1), (0,0), (0,1)
        # (1,-1), (1,0), (1,1)
        for i in range(-1, 2):
            for j in range(-1,2):
                if (i == 0 and j == 0): 
                     continue
                if in_range(row + i, col + j) and arr[row + i][col + j] == 1:
                    counter+=1
        return counter

    def evolve(self,arr):
        arr2 = [row[:] for row in arr]
        for row in range(NUM_CUBES):
            for col in range(NUM_CUBES):
                num = self.checkNeighbors(arr, row, col)
                match num: 
                        #If a cell has less than two neighbors, it dies. 
                        case num if num < 2 :
                            arr2[row][col] = 0
                        #If a cell has two or three neighbors, it lives.
                        case num if num == 2 :
                            continue 
                        #If a cell has exactly 3 neighbors, a new piece is created.
                        case num if num == 3:
                            arr2[row][col] = 1
                        #If a cell has more than three neighbors, it dies.
                        case num if num > 3 :
                            arr2[row][col] = 0
                        case _:
                            continue            
        return arr2


@staticmethod
def in_range(*args):
    for arg in args:
        if arg < 0 or arg > NUM_CUBES - 1:
            return False
    return True