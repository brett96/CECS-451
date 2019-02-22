import sys
import random
import numpy
import math

#number of queens
n = int(sys.argv[1]) 
#number of states
k = int(sys.argv[2]) 
#calculate max fitness scores based on n
MAX_FITNESS_SCORE = math.factorial(n) / math.factorial(2) / math.factorial(n-2) 
#number of iterations until stop
MAX_ITERATION = 100
#probability of mutation
MUTATE_PROB = 0.1

class nQueens:
    def __init__(self):
        #location of queens on board
        self.board = None
        #fitness score of the entire board
        self.fitnessScore = None
        #probability of board being chosen
        self.probability = None
    #set all attributes of board
    def setValues(self, board, fitnessScore, probability):
        self.board = board
        self.fitnessScore = fitnessScore
        self.probability = probability
    #set board
    def setBoard(self, board):
        self.board = board
    #set fitness score
    def setFitnessScore(self, fitnessScore):
        self.fitnessScore = fitnessScore
    #set probability
    def setProbability(self, probability):
        self.probability = probability
    #get board
    def getBoard(self):
        return self.board
    #get fitness
    def getFitnessScore(self):
        return self.fitnessScore
    #get probability
    def getProbability(self):
        return self.probability
 
#make a randomized board of queen locations       
def makeGeneticList():
    board = numpy.arange(n)
    numpy.random.shuffle(board)
    return board

#make a population list of size k
def makePopulationList(populationSize):
    #generate nQueens objects
    population = [nQueens() for i in range(populationSize)]
    #generate boards for each nQueens
    for i in range(populationSize):
        population[i].setBoard(makeGeneticList())
        #calculate fitness scores and make sure it is non negative
        fitnessCheck = calculateFitness(population[i].board)
        while(fitnessCheck < 0):
            population[i].setBoard(makeGeneticList())
            fitnessCheck = calculateFitness(population[i].board)    
        #set fitness score to the nQueen object
        population[i].setFitnessScore(fitnessCheck)
    return population

#calculate fitness score of a board
def calculateFitness(board):
    #number of total conflicts
    conflicts = 0
    #number of row/column conflicts
    rcConflicts  = 0 
    #calculate conflicts for rows && columns
    rcConflicts += abs(len(board) - len(numpy.unique(board)))
    conflicts += rcConflicts
    #calculate diagonal conflicts
    for i in range(len(board)):
        for j in range(len(board)):
            if(i != j):
                xSlope = abs(i-j)
                ySlope = abs(board[i] - board[j])
                if(xSlope == ySlope):
                    conflicts += 1
    return MAX_FITNESS_SCORE - conflicts

#selection algorithm used to select parents based on their probability and randomization
def roulleteWheelSelection(population):
    #total sum of all fitness scores in popoulation
    sumFitness = sum([i.fitnessScore for i in population])
    #generate a random number betwen 0 and S
    randomPick = random.uniform(0, sumFitness)
    #current sum
    current = 0
    #start from the beginning of populationa nd keep adding current to fitness score
    #until current > randomPick
    for p in population:
        #print(p.fitnessScore)
        current += p.fitnessScore
        if current > randomPick:
            return p

#get parents from population      
def getParents(population):
    #parent 1
    p1 = None
    #parent 2
    p2 = None 
    #choose parents that are different from each other
    while (p1 is None or p2 is None) and ( p1 == p2):
        p1 = roulleteWheelSelection(population)
        p2 = roulleteWheelSelection(population)
    #checks if parents are not none and returns them        
    if p1 is not None and p2 is not None:
        return p1, p2
    else:
        sys.exit(-1)
  
