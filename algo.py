import random

def check_win(grid):
    combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    flat_grid = []
    draw = True
    for y in grid:
        for x in y:
            flat_grid.append(x)
    p = ['O', 'X']
    for c in combinations:
        if flat_grid[c[0]].typ == flat_grid[c[1]].typ == flat_grid[c[2]].typ != None:
            return p[flat_grid[c[0]].typ]
    for i in flat_grid:
        if i.typ == None:
            draw = False
            break
    if draw:
        return 'Tie'
    return False

def playmove(grid):
    index = 0
    available = []
    best = -10000000000000
    bestmove = None
    for y in grid:
        for x in y:
            if x.typ == None:
                grid[index//3][index%3].typ = 1
                score = minimax(grid, 0, False)
                grid[index//3][index%3].typ = None
                if score > best:
                    best = score
                    bestmove = index
            index+=1
    return bestmove

scores = {
    'X': 10,
    'O': -10,
    'Tie': 0
}

def minimax(grid, depth, maximizing):
    result = check_win(grid)
    if result:
        return scores[result]
    if maximizing:
        index = 0
        bestscore = -1000000000000
        for y in grid:
            for x in y:
                if x.typ == None:
                    grid[index//3][index%3].typ = 1
                    score = minimax(grid, depth + 1, False)
                    grid[index//3][index%3].typ = None
                    bestscore = max(score, bestscore)
                index+=1
        return bestscore
    else:
        index = 0
        bestscore = 1000000000000
        for y in grid:
            for x in y:
                if x.typ == None:
                    grid[index//3][index%3].typ = 0
                    score = minimax(grid, depth + 1, True)
                    grid[index//3][index%3].typ = None
                    bestscore = min(score, bestscore)
                index+=1
        return bestscore

