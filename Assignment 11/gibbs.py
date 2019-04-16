def gibbs(numSamples, x, e):
	counts = [0, 0, 0, 0]
	nonEvidence = ["cloudy", "rain"]
	currentState = [True, True, False, False]
	probCloudy = 0.5

	for j in range(1, counts):
		for z in nonEvidence:
			#set the value of Zi in x by sampling from P(Zi|mb(Zi))
			counts[x] += 1
	return Normalize(N)

def Normalize(N):
	pass