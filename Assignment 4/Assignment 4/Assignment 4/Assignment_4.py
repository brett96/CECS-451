import sys
import random
import numpy as np

class nQueens:
    def __init__(self, *args, **kwargs):
        self.numQueens = int(sys.argv[1])
        self.board = [["-" for i in range(self.numQueens)] for j in range(self.numQueens)]
        locations = []
        for i in range(0, int(self.numQueens)):
            done = False
            while not done:
                xLoc = random.randint(0, len(self.board)-1)
                yLoc = random.randint(0, len(self.board)-1)
                if (xLoc, yLoc) not in locations:
                    locations.append((xLoc, yLoc))
                    done = True
                    self.board[xLoc][yLoc] = "q"

        print(np.array(self.board))

    def solve(self, board):
        pass

if __name__ == "__main__":
    agent = nQueens()

