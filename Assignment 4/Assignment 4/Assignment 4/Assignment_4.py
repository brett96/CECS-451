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
 

    def generatePopulationList(self):
        populationList = []
        for i in range(int(sys.argv[2])):
            populationList.append([x[0] for x in self.locations] )
        return populationList



    def generateStates(self):   # Genrate 'k' states
        agents = {} # Dictionary assigning each agent an int value
        fitnesses = {}  # Dictionary assigning each agent's int to its fitness
        
        for i in range(0, self.k):
            agent = nQueens()

            agents[i] = agent # Add agent to agent dictionary
            agent.show()

            # Calculate fitness by finding number of non-attacking pairs
            attackingPairs = agent.checkAttacks()   
            fitness = agent.calculateFitness(attackingPairs)
            print(fitness)
            print("Fitness = ", str(fitness))
            fitnesses[i] = fitness    # Add corresponding agent's fitness to fitness dictionary (same keys)
            print("Genetic List = " + str(agent.getGeneticList()))
        totalStateSum = sum(fitnesses.values())
        print(totalStateSum)

        # Convert fitnesses values to percentages
        for i in range(0, self.k):
            fitnesses[i] = fitnesses[i] / totalStateSum
        

        parents = {}
        pcIdx = 0 #Parent/Child dictionary index (key value)
        children = {}
        while len(fitnesses) >= 0:
            if len(fitnesses) == 1:
                print("Single Parent:")
                parent = agents[list(fitnesses.keys())[0]]
                print("Parent = ", parent.getGeneticList())
                print("Child = ", parent.getGeneticList()) # If only 1 parent, make child a clone of the parent
                break
            f = sorted(fitnesses.values())  # Get sorted list of fitness values
            
            r = random.random() # Generate a random number to determine if mutation
            if len(f) == 0: # Stop if list is empty (already made all parents & children
                break
            choice = f[len(f)-1]
            for i in f:
                if i > r:   # If fitness of current parent is greater than generated probability:
                    choice = i  # Choose that parent (choice = parent's fitness)
                    break
        
            parent1 = agents[list(agents.keys())[0]]
            parent2 = agents[list(agents.keys())[0]]
        
            for f in fitnesses.keys():
                if fitnesses[f] == choice:  # If fitness == saved fitness:
                    parent1 = agents[f]         # Use that as parent
                    fitnesses.pop(f)            # Remove fitness from dictionary to choose 2nd parent
                    break
        
            possibleParents = []
            keys = fitnesses.keys()
            for key in keys:
                possibleParents.append(key)
            if len(possibleParents) == 0:
                break
            p2Key = random.choice(possibleParents)
            parent2 = agents[p2Key]
            fitnesses.pop(p2Key)

            print("Parent 1 List = " , parent1.getGeneticList())
            print("Parent 2 list = ", parent2.getGeneticList())


            crossoverInt = random.randint(1, self.numQueens - 1)
        
            parent1List = parent1.getGeneticList()
            parent2List = parent2.getGeneticList()
        
            p1a = parent1List[0:crossoverInt]
            p1b = parent1List[crossoverInt:]
        
            p2a = parent2List[0:crossoverInt]
            p2b = parent2List[crossoverInt:]
        
            child1 = p1a + p2b
            child2 = p2a + p1b
        
            print("Crossover index = ", crossoverInt)
            print("child 1 = ", child1)
            parents[pcIdx] = parent1.getGeneticList()   # Add parents & children to respective dictionaries
            children[pcIdx] = child1
            pcIdx += 1
            print("child 2 = ", child2)
            parents[pcIdx] = parent2.getGeneticList()
            children[pcIdx] = child2
            pcIdx += 1

        
            mutationProb1 = random.random()
            mutationProb2 = random.random()
        
            if(mutationProb1 < 0.05):
                child1 = self.mutation(child1)
            if(mutationProb2 < 0.05):
                child2 = self.mutation(child2)

            print("new child 1 = ", child1)
            print("new child 2 = ", child2)
    


    def getChildCoordinates(self, parent):
        pass
        
    def show(self): # Print out board & queens
        print(np.array(self.board))
        pass
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

    def mutation(self, child):
       index = random.randint(0, len(child) - 1)
       newVal = random.randint(0, len(child) - 1)
       
       child[index] = newVal
       
       return child
       

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
            
        return len(conflicts) / 2



if __name__ == "__main__":
    # 4 states
    agent1 = nQueens()
    agent1.generateStates()

