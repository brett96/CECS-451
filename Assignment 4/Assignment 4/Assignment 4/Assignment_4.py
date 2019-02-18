import sys
import random
import numpy as np

class nQueens:
    def __init__(self, *args, **kwargs):
        self.numQueens = int(sys.argv[1])
        self.board = [['-' for i in range(self.numQueens)] for j in range(self.numQueens)]  # Generate empty board
        locations = []  # Keep track of location of queens
        self.xVals, self.yVals = [i for i in range(0, self.numQueens)], [i for i in range(0, self.numQueens)]   # Generate 2 lists for all possible x and y values
        for i in range(0, int(self.numQueens)):
            #done = False
            #while not done:
            xLoc = random.choice(self.xVals)    # Select random element from xVals as x-coordinate
            yLoc = random.choice(self.yVals)    # Select random element from yVals as y-coordinate
            locations.append((xLoc, yLoc))      # Add new coordinates to locations
            self.board[xLoc][yLoc] = "q"        # Add a queen at the coordinates
            self.xVals.remove(xLoc)             # Remove chosen xLoc from xVals so no other queen appears in the row
            self.yVals.remove(yLoc)             # Remove chosen yLoc from yVals so no other queen appears in the column
                #if (xLoc, yLoc) not in locations:
                #    locations.append((xLoc, yLoc))
                #    done = True
                #    self.board[xLoc][yLoc] = "q"

        print(np.array(self.board))
        geneticList = []
        for x in range(0, self.numQueens):
            y = 0
            done = False
            while not done:
                if self.board[x][y] == 'q':
                    geneticList.append(y)
                    done = True
                y += 1
        print(geneticList)


        print()

    def solve(self, board):
        pass

    def selection(self, board):
        pass

    def crossover(self, board):
        pass

    def mutation(self, board):
        pass

if __name__ == "__main__":
    # 4 states
    agent1 = nQueens()
    agent2 = nQueens()
    agent3 = nQueens()
    agent4 = nQueens()

