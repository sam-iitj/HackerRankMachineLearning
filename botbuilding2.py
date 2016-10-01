#!/bin/python
def nextMove(n,r,c,grid):
    grid = map(lambda x:[elem for elem in x], grid)
    target = [0, 0] 
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "p":
                target = [i, j]
                break
    
    if target[0] - r < 0:
        return "UP"
    elif target[0] - r > 0:
        return "DOWN"
    elif target[1] - c > 0:
        return "RIGHT"
    elif target[1] - c < 0:
        return "LEFT"

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())
    
print nextMove(n,r,c,grid)

