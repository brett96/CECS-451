import sys
import random
import numpy as np

class nQueens:
    def __init__(self, *args, **kwargs):
        self.numQueens = int(sys.argv[1])
        self.board = [['-' for i in range(self.numQueens)] for j in range(self.numQueens)]  # Generate empty board
        self.locations = []  # Keep track of location of queens
        self.xVals, self.yVals = [i for i in range(0, self.numQueens)], [i for i in range(0, self.numQueens)]   # Generate 2 lists for all possible x and y values
        for i in range(0, int(self.numQueens)):
            #done = False
            #while not done:
            xLoc = random.choice(self.xVals)    # Select random element from xVals as x-coordinate
            yLoc = random.choice(self.yVals)    # Select random element from yVals as y-coordinate
            self.locations.append((xLoc, yLoc))      # Add new coordinates to locations
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

    def checkAttacks(self):
        queenXLocs = []
        queenYLocs = []
        conflicts = []
        for queen in self.locations:
            init = (queen[0], queen[1]) # Save initial location of queen 
            xPos = queen[0]
            yPos = queen[1]
            if (xPos in queenXLocs or yPos in queenYLocs) and queen not in conflicts:
                conflicts.append(queen)
            queenXLocs.append(xPos)
            queenYLocs.append(yPos)
            while queen[0] > 0:  #Check up, left
                queen = (queen[0] - 1, queen[1] - 1)
                if (queen in self.locations) and queen not in conflicts:
                    conflicts.append(queen)
            queen = init
            while queen[0] > 0: # Check up, right
                queen = (queen[0] - 1, queen[1]+1)
                if (queen in self.locations) and queen not in conflicts:
                    conflicts.append(queen)
            queen = init
            while queen[0] < self.numQueens:
                queen  = (queen[0] + 1, queen[1] + 1)
                if (queen in self.locations) and queen not in conflicts:
                    conflicts.append(queen)
            queen = init    # Restore queen to initial location
            while queen[0] < self.numQueens:
                queen  = (queen[0] + 1, queen[1] - 1)
                if (queen in self.locations) and queen not in conflicts:
                    conflicts.append(queen)
            queen = init    # Restore queen to initial location
            
        return "Attacking pairs = " + str(conflicts)


if __name__ == "__main__":
    # 4 states
    agent1 = nQueens()
    print(agent1.checkAttacks())
    agent2 = nQueens()
    print(agent2.checkAttacks())
    agent3 = nQueens()
    print(agent3.checkAttacks())
    agent4 = nQueens()
    print(agent4.checkAttacks())

