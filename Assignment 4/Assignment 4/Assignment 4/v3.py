import sys
import random
import numpy
import math

n = int(sys.argv[1])
k = int(sys.argv[2])
MAX_FITNESS_SCORE = math.factorial(n) / math.factorial(2) / math.factorial(n-2)
MAX_ITERATION = 10000
MUTATE_PROB = 0.1


class nQueens:
    def __init__(self):
        self.board = None
        self.fitnessScore = None
        self.probability = None
    
    def setValues(self, board, fitnessScore, probability):
        self.board = board
        self.fitnessScore = fitnessScore
        self.probability = probability
    
    def setBoard(self, board):
        self.board = board
    def setFitnessScore(self, fitnessScore):
        self.fitnessScore = fitnessScore
    def setProbability(self, probability):
        self.probability = probability
    def getBoard(self):
        return self.board
    def getFitnessScore(self):
        return self.fitnessScore
    def getProbability(self):
        return self.probability
        
def makeGeneticList():
    board = numpy.arange(n)
    numpy.random.shuffle(board)
    return board

def makePopulationList(populationSize):
    population = [nQueens() for i in range(populationSize)]
    for i in range(populationSize):
        
        
        population[i].setBoard(makeGeneticList())
        fitnessCheck = calculateFitness(population[i].board)
        
        
        while(fitnessCheck < 0):
            population[i].setBoard(makeGeneticList())
            fitnessCheck = calculateFitness(population[i].board)    
            
        population[i].setFitnessScore(fitnessCheck)
        #print(population[i].board)
        #print("Population fitness: ", population[i].fitnessScore)
    return population
        
def calculateFitness(board):
    #number of conflicts
    conflicts = 0
    rcConflicts  = 0
    #calculate conflicts for rows && columns
    rcConflicts += abs(len(board) - len(numpy.unique(board)))
    conflicts += rcConflicts
    #print("row and column conflicts: ", rcConflicts)
    
    
    #calculate diagonal conflicts
    for i in range(len(board)):
        for j in range(len(board)):
            if(i != j):
                xSlope = abs(i-j)
                ySlope = abs(board[i] - board[j])
                if(xSlope == ySlope):
                    conflicts += 1
    
    #print("diagonal conflicts: ", conflicts - rcConflicts)
    
    
    score = MAX_FITNESS_SCORE - conflicts
    #print("conflicts: " , conflicts)
    #print("max fitness score: ", MAX_FITNESS_SCORE)
    #print("fitness score: ", score)
    return score
        
# =============================================================================
#         length = len(list)
#         conflicts = 0
#         uniqueLength = len(np.unique(list))
#         if length == uniqueLength:
#             xyConflicts = 0
#         else:
#             xyConflicts = abs(length - uniqueLength)
#         conflicts += xyConflicts
# 
#         for i in range(len(list)):
#             for j in range(len(list)):
#                 if(i != j):
#                     diagLeft = abs(i-j)
#                     diagRight = abs(list[i] - list[j])
#                     if(diagLeft == diagRight):
#                         conflicts += 1
# 
#         return maxFactorial - conflicts
# 
# =============================================================================

def roulleteWheelSelection(population):
    sumFitness = sum([i.fitnessScore for i in population])
    randomPick = random.uniform(0, sumFitness)
    current = 0
    for p in population:
        current += p.fitnessScore
        if current > randomPick:
            return p


def getParents(population):
    p1 = None
    p2 = None
    
    while p1 != p2 or p1 is None or p2 is None:
        
    #sumFitness = numpy.sum([i.fitnessScore for i in population])
        
    

    #for p in population:
    #    p.probability = p.fitnessScore / sumFitness
        #print("P probability: ",p.board, "\t",  p.probability, "\t", p.fitnessScore, "/", sumFitness)
        
        sumFitness = sum([i.fitnessScore for i in population])
        selectionProbs = [i.fitnessScore / sumFitness for i in population]
        p1 = population[numpy.random.choice(len(population), p = selectionProbs)]
        p2 = population[numpy.random.choice(len(population), p = selectionProbs)]
        
        #p1 = roulleteWheelSelection(population)
        #p2 = roulleteWheelSelection(population)
        
    if p1 is not None and p2 is not None:
        return p1, p2
    else:
        sys.exit(-1)
           
