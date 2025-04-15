def checkNeighbors(arr):
    counter = 0
    for row in range([-1, 0, 1]):
        for col in range([-1, 0, 1]):
            if arr[row][col] == 1:
                counter+=1
    return counter

#If a cell has less than two neighbors, it dies.
def ruleOne(arr):
    nbrs = checkNeighbors(arr)
    
    pass
#If a cell has two or three neighbors, it lives.
def ruleTwo(arr):
    nbrs = checkNeighbors(arr)
    pass
#If a cell has more than three neighbors, it dies.
def ruleThree(arr):
    nbrs = checkNeighbors(arr)
    pass
#If a cell has exactly 3 neighbors, a new piece is created.
def ruleFour(arr):
    nbrs = checkNeighbors(arr)
    pass