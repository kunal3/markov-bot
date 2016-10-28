import discord
from markov import main

# Discord integration 
client = discord.Client()

@client.event
async def on_message(message):
    author = message.author
    if message.content.startswith('<@241600786470010881>'):
    	output = main(message.content)
    	await client.send_message(message.channel, output)

tokenFile = open("token.txt", 'r')
token = tokenFile.read()
client.run(str(token))