# =============================================================================
#     while True:
#         randomP1 = numpy.random.rand()
#         tempP1 = [i for i in population if i.probability <= randomP1]
#         try:
#             p1 = tempP1[0]
#             break
#         except:
#             pass
#             
#     while True:
#         randomP2 = numpy.random.rand()
#         tempP2 = [i for i in population if i.probability <= randomP2]
#         try:
#             indexP2 = numpy.random.randint(len(tempP2))
#             p2 = tempP2[indexP2]
#                                             
#             if p2 != p1:
#                 break
#             else:
#                 print("Equal parents")
#                 while p2 == p1:
#                    indexP2 = numpy.random.randint(len(tempP2))
#                    p2 = tempP2[indexP2]
#                 continue
# 
#                 
#         except:
#             print("Exception")
#             continue
# =============================================================================
        

        
# =============================================================================
#         self.p1, self.p2 = None, None
#         total = np.sum([self.calculateFitness(l) for l in self.boards.values()])
#         for b in self.boards:
#             self.probabilities[b] = self.fitnesses[b] / (total*1.0)
#         while True and len(self.boards) > 0:
#             p1Rand = np.random.rand()
#             p1RN = [x for x in self.boards if self.probabilities[x] <= p1Rand]
#             try:
#                 self.p1 = p1RN[0]
#                 break
#             except:
#                 pass
# 
#         while True and len(self.boards) > 0:
#             p2Rand = np.random.rand()
#             p2RN = [x for x in self.boards if self.probabilities[x] <= p2Rand]
#             try:
#                 t = np.random.randint(len(p2RN))
#                 self.p2 = p2RN[t]
#                 if self.p2 != self.p1:
#                     break
#                 else:
#                     print("Equal Parents")
#                     continue
#             except:
#                 print("Exception")
#                 continue
#         if self.p1 is not None and self.p2 is not None:
#             return self.p1, self.p2
#         else:
#             sys.exit(-1)
# =============================================================================

def crossover(p1, p2):
    crossoverIndex = random.randint(1, k - 1)
    
    child = nQueens()   
    
    cBoard = []


    cBoard.extend(p1.board[0:crossoverIndex])
    cBoard.extend(p2.board[crossoverIndex:])

    
    child.setBoard(cBoard)
    
    fitnessCheck = calculateFitness(child.board)
    #sumFitness = numpy.sum([i.fitnessScore for i in population])
    
    while(fitnessCheck < 0):
        p1, p2 = getParents(population)
        cBoard = []
        cBoard.extend(p1.board[0:crossoverIndex])
        cBoard.extend(p2.board[crossoverIndex:])  
        child.setBoard(cBoard)
        fitnessCheck = calculateFitness(child.board)

        
    child.setFitnessScore(fitnessCheck)
    #child.setProbability(child.fitnessScore / sumFitness)

    
    #print("\nChild: ", child.board, "\t",  child.fitnessScore,  "\t", child.probability, "\n")
    return child
        
# =============================================================================
#         s = str(self.p1)
#         if s.isnumeric():
#             return []
#         globals()
#         crossoverIndex = random.randint(1, k - 1)
#         child = []
#         print(self.p1)
#         child.extend(self.p1[0:crossoverIndex])
#         child.extend(self.p2[crossoverIndex:])
#         fit = self.calculateFitness(child)
#         print(fit)
#         return fit
# =============================================================================

def mutate(child):     
    for i in range(len(child.board)):
        if  random.random() < MUTATE_PROB:
            #print("Mutated")
            #print("Old board: ", child.board)
            #mutationIndex = numpy.random.randint(n-1)
            #oldVal = child.board[i]
            newVal = numpy.random.randint(n-1)
            child.board[i] = newVal
            #print("New board: ", child.board)
            #print("Changed: ", oldVal, " --> ", newVal, "at index: ", i, "\n")
    return child

