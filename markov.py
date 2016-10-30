# Kunal's attempt at Markov bots

import random
import pickle

def main(message):
	markovDepth = 2
	markovChain = {}
	startWords = []
	# inputString = "My name is Kunal."
	# inputString = importTrainingSet("input/The Hunger Games.txt")
	inputString = message
	markovChain = unpickleObject("brains/discordTest1.txt")
	startWords = unpickleObject("startWords/discordTest1.txt")
	markovChain, startWords = createMarkovChain(markovChain, startWords, inputString, markovDepth)
	pickleObject(markovChain, "brains/discordTest1.txt")
	pickleObject(startWords, "startWords/discordTest1.txt")

	return printRandom(markovChain, startWords, markovDepth)

# Picks a random starting word and follows it down the markov chain till it encounters
# a period, exclamation or question mark. A starting word is defined as any word that 
# begins with a capital letter.
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
	
	# print (reply)
	return reply

# Keys and values in the markov chain correspond to groups of words and the word
# which most commonly follow them. Markov depth is the variable which dictates 
# how many words are included in a group to form the key. For example -
# inputString = "My name is Kunal."
# markovDepth = 1
# Resulting Markov associations - 
# {'is': ['Kunal.'], 'My': ['name'], 'name': ['is']} 
# markovDepth = 2
# Resulting Markov associations - 		
# {'My name': ['is'], 'name is': ['Kunal.']}
def createMarkovChain(markovChain, startWords, inputString, markovDepth):
	inputString = inputString.split()

	for i in range(0, len(inputString) - markovDepth):
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

# main("Mei is the best defense character. This is important, you need to remember it.")