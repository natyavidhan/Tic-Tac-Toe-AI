import random

def playmove(grid):
    index = 0
    available = []
    best = -10000000000000
    bestmove = None
    for y in grid:
        for x in y:
            if x.typ == None:
                grid[index//3][index%3].typ = 1
                score = minimax(grid)
                grid[index//3][index%3].typ = None
                if score > best:
                    best = score
                    bestmove = index
            index+=1
    return bestmove

def minimax(grid):
    return 1