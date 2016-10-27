An explanation of the markov depth :

It defines how many words to group before associating them with the following word.

For example, inputString = "My name is Kunal."

markovDepth = 1
Resulting Markov associations - 
{'is': ['Kunal.'], 'My': ['name'], 'name': ['is']} 

markovDepth = 2
Resulting Markov associations - 		
{'My name': ['is'], 'name is': ['Kunal.']}