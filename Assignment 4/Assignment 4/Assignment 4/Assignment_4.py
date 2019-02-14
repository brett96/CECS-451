import sys
import random
import numpy as np

class nQueens:
    def __init__(self, *args, **kwargs):
        numQueens = int(sys.argv[1])
        board = [[0 for i in range(numQueens)] for j in range(numQueens)]
        for i in range(0, int(numQueens)):
            xLoc = random.randint(0, numQueens - 1)
            yLoc = random.randint(0, numQueens - 1)
            board[xLoc][yLoc] = "q"
        print(np.array(board))


if __name__ == "__main__":
    agent = nQueens()

