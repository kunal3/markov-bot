# Kunal's attempt at Markov bots

# TODO -
# Add cmd line args
# Add some sort of natural language processing for sensible replies
# Download discord history thru api

import random
import cPickle as pickle

def main():
	markovDepth = 2
	# inputString = "My name is Kunal."
	inputString = importTrainingSet("input/The Hunger Games.txt")
	markovChain, startWords = createMarkovChain(inputString, markovDepth)
	pickleObject(markovChain, "brains/outputHungerGames.txt")
	pickleObject(startWords, "startWords/outputHungerGames.txt")

	# markovChain = unpickleObject("brains/outputHungerGames.txt")
	# startWords = unpickleObject("startWords/outputHungerGames.txt")

	printRandom(markovChain, startWords, markovDepth)

def printRandom(markovChain, startWords, markovDepth):
	start = random.choice(startWords)
	reply = start
	nextWord = start
	
	while reply[-1]!="." and reply[-1]!="!" and reply[-1]!="?":
		try:
			nextWord = random.choice(markovChain[nextWord])
		except KeyError:
			nextWord = random.choice(markovChain.keys())
		reply = reply + " " + nextWord
		nextWord = " ".join(reply.split()[-markovDepth:])

	print reply

def createMarkovChain(inputString, markovDepth):
	inputString = inputString.split()
	markovChain = dict()
	startWords = []

	print "Corpus size = ", len(inputString)
	
	for i in range(0, len(inputString) - markovDepth):

		# Define the key and value. This is done in a loop because
		# you can change how many words form a key. For example -
		# inputString = "My name is Kunal."
		# markovDepth = 1
		# Resulting Markov associations - 
		# {'is': ['Kunal.'], 'My': ['name'], 'name': ['is']} 
		# markovDepth = 2
		# Resulting Markov associations - 		
		# {'My name': ['is'], 'name is': ['Kunal.']}

		key = ""
		for j in range(i, i+markovDepth-1):
			key = key + inputString[j] + " "
		key = key + inputString[i+markovDepth-1]
		val = inputString[i+markovDepth]

		# This list is used to start sentences with Capital letters
		if key[0].isupper():
			startWords.append(key)

		# Adding new key association to chain
		if key not in markovChain:
			markovChain[key] = []
		markovChain[key].append(val)

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