#!/usr/bin/python
def next_move(posr, posc, board):
    def funct(key):
        return abs(posr-key[0]) + abs(posc-key[1])
    
    indexes = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == "d":
                indexes += [[i, j]]
    
    indexes = sorted(indexes, key=funct)
    target = indexes[0]
   
    if board[posr][posc] == "d":
        print "CLEAN"
    elif target[0] - posr < 0:
        print "UP"
    elif target[0] - posr > 0:
        print "DOWN"
    elif target[1] - posc < 0:
        print "LEFT"
    elif target[1] - posc > 0:
        print "RIGHT"
    
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
