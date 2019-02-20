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
        self.child1 = None
        
        pass

    def makeGeneticList(self):
        global n
        locationList = np.arange(n)
        np.random.shuffle(locationList)
        return locationList

    def makePopulationList(self):
        global k
        populationSize = k
        for i in range(populationSize):
            self.boards[i] = self.makeGeneticList()
            self.fitnesses[i] = self.calculateFitness(self.boards[i])

    def calculateFitness(self, list):
        print("list = ", list)
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
        if self.boards == None:
            return True
        f = math.factorial
        max = f(n) / f(2) / f(n - 2)
        print("Boards = ", self.boards)
        fVals = [self.calculateFitness(l) for l in self.boards.values()]
        if max in fVals:
            return True
        return False


    def getParents(self):
        globals()
        self.p1, self.p2 = None, None
        total = np.sum([self.calculateFitness(l) for l in self.boards.values()])
        for b in self.boards:
            self.probabilities[b] = self.fitnesses[b] / (total*1.0)
        while True and len(self.boards) > 0:
            p1Rand = np.random.rand()
            p1RN = [x for x in self.boards if self.probabilities[x] <= p1Rand]
            try:
                self.p1 = p1RN[0]
                break
            except:
                pass

        while True and len(self.boards) > 0:
            p2Rand = np.random.rand()
            p2RN = [x for x in self.boards if self.probabilities[x] <= p2Rand]
            try:
                t = np.random.randint(len(p2RN))
                self.p2 = p2RN[t]
                if self.p2 != self.p1:
                    break
                else:
                    print("Equal Parents")
                    continue
            except:
                print("Exception")
                continue
        if self.p1 is not None and self.p2 is not None:
            return self.p1, self.p2
        else:
            sys.exit(-1)



    def crossover(self):
        s = str(self.p1)
        if s.isnumeric():
            return []
        globals()
        crossoverIndex = random.randint(1, k - 1)
        child = []
        print(self.p1)
        child.extend(self.p1[0:crossoverIndex])
        child.extend(self.p2[crossoverIndex:])
        fit = self.calculateFitness(child)
        print(fit)
        return fit


    def genetic(self):
        newGeneration = {}
        for i in range(len(self.boards)):
            if len(self.boards) < 1:
                return newGeneration
            else:
                self.p1, self.p2 = self.getParents()
                self.child1 = self.crossover()
            newGeneration[i] = self.child1
        return newGeneration


if __name__ == '__main__':
    globals()
    controller = nQueens()
    controller.makePopulationList()
    while not controller.isSolved():
        controller.boards = controller.genetic()
        print("Parent 1 = ", controller.p1)
        print("Parent 2 = ", controller.p2)





