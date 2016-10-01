#!/bin/python
def displayPathtoPrincess(n,grid):
    grid = map(lambda x: [elem_ for elem_ in x], grid)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "m":
                start_pos = [i, j]
            if grid[i][j] == "p":
                target_pos = [i, j]

    while start_pos != target_pos:
        if target_pos[1] - start_pos[1] > 0:
            print "RIGHT"
            start_pos[1] = start_pos[1] + 1
        elif target_pos[1] - start_pos[1] < 0:
            print "LEFT"
            start_pos[1] = start_pos[1] - 1
        elif target_pos[0] - start_pos[0] < 0:
            print "UP"
            start_pos[0] = start_pos[0] - 1
        elif target_pos[0] - start_pos[0] > 0:
            print "DOWN"
            start_pos[0] = start_pos[0] + 1

#print all the moves here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
