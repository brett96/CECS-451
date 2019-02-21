import sys
import random
import numpy
import math

n = int(sys.argv[1])
k = int(sys.argv[2])
MAX_FITNESS_SCORE = math.factorial(n) / math.factorial(2) / math.factorial(n-2)
MAX_ITERATION = 100
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
    
    score = (MAX_FITNESS_SCORE - conflicts) * 1.0
    #print("conflicts: " , conflicts)
    #print("max fitness score: ", MAX_FITNESS_SCORE)
    #print("fitness score: ", score)
    return score
        

def roulleteWheelSelection(population):
    sumFitness = sum([i.fitnessScore for i in population])
    randomPick = random.uniform(0, sumFitness)
    #print("Random pick: ",randomPick)
    current = 0
    for p in population:
        #print(p.fitnessScore)
        current += p.fitnessScore
        if current > randomPick:
            return p

#def tournamentSelection(population):
#    best = None
#    for i=1 to k:
#        ind = population[random(1, n)]
#        if (best == None) or ind.fitnessScore >



def getParents(population):
    p1 = None
    p2 = None
    
    while (p1 is None or p2 is None) and ( p1 == p2) :
        p1 = roulleteWheelSelection(population)
        p2 = roulleteWheelSelection(population)
        
        #sumFitness = numpy.sum([i.fitnessScore for i in population])
        #for p in population:
        #    p.probability = p.fitnessScore / sumFitness
        #print("P probability: ",p.board, "\t",  p.probability, "\t", p.fitnessScore, "/", sumFitness)   
        # sumFitness = sum([i.fitnessScore for i in population])
        #selectionProbs = [i.fitnessScore / sumFitness for i in population]
        #p1 = population[numpy.random.choice(len(population), p = selectionProbs)]
        #p2 = population[numpy.random.choice(len(population), p = selectionProbs)]
        
    if p1 is not None and p2 is not None:
        return p1, p2
    else:
        sys.exit(-1)
           
def crossover(p1, p2):
    crossoverIndex = random.randint(0, k - 1)
    
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

    
    #print("Child: ", child.board, "\t",  child.fitnessScore,  "\t", child.probability)
    #print("Child: ", child.board)
    return child

def mutate(child):     
    for i in range(len(child.board)):
        if  random.random() < MUTATE_PROB:
            #print("Mutated")
            #print("Old board: ", child.board)
            #print("Old fitness score: ", child.fitnessScore)
            #mutationIndex = numpy.random.randint(n-1)
            oldVal = child.board[i]
            newVal = numpy.random.randint(n-1)
            while oldVal == newVal:
                newVal = numpy.random.randint(n-1)
            child.board[i] = newVal
            fitnessCheck = calculateFitness(child.board)
            while(fitnessCheck < 0):
                oldVal = child.board[i]
                newVal = numpy.random.randint(n-1)
                while oldVal == newVal:
                    newVal = numpy.random.randint(n-1)   
                child.board[i] = newVal
                fitnessCheck = calculateFitness(child.board)
            child.setFitnessScore(fitnessCheck)
            #child.setFitnessScore(calculateFitness(child.board))
            #print("New board: ", child.board)
            #print("New fitness score: ", child.fitnessScore)
            #print("Changed: ", oldVal, " --> ", newVal, "at index: ", i, "\n")
    return child

def genetic(population, iteration):
    print (" #"*10 ,"Executing Genetic  generation : ", iteration + 1 , " #"*10)
    newGeneration = []
    newGeneration = [nQueens() for i in range(len(population))]
        
    for i in range(len(population)):
        p1, p2 = getParents(population)
        #print("Parents: ", p1.board, "\t", p2.board)
        #print("\nParent 1: ", p1.board, "\t",  p1.fitnessScore,  "\t", p1.probability)
        #print("Parent 2: ", p2.board, "\t",  p2.fitnessScore,  "\t", p2.probability)
        c = crossover(p1,p2)
        c = mutate(c)
        newGeneration[i].setValues(c.board, c.fitnessScore, c.probability)
    
    population.append(newGeneration)
    
    #print("New Generation: ")
    for  g in newGeneration:
        print(g.board, "\t",  g.fitnessScore)
    
    return newGeneration
                  
def isSolved(population):
    fitnessScores = [i.fitnessScore for i in population]
    #print (fitnessScores)
    if MAX_FITNESS_SCORE in fitnessScores:
        return True
    if iteration == MAX_ITERATION:
       return True
    return False

def maxFitnessScoreFound(population):
    fitnessScores = [i.fitnessScore for i in population]
    return max(fitnessScores)    

if __name__ == '__main__':
    iteration = 0
    populationSize = k
    population = makePopulationList(populationSize)
    maxScoreFound = 0
    maxScoreFounds = []
    
    print("\nOriginal Population: ")
    for p in population:
        print(p.board, "\t", p.fitnessScore)
    
    while not isSolved(population):
 
        population = genetic(population, iteration)
        iteration += 1
        
        if(maxScoreFound < maxFitnessScoreFound(population)):
            maxScoreFound = maxFitnessScoreFound(population)
            maxScoreFounds.append(iteration)
    
    print ("Iterations: ", iteration)
     
    if MAX_FITNESS_SCORE in [i.fitnessScore for i in population]:
        print ("Successful boards: ") 
        for each in population:
            if each.fitnessScore == MAX_FITNESS_SCORE :
                print(each.board, "\t", each.fitnessScore)
    else:
        print("Max fitness score found: ", maxScoreFound)
        print("Max fitness score lists amount: ",  len(maxScoreFounds))
        print("Max fitness score found list: ", maxScoreFounds)


