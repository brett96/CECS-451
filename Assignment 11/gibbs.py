def gibbs(numSamples, x, e):
	n = int(sys.argv[1])
	counts = [0, 0, 0, 0]
	nonEvidence = ["cloudy", "rain"]
	currentState = [True, True, False, False]
	probCloudy = [0.5]
	probSprinkler = [0.1, 0.5]
	probRain = [0.8, 0.2]
	probWetGrass = [0.99, 0.9, 0.9, 0]


	#P(C|S,R)
	#P(C|S,~R)
	#P(R|C,S,W)
	#P(R|~C,S,W)

	for j in range(1, counts):
		for z in nonEvidence:
			#set the value of Zi in x by sampling from P(Zi|mb(Zi))
			counts[x] += 1
	return Normalize(N)

def Normalize(N):
	norm = [float(i)/max(N) for i in N]
	pass