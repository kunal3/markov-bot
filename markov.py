# Kunal's attempt at Markov bots
import random
import cPickle as pickle

def main():
	inputString = "Hi my name is Kunal and I am a guy.\n	Hi i am jacob and i am a girl!"
	inputString = importData("The Hunger Games.txt")
	# inputString = importData("Sigmund Freud’s Dream Psychology.txt")

	markovChain = createDict(inputString)
	# markovChain = importDict("Hunger Games.txt")

	# print markovChain

	exportDict(markovChain, "outputHungerGames.txt")
	# importDict("output.txt")

	printRandom(markovChain)

	# make brainHarryPotter.txt	
	# make brainLordOfTheRings.txt

def printRandom(markovChain):
	start = random.choice(markovChain.keys())
	reply = start
	nextWord = start
	
	while reply[-1]!="." and reply[-1]!="!" and reply[-1]!="?":
		nextWord = random.choice(markovChain[nextWord])
		reply = reply + " " + nextWord
	
	print reply

def createDict(inputString):
	prevWasKey = 0
	markovChain = dict()
	for word in inputString.split():
		markovChain[word] = []
		for val in inputString.split():
			if prevWasKey:
				prevWasKey = 0
				markovChain[word].append(val)
			if word==val:
				prevWasKey = 1
		prevWasKey = 0
	return markovChain

def importData(filename):
	with open(filename, 'r') as myfile:
		data = myfile.read().replace('\n', ' ')
	return data

def exportDict(markovChain, filename):
	output = open(filename, 'ab+')
	pickle.dump(markovChain, output)
	output.close()

def importDict(filename):
	output = open(filename, 'rb')
	result = pickle.load(output)
	# print result
	return result

main()