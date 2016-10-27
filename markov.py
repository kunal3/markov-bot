# Kunal's attempt at Markov bots

# TODO -
# Add cmd line args
# Add some sort of natural language processing for sensibl replies
# Add beginning of sentence as always being a Capital lettered word

import random
import cPickle as pickle

def main():
	inputString = importData("input/The Hunger Games.txt")
	# inputString = importData("Sigmund Freud's Dream Psychology.txt")

	markovChain = createDict(inputString)
	# markovChain = importDict("brains/outputHungerGames.txt")

	# print markovChain

	exportDict(markovChain, "brains/outputHungerGames2.txt")
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
	# Double for loop is bad way to do this. Can be done in single iteration. 

	inputString = inputString.split()
	markovChain = dict()
	print len(inputString)
	for i in range(0, len(inputString)-1):
		word = inputString[i]
		val = inputString[i+1]
		if word not in markovChain:
			markovChain[word] = []
		markovChain[word].append(val)

	return markovChain

def importData(filename):
	with open(filename, 'r') as myfile:
		data = myfile.read().replace('\n', ' ')
	return data

def exportDict(markovChain, filename):
	output = open(filename, 'wb')
	pickle.dump(markovChain, output)
	output.close()

def importDict(filename):
	output = open(filename, 'rb')
	result = pickle.load(output)
	# print result
	return result

main()