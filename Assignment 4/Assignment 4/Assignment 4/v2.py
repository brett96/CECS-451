import sys
import random
import numpy as np
import math
import operator

n = int(sys.argv[1])
k = int(sys.argv[2])

class nQueens:
    def __init__(self):
        self.boards = {}
        self.fitnesses = {}
        self.probabilities = {}
        self.p1 = None
        self.p2 = None
        
        pass

    def makeGeneticList(self):
        global n
        locationList = np.arange(n)
        np.random.shuffle(locationList)
        return list(locationList)

    def makePopulationList(self):
        global k
        populationSize = k
        for i in range(populationSize):
            self.boards[i] = self.makeGeneticList()
            self.fitnesses[i] = self.calculateFitness(self.boards[i])


    def updateFitnesses(self):
        for i in range(len(self.boards)):
            self.fitnesses[i] = self.calculateFitness(self.boards[i])

    def calculateFitness(self, list):
        #print("list = ", list)
        length = len(list)
        conflicts = 0
        uniqueLength = len(np.unique(list))
        if length == uniqueLength:
            xyConflicts = 0
        else:
            xyConflicts = abs(length - uniqueLength)
        conflicts += xyConflicts

        for i in range(len(list)):
            for j in range(len(list)):
                if(i != j):
                    diagLeft = abs(i-j)
                    diagRight = abs(list[i] - list[j])
                    if(diagLeft == diagRight):
                        conflicts += 1

        f = math.factorial
        result = f(n) / f(2) / f(n - 2) - conflicts
        return result

    def isSolved(self):
        globals()
        #if self.boards == None:
        #    return True
        f = math.factorial
        #max = f(n) / f(2) / f(n - 2)
        max = 28
        #print("Boards = ", self.boards)
        fVals = [self.calculateFitness(l) for l in self.boards.values()]
        for i in range(len(self.boards)):
            self.fitnesses[i] = self.calculateFitness(self.boards[i])
        print("max = ", max)
        print("fVals = ", fVals)
        # fVals filled w/ 'max' in each index after 1st call of isSolved?
        if max in fVals:
            return True
        return False


    def getParents(self):
        globals()
        copyBoards = self.boards
        deletedBoards = {}
        deletedFitnesses = {}
        self.p1, self.p2 = 0, 1
        self.fitnesses = {}
        for board in self.boards:
            self.fitnesses[board] = self.calculateFitness(self.boards[board])
        total = np.sum([self.calculateFitness(l) for l in self.boards.values()])
        self.probabilities = {}
        for i in range(len(self.boards)):
            self.probabilities[i] = self.fitnesses[i] / (total)
        #while True:# and len(self.boards) > 0:
        #    p1Rand = np.random.rand()
        #    #p1RN = [x for x in self.boards if self.probabilities[x] <= p1Rand]
        #    #try:
        #    #    self.p1 = p1RN[0]
        #    #    break
        #    #except:
        #    #    pass

        #    f = sorted(self.fitnesses.values())
        #    high = f[len(f)-1]
        #    self.p1 = 0
        #    changed = False
        #    for i in range(len(f)):
        #        if self.fitnesses[i] == high:
        #            self.p1 = i
        #            deletedBoards[i] = self.boards[i]
        #            deletedFitnesses[i] = self.fitnesses[i]
        #            self.fitnesses.pop(i)
        #            self.probabilities.pop(i)
        #            self.boards.pop(i)
        #            changed = True
        #    if not changed:
        #        deletedBoards[0] = self.boards[0]
        #        deletedFitnesses[0] = self.fitnesses[0]
        #        self.fitnesses.pop(0)
        #        self.probabilities.pop(0)
        #        self.boards.pop(0)
        #    #print("p1 = ", self.p1)
        #    break
        #self.p2 = random.choice(list(self.fitnesses.keys()))
        #deletedBoards[self.p2] = self.boards[self.p2]
        #deletedFitnesses[self.p2] = self.fitnesses[self.p2]
        #self.fitnesses.pop(self.p2)
        #self.probabilities.pop(self.p2)
        #self.boards.pop(self.p2)

        while True:
            parent1_random = np.random.rand()
            parent1_rn = [x for x in self.boards if self.probabilities[x] <= parent1_random]
            try:
                parent1 = parent1_rn[0]
                break
            except:
                pass

        while True and len(self.boards) > 0:
            p2Rand = np.random.rand()
            p2RN = [x for x in self.boards if self.probabilities[x] <= p2Rand]
            try:
                t = np.random.randint(len(p2RN))
                self.p2 = p2RN[t]
                print("p2 = ", self.p2)
                if self.p2 != self.p1:
                    break
                else:
                    print("Equal Parents")
                    continue
            except Exception as e: print(e)
        for board in deletedBoards:
            self.boards[board] = deletedBoards[board]
            self.fitnesses[board] = deletedFitnesses[board]
        
        if self.p1 is not None and self.p2 is not None:
            print("FLAG")
            return self.p1, self.p2
        else:
            sys.exit(-1)

    def mutate(self, childList):
        result = childList
        fitness = self.calculateFitness(childList)
        total = np.sum([self.calculateFitness(l) for l in self.boards.values()])
        probability = fitness / total
        if probability < .05:
            newVal = np.random.randint(n)
            result[newVal] = np.random.randint(n)
        return result


    def crossover(self):
        #if s.isnumeric():
        #    return []
        globals()
        crossoverIndex = random.randint(1, k - 1)
        child1 = []
        child2 = []
        #child.extend(self.p1[0:crossoverIndex])

        child1.extend(self.boards[self.p1][0:crossoverIndex])

        child1.extend(self.boards[self.p2][crossoverIndex:])
        child2.extend(self.boards[self.p2][0:crossoverIndex])
        child2.extend(self.boards[self.p1][crossoverIndex:])

        c1Fitness = self.calculateFitness(child1)
        c2Fitness = self.calculateFitness(child2)

        #print("child 1 fitness = ", c1Fitness, "\nChild 2 Fitness = ", c2Fitness)

        p1Fitness = self.calculateFitness(self.boards[self.p1])
        p2Fitness = self.calculateFitness(self.boards[self.p2])
        if c1Fitness < p1Fitness:
            child1 = self.boards[self.p1]
        if c2Fitness < p2Fitness:
            child2 = self.boards[self.p2]

        print("Child 1 = ", child1, ";  Child 2 = ", child2)

        return child1, child2


    def genetic(self):
        newGeneration = {}
        #while len(newGeneration) < k:
        #for board in self.boards:
        #    self.p1, self.p2 = self.getParents()


        i = 0
        length = len(self.boards)
        while i < length:
            print("boards = ", self.boards)
            if len(self.boards) < 1:
                print("\nEMPTY BOARD\n")
                return newGeneration
            else:
                # Same child gets added every time
                self.p1, self.p2 = None, None
                self.p1, self.p2 = self.getParents()  # IS THIS THE PROBLEM?
                #print(self.boards)
                print("Parent 1 = ", self.boards[self.p1], ";  Parent 2 = ", self.boards[self.p2])
                child1, child2 = self.crossover()  # Have crossover return a list
                #print("Child = ", self.child1)
            child1 = self.mutate(child1)
            child2 = self.mutate(child2) 
            print("Parent 1 = ", self.boards[self.p1], ";\tFitness = ", self.calculateFitness(self.boards[self.p1]))
            print("Parent 2 = ", self.boards[self.p2], ";\tFitness = ", self.calculateFitness(self.boards[self.p2]))
            print("Child1 = ", child1, ";\tFitness = ", self.calculateFitness(child1))
            print("Child2 = ", child2, ";\tFitness =", self.calculateFitness(child2))
            
            newGeneration[i] = child1
            i += 1
            newGeneration[i] = child2
            i += 1
        print("new generation = ", newGeneration)
        return newGeneration


if __name__ == '__main__':
    globals()
    controller = nQueens()
    controller.makePopulationList()
    while not controller.isSolved():
    #for i in range(0,10):
        controller.boards = controller.genetic()
        controller.updateFitnesses()
        #print("Parent 1 = ", controller.boards[controller.p1])
        #print("Parent 2 = ", controller.boards[controller.p2])
        print("\n\n")
    #controller.makePopulationList()
    #while True:
    #    for board in controller.boards:
    #        if controller.calculateFitness(controller.boards[board]) == 28:
    #            break
    #    controller.boards = controller.genetic()
    #    controller.updateFitnesses()


        