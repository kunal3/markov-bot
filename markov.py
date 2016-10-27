# Kunal's attempt at Markov bots

# TODO -
# Add cmd line args
# Add some sort of natural language processing for sensibl replies
# Download discord history thru api

import random
import cPickle as pickle

def main():
	inputString = importTrainingSet("input/The Hunger Games.txt")
	markovChain, startWords = create2WordDict(inputString)
	pickleObject(markovChain, "brains/outputHungerGames.txt")
	pickleObject(startWords, "startWords/outputHungerGames.txt")

	# markovChain = unpickleObject("brains/outputHungerGames.txt")
	# startWords = unpickleObject("startWords/outputHungerGames.txt")

	print2WordRandom(markovChain, startWords)


def printRandom(markovChain):
	start = random.choice(markovChain.keys())
	reply = start
	nextWord = start
	
	while reply[-1]!="." and reply[-1]!="!" and reply[-1]!="?":
		nextWord = random.choice(markovChain[nextWord])
		reply = reply + " " + nextWord
	
	print reply

def print2WordRandom(markovChain, startWords):
	# start = random.choice(markovChain.keys())
	start = random.choice(startWords)
	reply = start
	nextWord = start
	
	while reply[-1]!="." and reply[-1]!="!" and reply[-1]!="?":
		try:
			nextWord = random.choice(markovChain[nextWord])
		except KeyError:
			nextWord = random.choice(markovChain.keys())
		reply = reply + " " + nextWord
		nextWord = reply.split()[-2] + " " + reply.split()[-1]

	print reply


def createDict(inputString):
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

def create2WordDict(inputString):
	inputString = inputString.split()
	markovChain = dict()
	startWords = []
	print len(inputString)
	for i in range(0, len(inputString)-2):
		word = inputString[i] + " " + inputString[i+1]
		val = inputString[i+2]

		if word[0].isupper():
			startWords.append(word)

		if word not in markovChain:
			markovChain[word] = []
		markovChain[word].append(val)

	return markovChain, startWords

def importTrainingSet(filename):
	with open(filename, 'r') as myfile:
		data = myfile.read().replace('\n', ' ')
	return data

def pickleObject(markovChain, filename):
	output = open(filename, 'wb')
	pickle.dump(markovChain, output)
	output.close()

def unpickleObject(filename):
	output = open(filename, 'rb')
	result = pickle.load(output)
	return result

main()