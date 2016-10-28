# Kunal's attempt at Markov bots

# TODO -
# Add cmd line args
# Add some sort of natural language processing for sensible replies
# Download discord history thru api
# Link to authorize my bot - https://discordapp.com/oauth2/authorize?&client_id=241600786470010881&scope=bot

import random
import pickle
import discord

def main():
	markovDepth = 2
	# inputString = "My name is Kunal."
	# inputString = importTrainingSet("input/The Hunger Games.txt")
	# markovChain, startWords = createMarkovChain(inputString, markovDepth)
	# pickleObject(markovChain, "brains/outputHungerGames.txt")
	# pickleObject(startWords, "startWords/outputHungerGames.txt")

	markovChain = unpickleObject("brains/outputHungerGames.txt")
	startWords = unpickleObject("startWords/outputHungerGames.txt")

	return printRandom(markovChain, startWords, markovDepth)

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

	return (reply)

def createMarkovChain(inputString, markovDepth):
	inputString = inputString.split()
	markovChain = dict()
	startWords = []
	
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

# Discord integration 
client = discord.Client()

@client.event
async def on_message(message):
    author = message.author
    if message.content.startswith('<@241600786470010881>'):
    	output = main()
    	await client.send_message(message.channel, output)

tokenFile = open("token.txt", 'r')
token = tokenFile.read()
client.run(str(token))