def genetic(iteration):
    
    print (" #"*10 ,"Executing Genetic  generation : ", iteration + 1 , " #"*10)
    newGeneration = []
    newGeneration = [nQueens() for i in range(populationSize)]
        
    for i in range(len(population)):
        p1, p2 = getParents(population)
        #print("\nParent 1: ", p1.board, "\t",  p1.fitnessScore,  "\t", p1.probability)
        #print("Parent 2: ", p2.board, "\t",  p2.fitnessScore,  "\t", p2.probability)
        
        c = mutate(crossover(p1,p2))
            
        newGeneration[i].setValues(c.board, c.fitnessScore, c.probability)
    
    population.append(newGeneration)
    
    #print("New Generation: ")
    #for  g in newGeneration:
    #  print(g.board, "\t",  g.fitnessScore, "\t",  g.probability)
    
    return newGeneration
                  
# =============================================================================
#         newGeneration = {}
#         for i in range(len(self.boards)):
#             if len(self.boards) < 1:
#                 return newGeneration
#             else:
#                 self.p1, self.p2 = self.getParents()
#                 self.child1 = self.crossover()
#             newGeneration[i] = self.child1
#         return newGeneration
# =============================================================================

def isSolved():
    
    fitnessScores = [i.fitnessScore for i in population]
    #print (fitnessScores)
    
    if MAX_FITNESS_SCORE in fitnessScores:
        return True
    
    if iteration == MAX_ITERATION:
       return True
    
    return False

# =============================================================================
#     globals()
#     #if self.boards == None:
#     #    return True
#     f = math.factorial
#     max = f(n) / f(2) / f(n - 2)
#     #print("Boards = ", self.boards)
#     fVals = [self.calculateFitness(l) for l in self.boards.values()]
#     print("max = ", max)
#     print("fVals = ", fVals)
#     # fVals filled w/ 'max' in each index after 1st call of isSolved?
#     if max in fVals:
#         return True
#     return False
# =============================================================================

# =============================================================================
# population = makePopulationList(k)
# 
# print("Population size: ", len(population))
# 
# iteration = 0
# while not isSolved():
#     population = genetic(iteration)
#     iteration += 1
#     
# print("Iteration number: ", iteration)
# for each in population:
#     if each.fitnessScore == MAX_FITNESS_SCORE:
#         print(each.board)
# =============================================================================

def maxFitnessScoreFound(population):
    fitnessScores = [i.fitnessScore for i in population]
    return max(fitnessScores)    

if __name__ == '__main__':
    iteration = 0
    populationSize = k
    population = makePopulationList(populationSize)
    maxScoreFound = 0
    maxScoreFounds = []
    #print("Original Population: ")
    #for p in population:
    #    print(p.board, "\t", p.fitnessScore, "\t", p.probability)
    
    while not isSolved():
 
        population = genetic(iteration)
        iteration += 1
        
        if(maxScoreFound < maxFitnessScoreFound(population)):
            maxScoreFound = maxFitnessScoreFound(population)
            maxScoreFounds.append(iteration)
        
         
    print ("Iterations: ", iteration)
     
    if MAX_FITNESS_SCORE in [i.fitnessScore for i in population]:
        print ("Successful boards: ") 
        for each in population:
            if each.fitnessScore == MAX_FITNESS_SCORE :
                print(each.board)
    else:
        print("Max fitness score found: ", maxScoreFound)
        print("Max fitness score lists amount: ",  len(maxScoreFounds))
        print("Max fitness score found list: ", maxScoreFounds)



# =============================================================================
# if __name__ == '__main__':
#     iteration = 0
#     populationSize = k
#     population = makePopulationList(populationSize)
# 
#     while not isSolved():
# 
#         population = genetic(iteration)
#         iteration += 1
#         
#     print ("Iteration: ", iteration)
#     
#     print ("Successful boards: ") 
#     for each in population:
#         if each.fitnessScore == MAX_FITNESS_SCORE :
#             print(each.board)
# =============================================================================
        
# =============================================================================
#     globals()
#     
#     controller = nQueens()
#     controller.makePopulationList()
#     while not controller.isSolved():
#         controller.boards = controller.genetic()
#         print("Parent 1 = ", controller.p1)
#         print("Parent 2 = ", controller.p2)
# =============================================================================
