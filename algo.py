import random

def playmove(grid):
    index = 0
    available = []
    for y in grid:
        for x in y:
            if x.typ == None:
                available.append(index)
            index+=1
    return random.choice(available) if len(available) > 0 else None