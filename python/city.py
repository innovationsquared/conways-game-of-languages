from const import *
#initialize 100x100 array for 10x10 cubes
#0 for dead, 1 for alive (All dead at start)
class City:
    city = [[0 for i in range(NUM_CUBES)] for j in range(NUM_CUBES)]

    for row in city: 
            print(row)


    def initializeScreen(surface):
            for i in range(NUM_CUBES):
                    for j in range(NUM_CUBES):
