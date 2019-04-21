import random
# Find: P(Rain | Sprinkler = true; WetGrass = true)

counts = [0, 0]
def gibbs(numSamples, x, e):
	#n = int(sys.argv[1])
	#[cloudy, sprinkler, rain, wetgrass]
	nonEvidence = {"cloudy":True, "rain":False}
	currentState = [True, True, False, False]
	# Hard code probabilities:
	probC = 0.5 		# P(cloudy)
	probSC = .1 		# P(S|C=true)
	probSNotC = .5 		# P(S|C=false)
	probRC = .8 		# P(R|C=true)
	probRNotC = .2 		# P(R|C=false)
	probWSR = .99 		# P(W|S=true, R=true)
	probWSNotR = .9 	# P(W|S=true, R=false)
	probWNotSR = .9 	# P(W|S=false, R=true)
	probWNotSNotR = 0  	# P(W|S=false, R=false)

	# probSprinkler = [0.1, 0.5]
	# probRain = [0.8, 0.2]
	# probWetGrass = [0.99, 0.9, 0.9, 0]


	#P(C|S,R)
	#P(C|S,~R)
	#P(R|C,S,W)
	#P(R|~C,S,W)

	for j in range(1000000):
		# Randomly pick from non evidence variables
		pick = random.choice(list(nonEvidence.keys()))
		# Flip variable value
		nonEvidence[pick] = not nonEvidence[pick]
		# for z in nonEvidence:
		# 	#set the value of Zi in x by sampling from P(Zi|mb(Zi))
		# 	nonEvidence[z] = not nonEvidence[z]
		# 	counts[list(nonEvidence.keys()).index(z)] += 1
	probRain = 0
	if nonEvidence["cloudy"]:
		probRain = probRC*probWSR / ((probRC*probWSR) + (probRNotC*probWSNotR))
	else:
		probRain = probRNotC*probWSR / ((probRNotC*probWSR) + (probRC*probWSNotR))
	print(nonEvidence)
	return "<" + str(probRain) + ", " + str(1-probRain) + ">"
	#return Normalize(counts)

def Normalize(N):
	return [float(i)/sum(counts) for i in counts]

if __name__ == "__main__":
	print(gibbs(1000000, "rain", ["cloudy", "rain"]))