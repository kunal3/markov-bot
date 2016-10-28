Kunal Agrawal and Jeremy Meyer

------------------------------------------------------------------------------------

An explanation of the markov depth :

It defines how many words to group before associating them with the following word.

For example, inputString = "My name is Kunal."

markovDepth = 1
Resulting Markov associations - 
{'is': ['Kunal.'], 'My': ['name'], 'name': ['is']} 

markovDepth = 2
Resulting Markov associations - 		
{'My name': ['is'], 'name is': ['Kunal.']}

------------------------------------------------------------------------------------

How we plan to have the markov brain talk about a subject :

We have a reverse dictionary for our forward markov chain dictionary.
So the above 2 depth association's reverse dictionary would look something like this - 
{'is': ['My name'], 'Kunal.': ['name is']}

Now, the key is followed by words which precede it. Now we can build a sentence forward
and backwards from our two dictionaries!

This most efficient way of searching for the subject word is to have a third dictionary, 
which takes the keys from the first dictionary and splits it up into single word and associates
every pair, just like you would do to the first dictionary if our markov depth was 1.

Building the sentence forward - 
Take dict 3, find our subject keyword in it, and follow this keyword's values down the rabbit
hole markov depth times. Once we have a string of markov depth length, use this as a key 
for the first dictionary and building your forward sentence.

Building the sentence backwards - 
Since the backwards dictionary will always have keys with a depth of 1, 

------------------------------------------------------------------------------------