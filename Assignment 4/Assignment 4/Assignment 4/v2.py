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
        max = f(n) / f(2) / f(n - 2)
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
        self.p1, self.p2 = None, None
        total = np.sum([self.calculateFitness(l) for l in self.boards.values()])
        for i in range(len(self.boards)):
            self.probabilities[i] = self.fitnesses[i] / (total)
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
            except Exception as e: print(e)

        if self.p1 is not None and self.p2 is not None:
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

        #child.extend(self.p2[crossoverIndex:])

        child1.extend(self.boards[self.p2][crossoverIndex:])
        child2.extend(self.boards[self.p2][0:crossoverIndex])
        child2.extend(self.boards[self.p1][crossoverIndex:])

        return child1, child2


    def genetic(self):
        newGeneration = {}
        #while len(newGeneration) < k:
        for board in self.boards:
            self.p1, self.p2 = self.getParents()


        i = 0
        while i < len(self.boards):
            print("boards = ", self.boards)
            if len(self.boards) < 1:
                print("\nEMPTY BOARD\n")
                return newGeneration
            else:
                # Same child gets added every time
                self.p1, self.p2 = self.getParents()
                child1, child2 = self.crossover()  # Have crossover return a list
                #print("Child = ", self.child1)
            child1 = self.mutate(child1)
            child2 = self.mutate(child2) 
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
        controller.boards = controller.genetic()
        controller.updateFitnesses()
        #print("Parent 1 = ", controller.boards[controller.p1])
        #print("Parent 2 = ", controller.boards[controller.p2])



        