#crossover between two parents         
def crossover(p1, p2, population):
    #random index where the crossover begins
    crossoverIndex = random.randint(0, k - 1)
    #initialize child object
    child = nQueens() 
    #creates a board to with p1[0: index] + p2[index:]
    cBoard = []
    cBoard.extend(p1.board[0:crossoverIndex])
    cBoard.extend(p2.board[crossoverIndex:])
    #set the child board
    child.setBoard(cBoard)
    #calculates fitness and ch
    fitnessCheck = calculateFitness(child.board)    
    while(fitnessCheck < 0):
        p1, p2 = getParents(population)
        cBoard = []
        cBoard.extend(p1.board[0:crossoverIndex])
        cBoard.extend(p2.board[crossoverIndex:])  
        child.setBoard(cBoard)
        fitnessCheck = calculateFitness(child.board)
    #calculate fitness score of child and make sure it is non negative  
    child.setFitnessScore(fitnessCheck)    
    
    print("Parents: ", p1.board, "\t", p2.board)
    print("Child: ", child.board)
    return child

#mutation of child
def mutate(child):     
    #goes through the entire child board
    for i in range(len(child.board)):
        #generates a random value and if its less than the initialized  mutation prob --> mutate
        if  random.random() < MUTATE_PROB:
            oldVal = child.board[i]
            newVal = numpy.random.randint(n-1)
            #makes sure that the new mutation value is differerent than the old value
            while oldVal == newVal:
                newVal = numpy.random.randint(n-1)
            child.board[i] = newVal
             #calculate new fitness score of child and make sure it is non negative 
            fitnessCheck = calculateFitness(child.board)
            while(fitnessCheck < 0):
                oldVal = child.board[i]
                newVal = numpy.random.randint(n-1)
                #makes sure that the new mutation value is differerent than the old value
                while oldVal == newVal:
                    newVal = numpy.random.randint(n-1)   
                child.board[i] = newVal
                fitnessCheck = calculateFitness(child.board)
            #set the new fitness score
            child.setFitnessScore(fitnessCheck)
    return child

#genetic algorithm
def genetic(population, iteration):
    print (" #"*10 ,"Executing Genetic  generation : ", iteration , " #"*10)
    #define new generation of population
    newGeneration = []
    #initialize nqueens objects for each item in population
    newGeneration = [nQueens() for i in range(len(population))]
    #create and fill the new population with new children
    for i in range(len(population)):
        #get the parents
        p1, p2 = getParents(population)
        #create a child
        c = crossover(p1,p2, population)
        #mutates the child
        c = mutate(c)
        #adds the child to the new generation
        newGeneration[i].setValues(c.board, c.fitnessScore, c.probability)
    #append the new generation to the population
    population.append(newGeneration)
    #for  g in newGeneration:
    #    print(g.board, "\t",  g.fitnessScore)
    return newGeneration

#loop to continue until solution is found
def isSolved(population, iteration):
    #list of all fitness scores in population
    fitnessScores = [i.fitnessScore for i in population]
    #if the  answer is in the list --> return true to end the program
    if MAX_FITNESS_SCORE in fitnessScores:
        return True
    #if the iteration goes until the max --> return true to end the program
    if iteration == MAX_ITERATION:
        print ("\n","#"*20 ,"RESETTING POPULATION", "#"*20,"\n")
        reset()
        return True
    return False

#reset the entire program to create a new population
#reseting is necessary due to poor parent selection
def reset():
    main()

# =============================================================================
# def lastResort():
#     values = numpy.arange(n)
#     fitness = 0
#     while fitness < MAX_FITNESS_SCORE:
#         numpy.random.shuffle(values )
#         fitness = calculateFitness(values)
#         print(values)
#     print(values)
# =============================================================================

#return the max fitness score found
def maxFitnessScoreFound(population):
    fitnessScores = [i.fitnessScore for i in population]
    return max(fitnessScores)    

def main():
    iteration = 0
    populationSize = k
    population = makePopulationList(populationSize)
    #Begin genetic algorithm recursion
    while not isSolved(population, iteration):
        #initialize genetic algorithm
        population = genetic(population, iteration)
        iteration += 1
    
    #If max fitness score is found in search

    if MAX_FITNESS_SCORE in [i.fitnessScore for i in population]:
        print ("\nIterations: ", iteration)
        print ("Successful boards: ") 
        for each in population:
            if each.fitnessScore == MAX_FITNESS_SCORE :
                print(each.board)

if __name__ == "__main__":
    main()