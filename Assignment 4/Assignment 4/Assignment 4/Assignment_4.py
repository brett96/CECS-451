import sys
import random
import numpy as np
import math

class nQueens:
    def __init__(self, *args, **kwargs):
        self.numQueens = int(sys.argv[1])
        self.k = int(sys.argv[2])
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

        #print(np.array(self.board))
        geneticList = []
        for x in range(0, self.numQueens):
            y = 0
            done = False
            while not done:
                if self.board[x][y] == 'q':
                    geneticList.append(y)
                    done = True
                y += 1
        #print(geneticList)


        #print()
 

    def generatePopulationList(self):
        populationList = []
        for i in range(int(sys.argv[2])):
            populationList.append([x[0] for x in self.locations] )
        return populationList

    def generateStates(self):   # Genrate 'k' states
        #agents = [] # List containing all states (aka boards)
        agents = {} # Dictionary assigning each agent an int value
        fitnesses = {}  # Dictionary assigning each agent's int to its fitness
        for i in range(0, int(sys.argv[2])):
            agent = nQueens()
            #agents.append(agent)
            agents[i+1] = agent
            agent.show()
            #print("Attacks: " + str(agent.checkAttacks()))
            attackingPairs = agent.checkAttacks()
            fitness = agent.calculateFitness(attackingPairs)
            fitnesses[i+1] = fitness
            print("Genetic List = " + str(agent.getGeneticList()))
        totalStateSum = sum(fitnesses)
        for f in fitnesses:
            print("Fitness = " + str(fitnesses[f]/totalStateSum))
        fitLength = len(fitnesses)
        for i in range(0, fitLength // 2):
            fitnesses.pop(min(fitnesses))
        
        parent1 = max(fitnesses.values())
        result = agents[1].getGeneticList()
        for i in range(len(fitnesses.items())):
            if fitnesses.get(i+1) == parent1:
                result = agents[i+1].getGeneticList()
                print(result)
                fitnesses.pop(i+1)

        print(result)
        parent2 = max(fitnesses.values())
        for i in range(len(fitnesses.items())):
            if fitnesses.get(i+1) == parent1:
                result = agents[i+1].getGeneticList()
                fitnesses.pop(i+1)
        print(result)
        #fitnesses.pop(parent1)
        #parent2 = max(fitnesses.values())




    def show(self): # Print out board & queens
        print(np.array(self.board))
        #print()

    def getGeneticList(self):
        geneticList = []
        for x in range(0, self.numQueens):
            y = 0
            done = False
            while not done:
                if self.board[x][y] == 'q':
                    geneticList.append(y)
                    done = True
                y += 1
        return geneticList

    def selection(self, board):
        pass

    def crossover(self, board):
        pass

    def mutation(self, board):
        pass

    def calculateFitness(self, attackingPairs):
        f = math.factorial
        return ((f(self.numQueens) / f(2) / f(self.numQueens - 2)) - attackingPairs)

    def checkAttacks(self): # Get attacking pairs
        conflicts = []  # List containing tuples of attacking pairs
        for queen in self.locations:
            init = (queen[0], queen[1]) # Save initial location of queen 

            while queen[0] > 0:  #Check up, left
                queen = (queen[0] - 1, queen[1] - 1)
                if (queen in self.locations) and (queen, init) not in conflicts:
                    conflicts.append((queen, init))
            queen = init    # Return queen to initial state
            while queen[0] > 0: # Check up, right
                queen = (queen[0] - 1, queen[1]+1)
                if (queen in self.locations) and (queen, init) not in conflicts:
                    conflicts.append((queen, init))
            queen = init
            while queen[0] < self.numQueens:    # Check down, right
                queen  = (queen[0] + 1, queen[1] + 1)
                if (queen in self.locations) and (queen, init) not in conflicts:
                    conflicts.append((queen, init))
            queen = init    # Restore queen to initial location
            while queen[0] < self.numQueens:    # Check down, left
                queen  = (queen[0] + 1, queen[1] - 1)
                if (queen in self.locations) and (queen, init) not in conflicts:
                    conflicts.append((queen, init))
            queen = init    # Restore queen to initial location
            
        #return "Attacking pairs = " + str(conflicts)
        #print("Conflicts:\n")
        #for conflict in conflicts:
        #    print(str(conflict) + "\n")
        return len(conflicts) / 2



if __name__ == "__main__":
    # 4 states
    agent1 = nQueens()
    agent1.generateStates()

